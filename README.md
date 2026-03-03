![Secure Login GUI](secure_login.png)
# Secure Login GUI with Brute-Force Detection

## Description
A Python Tkinter GUI login system that:
- Tracks failed login attempts
- Locks account after 5 failed attempts
- Logs failed attempts to `security_log.txt`
- Emits a beep sound on security alert

## Tech Stack
- Python
- Tkinter (GUI)
- Winsound (alerts)
- PyInstaller (for creating .exe)

## How to Run
### Option 1: Using Python
```bash
python secure_login_gui.py

## Screenshots
![Login Screen](screenshots/login_screen.png.png)
![Failed Login](screenshots/failed_login.png.png)
![Lock Alert](screenshots/BruteFroce_attack detected.png.png)
![account lock](screenshots/Account_lock.png.png)
![account unlock](screenshots/Account_unlock.png.png)
![logi sucessfull](screenshots/login_sucessfull.png.png)
