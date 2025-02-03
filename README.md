```
# ProPlus

## Overview

ProPlus is a Python-based utility program designed to guide users through a step-by-step process for system recovery on Windows platforms. It provides a structured approach to troubleshoot and potentially fix common system issues.

## Features

- **System Restore Point Creation:** Provides an option to create a restore point before making any changes.
- **System File Checker (SFC):** Guides users to check for and repair corrupted system files.
- **Check Disk Utility (CHKDSK):** Helps users run disk checks to detect and fix disk errors.
- **Optional Windows Reset:** Suggests a Windows reset if previous steps do not resolve the issue.

## Requirements

- Windows Operating System
- Python 3.x
- `pywin32` module for creating system restore points

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/proplus.git
   ```

2. Navigate to the directory:
   ```bash
   cd proplus
   ```

3. Install the required Python module:
   ```bash
   pip install pywin32
   ```

## Usage

Run the `proplus.py` script using Python:

```bash
python proplus.py
```

Follow the on-screen instructions to guide you through the recovery process.

## Note

- ProPlus is specifically designed for Windows platforms. Running it on non-Windows systems will not work.
- Ensure you have administrative privileges while running the program as it requires access to system utilities.

## License

This project is licensed under the MIT License.