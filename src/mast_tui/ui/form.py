from dataclasses import dataclass
from typing import List


@dataclass
class FormField:
    """Represents a single input field in the form."""
    label: str
    mast_field_name: str
    example: str = ""
    value: str = ""
    is_focused: bool = False
    is_editing: bool = False


class AdvancedSearchForm:
    """Manages the advanced search form state and interactions."""
    def __init__(self):
        self.fields: List[FormField] = [
            FormField("Mission", "obs_collection", "e.g., HST, JWST"),
            FormField("Instrument", "instrument_name", "e.g., WFC3/IR"),
            FormField("Target Name", "target_name", "e.g., M31, NGC 104"),
            FormField("Filters", "filters", "e.g., F160W"),
            FormField("Proposal ID", "proposal_id", "e.g., 12061"),
            FormField("PI Name", "proposal_pi", "e.g., Brown"),
            FormField("Waveband", "wavelength_region", "e.g., Optical, UV"),
            FormField("Product Type", "dataproduct_type", "e.g., image, spectrum"),
            FormField("Project", "project", "e.g., HSC"),
            FormField("Obj. Type", "target_classification", "e.g., GALAXY"),
            FormField("Calib. Level", "calib_level", "e.g., 2, 3"),
            FormField("Obs. ID", "obs_id", "e.g., j8pu01010"),
            FormField("Intent Type", "intentType", "science or calibration"),
            FormField("Min. Wave.", "em_min", "e.g., 1.2e-07 (meters)"),
            FormField("Max. Wave.", "em_max", "e.g., 2.5e-07 (meters)"),
        ]
        self.fields[0].is_focused = True
        self.focused_index = 0
        self.scroll_offset = 0

    def process_input(self, val, state, term):
        """Handle input for the form."""
        field = self.fields[self.focused_index]

        if field.is_editing:
            if val.is_sequence:
                if val.name == "KEY_ENTER" or val.name == "KEY_TAB":
                    field.is_editing = False
                elif val.name == "KEY_ESCAPE":
                    field.is_editing = False
                elif val.name == "KEY_BACKSPACE" or val.name == "KEY_DELETE":
                    field.value = field.value[:-1]
            elif val:
                # Regular character input
                if not ord(val[0]) < 32:
                    field.value += val
            return

        # Check for Ctrl+S (ASCII 19)
        if val and ord(val[0]) == 19:
            # Trigger search
            return "SEARCH"

        # Check for / to clear form
        if val == "/":
            for f in self.fields:
                f.value = ""
            self.fields[self.focused_index].is_focused = False
            self.focused_index = 0
            self.fields[0].is_focused = True
            self.scroll_offset = 0
            return "CLEAR"

        if val.is_sequence:
            if val.name == "KEY_DOWN":
                field.is_focused = False
                self.focused_index = (self.focused_index + 1) % len(self.fields)
                self.fields[self.focused_index].is_focused = True
                self._update_scroll(term)
            elif val.name == "KEY_UP":
                field.is_focused = False
                self.focused_index = (self.focused_index - 1) % len(self.fields)
                self.fields[self.focused_index].is_focused = True
                self._update_scroll(term)
            elif val.name == "KEY_ENTER" or val.name == "KEY_TAB":
                field.is_editing = True
            elif val.name == "KEY_ESCAPE":
                return "EXIT"
        elif val == "\x1b":  # ESC character if not caught as sequence
            return "EXIT"

        return None

    def _update_scroll(self, term):
        """Adjust scroll offset if focus is out of view."""
        max_visible = term.height - 7 # Reserve space for title, prompt, headers, status
        if self.focused_index < self.scroll_offset:
            self.scroll_offset = self.focused_index
        elif self.focused_index >= self.scroll_offset + max_visible:
            self.scroll_offset = self.focused_index - max_visible + 1

    def render(self, term):
        """Render the form to the terminal."""
        start_y = 3
        title = "Advanced Search (MAST Observations.query_criteria)"
        print(term.move_xy(0, start_y) + term.bold(title))
        print(term.move_xy(0, start_y + 1) + "-" * term.width)

        max_visible = term.height - 7
        end_idx = self.scroll_offset + max_visible
        visible_fields = self.fields[self.scroll_offset : end_idx]

        for i, field in enumerate(visible_fields):
            y = start_y + 3 + i
            label_text = f"{field.label:15}: "

            if field.is_editing:
                value_text = field.value + term.reverse(" ")
            else:
                value_text = field.value if field.value else "[Empty]"

            example_text = term.italic(term.color(8)(f" ({field.example})"))
            line = f"{label_text} {value_text}"

            if field.is_focused:
                if field.is_editing:
                    bg = term.black_on_yellow(line.ljust(term.width))
                    print(term.move_xy(0, y) + bg)
                    x_pos = len(label_text) + len(field.value) + 2
                    print(term.move_xy(x_pos, y) + example_text)
                else:
                    bg = term.black_on_cyan(line.ljust(term.width))
                    print(term.move_xy(0, y) + bg)
                    x_pos = len(label_text) + len(value_text) + 1
                    print(term.move_xy(x_pos, y) + example_text)
            else:
                padding_len = term.width - len(line) - len(field.example) - 3
                padding = " " * padding_len
                print(term.move_xy(0, y) + line + example_text + padding)

        # Show indicator if more fields are available
        if self.scroll_offset > 0:
            print(term.move_xy(term.width - 5, start_y + 2) + term.bold("^ More"))
        if self.scroll_offset + max_visible < len(self.fields):
            y_pos = start_y + 3 + max_visible
            print(term.move_xy(term.width - 5, y_pos) + term.bold("v More"))

    def get_filters(self):
        """Return a dictionary of the current form values."""
        return {f.mast_field_name: f.value for f in self.fields if f.value}
