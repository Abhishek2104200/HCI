#IMAGE AUGMENTATION Classified into modules

#MODULE 1-Main Module (main.py):
#Entry point of the application.
#initializes the main Tkinter window and login page.
# main.py
import tkinter as tk
from login_page import LoginPage
def main():
 root = tk.Tk()
 login_page = LoginPage(root)
 root.mainloop()

if __name__ == "__main__":
 main()

#MODULE 2-Login Page Module (login_page.py):
#Creates the login page UI.
#Handles login logic.
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


#MODULE 3-Image Module (image.py):
#Handles image loading and display
# image.py
from PIL import Image, ImageTk

def load_image(file_path):
 try:
 image = Image.open(file_path)
 return image
 except Exception as e:
print("Error loading image:", e)
 return None

def create_photo_image(image):
 photo_image = ImageTk.PhotoImage(image)
 return photo_image

