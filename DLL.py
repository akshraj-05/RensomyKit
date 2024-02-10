import psutil
import os
import sys
import tkinter as tk
from tkinter import messagebox
import time

UPDATED_FILE = "updatedFile.txt"

def get_process_dlls(process):
    try:
        dlls = process.memory_maps()
        return [dll.path for dll in dlls if dll.path.endswith(".dll")]
    except:
        return []

def is_process_known(process):
    with open(UPDATED_FILE, "r") as f:
        return process.name() in f.read().splitlines()

def add_process_to_file(process):
    with open(UPDATED_FILE, "a") as f:
        f.write(process.name() + "\n")

def alert(process):
    choice = messagebox.askyesno(title=f"Unknown DLL for process '{process.name()}'", 
                                 message=f"Process '{process.name()}' is using an unknown DLL and may be malicious.\nDo you want to add this process to the safe list?", 
                                 icon=messagebox.WARNING)
    if choice:
        add_process_to_file(process)
    else:
        process.kill()

def main():
    if not os.path.exists(UPDATED_FILE):
        open(UPDATED_FILE, "w").close()
    try:
        while True:
            for process in psutil.process_iter():
                if not is_process_known(process):
                    dlls = get_process_dlls(process)
                    if dlls:
                        alert(process)
    except: 
        print("an Exception ouccered")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    main()
