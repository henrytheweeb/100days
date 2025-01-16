import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image handling
import turtle

def custom_messagebox(message, title="Custom Message", icon_path="snake.png"):
    # Create a new window for the custom message box
    custom_box = tk.Toplevel()  # Custom pop-up window
    custom_box.title(title)
    
    # Set the window size and prevent resizing
    custom_box.geometry("300x150")
    custom_box.resizable(False, False)
    
    # Load and resize the custom icon (image file)
    try:
        image = Image.open(icon_path)  # Open the image using Pillow
        image = image.resize((50, 50))  # Resize the image to 50x50 pixels (adjust as needed)
        icon_image = ImageTk.PhotoImage(image)  # Convert to a PhotoImage object
    except Exception as e:
        print("Error loading or resizing image:", e)
        icon_image = None  # Default to None if loading or resizing fail
    
    # Display the icon in the messagebox
    if icon_image:
        icon_label = tk.Label(custom_box, image=icon_image)
        icon_label.image = icon_image  # Keep a reference to the image
        icon_label.grid(row=0, column=0, padx=10, pady=10)
    
    # Display the message text
    message_label = tk.Label(custom_box, text=message, font=("Arial", 12))
    message_label.grid(row=0, column=1, padx=10, pady=10)
    
    # Add an "OK" button to close the pop-up
    ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy)
    ok_button.grid(row=1, column=1, padx=10, pady=10)
    
    custom_box.wait_window()
