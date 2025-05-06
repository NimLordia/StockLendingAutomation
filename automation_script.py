import keyboard  # <-- for ESC detection

from tkinter import messagebox
import pyautogui
import pandas as pd
import time
import pyperclip

pyautogui.FAILSAFE = True

# Defined screen positions
checkbox_location = (1361, 295)
alert1_location = (908, 554)
alert2_location = (939, 561)
bo_reselect_location = (1523, 80)

# Defined RGB colors
UNCHECKED_RGB = (174, 224, 247)
CHECKED_RGB = (75, 108, 151)

def run_automation(file_path, output_path='automation_results.xlsx'):
    customer_data = pd.read_excel(file_path)
    results = []

    for customer_id in customer_data['GCID']:
        if keyboard.is_pressed('esc'):
            messagebox.showinfo("Operation Stopped", "Automation stopped by user (ESC pressed).")
            break
        customer_id_str = str(customer_id)
        if customer_id_str.endswith('.0'):
            customer_id_str = customer_id_str[:-2]

        pyperclip.copy(customer_id_str)
        time.sleep(2)  # Allow time to manually focus BO window

        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)

        pyautogui.press('tab')
        time.sleep(0.3)

        pyautogui.press('g')
        time.sleep(0.2)

        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.press('enter')
        time.sleep(8)

        checkbox_pixel = pyautogui.pixel(*checkbox_location)

        if checkbox_pixel == CHECKED_RGB:
            pyautogui.click(checkbox_location)
            time.sleep(0.5)

            pyautogui.click(alert1_location)
            time.sleep(1)

            pyautogui.click(alert2_location)
            time.sleep(1)

            pyautogui.click(bo_reselect_location)
            time.sleep(1)

            result = 'Checkbox unchecked, alerts approved, BO reselected'

        elif checkbox_pixel == UNCHECKED_RGB:
            result = 'Checkbox already unchecked'
            pyautogui.click(bo_reselect_location)
            time.sleep(1)

        else:
            result = f'Unexpected color detected: {checkbox_pixel}'
            pyautogui.click(bo_reselect_location)
            time.sleep(1)

        results.append({'GCID': customer_id_str, 'Result': result})

        time.sleep(1)

    pd.DataFrame(results).to_excel(output_path, index=False)
