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


