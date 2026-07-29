# Checkbox Automation

A desktop automation tool designed to handle a repetitive manual task in a back-office system.

## Overview

The application receives a list of customer IDs and processes each customer one at a time.

For every customer, it:

1. Opens the customer card.
2. Checks whether a specific checkbox is enabled.
3. If the checkbox is enabled:

   * Unticks the checkbox.
   * Confirms the change.
   * Accepts the two confirmation alerts.
4. Closes the customer card.
5. Continues to the next customer.

If the checkbox is already disabled, the application closes the customer card without making changes and continues to the next customer.

## How It Works

The automation uses mouse controls and pixel-color detection.

Because each customer card opens in the same position, the application can:

* Move the mouse to predefined screen coordinates.
* Read the RGB color of a specific pixel.
* Determine whether the checkbox is enabled.
* Click the required buttons automatically.

## Usage

1. Prepare an Excel file containing the customer IDs.
2. Open the application.
3. Select the Excel file.
4. Click **Start**.
5. Click the back-office application window within two seconds.

The automation will then begin processing the customers from the Excel file.

## Testing Mouse Positions and Pixel Colors

The test module can be used to determine:

* Mouse coordinates.
* Pixel colors in RGB format.

Run the test module and move the mouse to the desired location within five seconds.

The module will display the mouse position and the RGB value of the selected pixel.

## Building the Executable

Use PyInstaller to create a standalone Windows executable:

```bash
pyinstaller --onefile --noconsole --name CheckboxAutomation gui_script.py
```

The generated executable will be located inside the `dist` directory:

```text
dist/CheckboxAutomation.exe
```

## Important Notes

* Keep the back-office window in the same position and size while the automation is running.
* Do not move the mouse or interact with the computer during the process.
* Display scaling, screen resolution, or UI layout changes may affect mouse coordinates and pixel-color detection.
* Test the automation with a small customer list before processing a large file.
