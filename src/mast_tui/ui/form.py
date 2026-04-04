from dataclasses import dataclass
from typing import List, Optional

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
        ]
        self.fields[0].is_focused = True
        self.focused_index = 0

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
            
        # Check for / to clear form (as per T018)
        if val == "/":
            for f in self.fields:
                f.value = ""
            self.fields[self.focused_index].is_focused = False
            self.focused_index = 0
            self.fields[0].is_focused = True
            return "CLEAR"

        if val.is_sequence:
            if val.name == "KEY_DOWN":
                field.is_focused = False
                self.focused_index = (self.focused_index + 1) % len(self.fields)
                self.fields[self.focused_index].is_focused = True
            elif val.name == "KEY_UP":
                field.is_focused = False
                self.focused_index = (self.focused_index - 1) % len(self.fields)
                self.fields[self.focused_index].is_focused = True
            elif val.name == "KEY_ENTER" or val.name == "KEY_TAB":
                field.is_editing = True
            elif val.name == "KEY_ESCAPE":
                return "EXIT"
        elif val == "\x1b":  # ESC character if not caught as sequence
            return "EXIT"
            
        return None

    def render(self, term):
        """Render the form to the terminal."""
        start_y = 3
        print(term.move_xy(0, start_y) + term.bold("Advanced Search (MAST query_criteria)"))
        print(term.move_xy(0, start_y + 1) + "-" * term.width)

        for i, field in enumerate(self.fields):
            y = start_y + 3 + i
            label_text = f"{field.label:15}: "
            
            if field.is_editing:
                # Show underscore cursor or different style while editing
                value_text = field.value + term.reverse(" ")
            else:
                value_text = field.value if field.value else "[Empty]"
            
            # Add example text
            example_text = term.italic(term.color(8)(f" ({field.example})"))
            
            line = f"{label_text} {value_text}"
            
            if field.is_focused:
                if field.is_editing:
                    # Highlight line, then add example separately to avoid coloring it with yellow background
                    print(term.move_xy(0, y) + term.black_on_yellow(line.ljust(term.width)))
                    print(term.move_xy(len(label_text) + len(field.value) + 2, y) + example_text)
                else:
                    print(term.move_xy(0, y) + term.black_on_cyan(line.ljust(term.width)))
                    print(term.move_xy(len(label_text) + len(value_text) + 1, y) + example_text)
            else:
                print(term.move_xy(0, y) + line + example_text + " " * (term.width - len(line) - len(field.example) - 3))
                
    def get_filters(self):
        """Return a dictionary of the current form values."""
        return {f.mast_field_name: f.value for f in self.fields if f.value}
