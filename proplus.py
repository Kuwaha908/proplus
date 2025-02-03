import os
import platform
import subprocess

class ProPlus:
    def __init__(self):
        self.system_info = self.get_system_info()

    def get_system_info(self):
        return {
            "platform": platform.system(),
            "release": platform.release(),
            "version": platform.version()
        }

    def validate_windows(self):
        if self.system_info["platform"] != "Windows":
            print("ProPlus is designed for Windows platforms only.")
            return False
        return True

    def guide_user(self):
        if not self.validate_windows():
            return

        print("Welcome to ProPlus: System Recovery Guide")
        print("Step 1: Create a System Restore Point (Recommended)")
        self.create_restore_point()
        
        print("Step 2: Run System File Checker (SFC)")
        self.run_sfc()

        print("Step 3: Run Check Disk Utility (CHKDSK)")
        self.run_chkdsk()

        print("Step 4: Optional - Reset Windows")
        print("Use this step if the previous steps did not resolve the issue.")

    def create_restore_point(self):
        try:
            import win32com.client
            objWMI = win32com.client.GetObject("winmgmts:\\\\.\\root\\default:SystemRestore")
            result = objWMI.CreateRestorePoint("ProPlus Restore Point", 0, 100)
            if result == 0:
                print("System Restore Point created successfully.")
            else:
                print("Failed to create System Restore Point.")
        except ImportError:
            print("pywin32 module is required to create a restore point.")
        except Exception as e:
            print(f"Error creating restore point: {e}")

    def run_sfc(self):
        try:
            print("Running System File Checker...")
            subprocess.run("sfc /scannow", check=True, shell=True)
            print("System File Checker completed.")
        except subprocess.CalledProcessError:
            print("An error occurred while running System File Checker.")

    def run_chkdsk(self):
        try:
            print("Running Check Disk Utility...")
            subprocess.run("chkdsk /f /r", check=True, shell=True)
            print("Check Disk Utility completed.")
        except subprocess.CalledProcessError:
            print("An error occurred while running Check Disk Utility.")

if __name__ == "__main__":
    proplus = ProPlus()
    proplus.guide_user()