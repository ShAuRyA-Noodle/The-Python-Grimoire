"""
cursor_tracker.py
-----------------

Utility script to continuously display the current mouse cursor coordinates.
This is primarily used during GUI automation development to determine accurate
screen positions for automated clicking, dragging, or input actions.

Safety:
- PyAutoGUI failsafe is enabled, allowing the script to terminate immediately
  if the cursor is moved to any screen corner.
- The script can also be stopped safely using Ctrl+C (KeyboardInterrupt).
"""

import time
import pyautogui


# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------

# Moving the cursor to a screen corner immediately aborts the script.
pyautogui.FAILSAFE = True

# Introduces a small pause after each PyAutoGUI call for stability.
pyautogui.PAUSE = 0.05


# ---------------------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------------------

def main():
    """
    Continuously print the current mouse cursor position at a fixed interval.
    This helps developers identify precise screen coordinates for automation tasks.
    """
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Cursor position -> X: {x}, Y: {y}")
            time.sleep(0.2)

    except KeyboardInterrupt:
        # Graceful shutdown when user presses Ctrl+C
        print("\nCursor tracking stopped by user.")


if __name__ == "__main__":
    main()
