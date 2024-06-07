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

#MODULE-4-Image Augmentation Module (image_augmentation.py):
#Contains functions for image augmentation.
# image_augmentation.py
import cv2
import numpy as np
def adjust_brightness(image, value):
 brightness_factor = float(value) / 100.0
 adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
 return adjusted_image
def adjust_contrast(image, value):
 contrast_factor = float(value) / 100.0
 adjusted_image = (image.astype(np.float32) / 255.0 - 0.5) * contrast_factor + 0.5
 adjusted_image = np.clip(adjusted_image, 0, 1)
 adjusted_image = (adjusted_image * 255).astype(np.uint8)
 return adjusted_image