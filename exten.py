import os
import tkinter as tk
from tkinter import messagebox
import time

def check_extension(filename):
    # Read the list of common extensions from a file
    with open("extened.txt", "r") as file:
        common_extensions = [line.strip() for line in file.readlines()]

    # Get the extension of the file
    extension = os.path.splitext(filename)[1]

    # Check if the extension is in the list of common extensions
    if extension not in common_extensions:
        # Display a dialog box with the uncommon extension and two options
        result = messagebox.askyesno("Uncommon extension found", f"An uncommon extension {extension} was found. Do you want to restore the system to the last recovery?")

        # Restore the system to the last recovery if the "Restore" option is chosen
        if result == True:
            # Code to restore the system to the last recovery
            pass
        else:
            # Close the dialog box if a "No" option is chosen
            tk.messagebox._show("", "", icon="warning", type="ok", parent=None)
            # Delay further processing for 5 seconds
            time.sleep(5)
    return True

while True:
    # Get the list of files in the current directory
    try:
        files = os.listdir(os.getcwd())

        # Check the extensions of all the files
        for file in files:
            check_extension(file)

    except:
        print("that was an error")