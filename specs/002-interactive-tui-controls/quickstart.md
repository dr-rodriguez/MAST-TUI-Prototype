# Quickstart: Interactive TUI Controls and Status Line

## Features
- Persistent title and gray prompt.
- Status line at the bottom.
- Slash-commands and keyboard shortcuts.
- Help menu with display state restoration.

## Interactive Guide

1.  **Launch**: Run `mast-tui`.
2.  **Prompt**: You will see a gray line with a blinking cursor. Start typing to see the prompt buffer update.
3.  **Help**: Press `?` or type `/help` and press `Enter` to open the help menu.
4.  **Exit Help**: Press `Esc` or `q` while in the help menu to return to your previous screen.
5.  **Clear Prompt**: Press `Esc` once to clear any text in the prompt.
6.  **Clear Display**: Type `/clear` and press `Enter` to empty the main display area.
7.  **Quit**: Type `/exit` or press `Esc` twice in rapid succession to exit.

## Keyboard Reference

| Key | Action |
|---|---|
| `?` | Open Help Menu |
| `/help` + `Enter` | Open Help Menu |
| `/exit` + `Enter` | Quit |
| `Esc-Esc` | Quit |
| `/clear` + `Enter` | Clear Display |
| `Esc` | Clear Prompt |
| `q` | Exit Help (if open) |
| `Backspace` | Edit Prompt |
