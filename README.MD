# Stock Lending Automation

A Python desktop automation prototype for processing stock-lending opt-outs in a legacy back-office system. It reads customer IDs from Excel, navigates customer records, checks a checkbox using its pixel color, and exports a record of attempted actions.

The project explores a practical approach to repetitive work in a desktop interface: PyAutoGUI supplies mouse and keyboard input, while a small Tkinter GUI lets an operator select an input file. Its current implementation depends on one specific screen layout and requires calibration before use.

## Workflow

1. Read the `GCID` column from the first worksheet of an Excel workbook.
2. Search for each customer using the back-office application's keyboard workflow.
3. Sample a pixel at the checkbox position.
4. If the pixel matches the checked color, click the checkbox and confirmation buttons. If it matches the unchecked color, skip the change. Record unexpected colors for review.
5. Return focus to the back-office interface and continue.
6. Write `GCID` and `Result` columns to `automation_results.xlsx` when the loop ends normally or stops through the ESC check.

The report describes the actions the script attempted; the script does not verify the selected customer's identity or confirm that a change was saved.

## Setup

Use Windows with Python 3.11 and an interactive desktop session. The target back-office application is not included. Run these commands in PowerShell from the repository directory:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe gui_script.py
```

Using the virtual environment's Python directly avoids a dependency on PowerShell activation settings.

## Input workbook

Provide an `.xlsx` file whose first worksheet has a header named exactly `GCID`, with one customer ID per row and no blank IDs.

| GCID |
| --- |
| DEMO001 |
| DEMO002 |
| DEMO003 |

[examples/sample_customers.xlsx](examples/sample_customers.xlsx) contains these synthetic text IDs. They demonstrate the file format and do not correspond to real customer records. Selecting this sample still starts the normal desktop automation; there is no dry-run mode.

The current Excel import infers column types. Numeric-looking IDs can lose leading zeros, even if stored as text, and blank rows are not validated. Check inputs manually and avoid using this version for IDs whose leading zeros must be preserved.

## Calibrate and run

The coordinates and RGB constants in `automation_script.py` are examples from the original setup. Before running:

1. Place the back-office window in a fixed position and size. Keep display resolution, scaling, and application theme consistent.
2. Run the pixel inspection utility and move the pointer to the target within five seconds:

   ```powershell
   .\.venv\Scripts\python.exe tools\inspect_pixel.py
   ```

3. Use the printed position and RGB value to update `checkbox_location`, `alert1_location`, `alert2_location`, `bo_reselect_location`, `CHECKED_RGB`, and `UNCHECKED_RGB` in `automation_script.py`. Inspect the checkbox in both states.
4. Check that the search keystrokes, confirmation sequence, and fixed delays match the target application. Calibration of coordinates alone does not make the script compatible with another application.
5. Start the GUI, choose a validated workbook, and click **Start Automation** once. Focus the back-office window within two seconds, then leave the mouse and keyboard idle.
6. Manually verify the resulting customer state and review the report. Begin with a small list in a test environment.

`automation_results.xlsx` is saved in the working directory and overwritten by the next run.

### Stopping a run

- Hold **ESC** until the script checks it at the start of the next customer. This is not an immediate stop; the current customer can finish first.
- Moving the mouse to the top-left screen corner triggers PyAutoGUI's fail-safe on a subsequent applicable PyAutoGUI call. This raises an exception, so the current implementation may exit without saving the report.

## Current limitations

- Fixed coordinates, exact pixel colors, and fixed delays make the workflow sensitive to layout changes, slow responses, and focus changes.
- The script does not verify the active window, customer identity, or checkbox state after clicking. A reported action is not proof of a successful update.
- Results are saved only after the loop. An exception can lose all results from the run.
- The Start button remains enabled during execution. Repeated clicks can launch competing workers; run only one instance at a time.
- ESC cancellation can still display the GUI's completion dialog. Review the report to determine which customers were processed.
- Input validation and automated tests have not yet been added. `tools/inspect_pixel.py` is a manual calibration utility.

These are the main next steps for making the prototype reliable enough for unattended use.

## Build a Windows executable

From the repository directory, use the checked-in PyInstaller specification:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --clean --noconfirm StockLendingAutomation.spec
```

The executable is written to `dist\StockLendingAutomation.exe`. Rebuild after changing coordinates or other source settings.

Build output, executables, Python caches, local environments, and generated result workbooks are excluded from version control. The repository contains source code and an explicitly synthetic example workbook; distribute packaged executables separately through GitHub Releases when needed.

## Repository layout

```text
automation_script.py           Desktop workflow and Excel report
gui_script.py                  Tkinter file selection and launch controls
requirements.txt               Pinned Python dependencies
StockLendingAutomation.spec    PyInstaller build configuration
tools/inspect_pixel.py         Manual mouse-position and RGB inspection
examples/sample_customers.xlsx Synthetic input format example
```
