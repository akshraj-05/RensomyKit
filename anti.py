import winreg
import subprocess
import tkinter as tk
from tkinter import messagebox

def get_uac_setting():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
        value, type = winreg.QueryValueEx(key, "ConsentPromptBehaviorAdmin")
        winreg.CloseKey(key)
        return value
    except WindowsError:
        return None

def get_password_policy():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Lsa")
        password_complexity, type = winreg.QueryValueEx(key, "PasswordComplexity")
        password_history, type = winreg.QueryValueEx(key, "PasswordHistory")
        min_password_age, type = winreg.QueryValueEx(key, "MinPasswordAge")
        max_password_age, type = winreg.QueryValueEx(key, "MaxPasswordAge")
        winreg.CloseKey(key)
        return password_complexity, password_history, min_password_age, max_password_age
    except WindowsError:
        return None

# def get_defender_status():
#     result = subprocess.run(['powershell.exe', 'Get-MpComputerStatus'], stdout=subprocess.PIPE)
#     output = result.stdout.decode('utf-8')
#     lines = output.splitlines()
#     defender_enabled = None
#     real_time_protection_enabled = None
#     for line in lines:
#         if "DefenderEnabled" in line:
#             defender_enabled = line.split(':')[-1].strip()
#         if "RealTimeProtectionEnabled" in line:
#             real_time_protection_enabled = line.split(':')[-1].strip()
#     return defender_enabled, real_time_protection_enabled

uac_setting = get_uac_setting()
if uac_setting is not None:
    print("User Account Control (UAC) setting:", uac_setting)
else:
    print("User Account Control (UAC) setting not found.")

password_policy = get_password_policy()
if password_policy is not None:
    print("Password policy:", password_policy)
else:
    print("Password policy not found.")

# defender_status = get_defender_status()
# if defender_status is not None:
#     print("Microsoft Defender status:", defender_status)
#     # if defender_status in (None, 'False'):
#     #     messagebox.showerror("Microsoft Defender Error", "Microsoft Defender is not enabled.")
# else:
#     print("Microsoft Defender status not found.")

def check_defender_status():
    result = subprocess.run(['powershell.exe', 'Get-MpComputerStatus'], capture_output=True, text=True)
    WindowsDStatus = result.stdout
    AVStatus = "Anti Virus Enabled: " + WindowsDStatus.split("AntivirusEnabled")[1].split("\n")[0].strip()
    print(AVStatus)
    RealTimeProtection = "Real-Time Protection Enabled: " + WindowsDStatus.split("RealTimeProtectionEnabled")[1].split("\n")[0].strip()
    if "True" in RealTimeProtection:
        print("Real-Time Protection: Enabled")
    else:
        print("Real-Time Protection: Disabled")
        messagebox.showerror("Microsoft Defender Error", "Microsoft Defender is not enabled.")

check_defender_status()
