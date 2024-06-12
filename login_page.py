#MODULE 2-Login Page Module:
#Creates the login page UI.
# login_page.py
import tkinter as tk
class LoginPage:
 def __init__(self, master):
 self.master = master
self.master.title("Login")
 # Create username label and entry
self.username_label = tk.Label(self.master, text="Username:")
self.username_label.pack()
self.username_entry = tk.Entry(self.master)
self.username_entry.pack()
 # Create password label and entry
self.password_label = tk.Label(self.master, text="Password:")
self.password_label.pack()
self.password_entry = tk.Entry(self.master, show="*") # Hide password characters
self.password_entry.pack()


 # Create login button
self.login_button = tk.Button(self.master, text="Login", command=self.handle_login)
self.login_button.pack()

 def handle_login(self):
 username = self.username_entry.get()
 password = self.password_entry.get()

 # Replace these with your actual authentication logic (e.g., database check)
 if username == "user" and password == "pass":
print("Login successful")
 else:
print("Invalid Login Credentials")
