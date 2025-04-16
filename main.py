import tkinter as tk
import shutil
import os
from pathlib import Path

window = tk.Tk()
log_box = tk.Text(window, height=30, width=90, state=tk.NORMAL)

# We want to be able to see the logs inside of the GUI.
def log_message(text_widget, message):
    text_widget.insert(tk.END, message + "\n")
    text_widget.see(tk.END)

checkboxes = []

# Function to delete selected folders
# Note: This function will delete the folders permanently, so use with caution.
def cleanup():
    checked_values = [var.get() for var in checkboxes]
    folder_paths = list(folders.values())
    for i in range(len(folders)):
        if checked_values[i] == 1:
            folder = folder_paths[i]
            if os.path.exists(folder):
                try:
                    # Attempt to delete the folder
                    shutil.rmtree(folder)
                    log_message(log_box, f"Successfully deleted {folder}")
                except PermissionError:
                    log_message(log_box, f"Permission denied for {folder}.\nTry running as administrator.\n")
                except Exception as e:
                    log_message(log_box, f"Error deleting {folder}: {e}")
            

window.title("Cleaning Tool for Windows (Needs Admin)")
window.geometry("600x400")
window.resizable(False, False)
# More folders can be defined here.
folders = {
    "Downloads": str(Path.home() / "Downloads"),
    "Temporary Files": "C:\\Windows\\Temp",
    "Recycle Bin": "C:\\$Recycle.Bin",
    "Windows.old": "C:\\Windows.old"
}
# Create checkboxes for each folder
for f in folders:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(window, text=f, variable=var)
    checkbox.pack()
    checkboxes.append(var)

clean_button = tk.Button(window, text="Clean", command=cleanup)
clean_button.pack()

log_box.pack()
log_message(log_box, "App by Keith Petrone\n\nSelect folders to delete and click 'Clean'\n\nNote: This app needs to be run as a system-level administrator\nto delete certain folders.\n\n")

window.mainloop()
