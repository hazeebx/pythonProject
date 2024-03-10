import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weld Defect Prediction")
        self.geometry("400x300")

        # Adding a button
        upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

        # Placeholder for the uploaded image
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            print(f"Selected file: {file_path}")
            self.display_image(file_path)

    def display_image(self, file_path):
        # Open the image using PIL
        image = Image.open(file_path)

        # Resize the image to fit the label
        image = image.resize((300, 200), Image.ANTIALIAS)

        # Convert the PIL Image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    app = App()
    app.mainloop()
