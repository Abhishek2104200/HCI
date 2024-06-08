MODULE 3-Image Module (image.py):
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
