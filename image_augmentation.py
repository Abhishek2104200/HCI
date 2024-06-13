#MODULE-4-Image Augmentation Module (image_augmentation.py):
#Contains functions for image augmentation.
#image_augmentation.py
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
