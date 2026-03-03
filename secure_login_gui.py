import tkinter as tk
from tkinter import messagebox
import winsound

# -------------------------
# Configuration
# -------------------------
correct_username = "admin"
correct_password = "1234"
failed_attempts = 0
locked = False

# -------------------------
# Functions
# -------------------------
def login():
    global failed_attempts, locked

    if locked:
        messagebox.showwarning("Account Locked", "⛔ Account is temporarily locked!")
        return

    username = entry_username.get()
    password = entry_password.get()

    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Success", "✅ Login Successful!")
        failed_attempts = 0
        attempts_label.config(text=f"Failed Attempts: {failed_attempts}")
    else:
        failed_attempts += 1
        attempts_label.config(text=f"Failed Attempts: {failed_attempts}")
        messagebox.showerror("Login Failed", "❌ Incorrect Username or Password")

        # Log failed attempt
        with open("security_log.txt", "a") as f:
            f.write(f"Failed login attempt {failed_attempts}\n")

    if failed_attempts >= 5:
        trigger_lock()

def trigger_lock():
    global locked, failed_attempts
    locked = True
    winsound.Beep(1000, 700)
    messagebox.showwarning(
        "Security Alert",
        "⚠️ Possible Brute Force Attack Detected!\nAccount locked for 10 seconds."
    )
    window.after(10000, unlock_account)  # Unlock after 10 seconds

def unlock_account():
    global locked, failed_attempts
    locked = False
    failed_attempts = 0
    attempts_label.config(text=f"Failed Attempts: {failed_attempts}")
    messagebox.showinfo("Unlocked", "✅ Account unlocked. You may try again.")

# -------------------------
# GUI Setup
# -------------------------
window = tk.Tk()
window.title("Secure Login System")
window.geometry("350x250")

tk.Label(window, text="Username").pack(pady=(20, 5))
entry_username = tk.Entry(window)
entry_username.pack()

tk.Label(window, text="Password").pack(pady=(10, 5))
entry_password = tk.Entry(window, show="*")
entry_password.pack()

tk.Button(window, text="Login", command=login).pack(pady=15)

attempts_label = tk.Label(window, text=f"Failed Attempts: {failed_attempts}")
attempts_label.pack()

window.mainloop()