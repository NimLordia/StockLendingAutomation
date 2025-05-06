import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import automation_script

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        entry_filepath.delete(0, tk.END)
        entry_filepath.insert(0, file_path)

def start_automation():
    file_path = entry_filepath.get()
    if not file_path:
        messagebox.showerror("Error", "Please select an Excel file.")
        return
    threading.Thread(target=run_thread, args=(file_path,)).start()

def run_thread(file_path):
    automation_script.run_automation(file_path)
    messagebox.showinfo("Success", "Automation Completed!\nResults saved to automation_results.xlsx")

# GUI Setup
root = tk.Tk()
root.title("Stock Lending Opt Out Automation")
root.geometry("500x250")

tk.Label(root, text="Select Customer Excel File:").pack(pady=10)
entry_filepath = tk.Entry(root, width=50)
entry_filepath.pack(pady=5)
tk.Button(root, text="Browse...", command=select_file).pack()
tk.Label(root, text="After clicking on 'Start Automation' you have 2 seconds to click on BO and select it").pack(pady=10)
tk.Label(root, text="To stop the operation, move the mouse to the top left corner of the screen").pack(pady=10)
tk.Button(root, text="Start Automation", command=start_automation, bg="green", fg="white").pack(pady=20)

root.mainloop()
