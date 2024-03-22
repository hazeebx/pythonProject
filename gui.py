import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weld Defect Prediction")
        self.geometry("800x800")

        # Adding a button
        upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

        # Placeholder for the uploaded image
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)
        # Prevent the window from being resized
        self.resizable(width=False, height=False)

        # Weld Parameters
        tk.Label(self, text="Weld Parameters", font=("Helvetica", 16)).pack(pady=5)

        # Parameter Inputs
        self.parameters = ["Current", "Length of Arc", "Angle", "Manipulation", "Speed"]
        self.parameter_entries = {}
        for parameter in self.parameters:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=parameter + ":")
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT)
            self.parameter_entries[parameter] = entry
        # Output Area
        output_frame = tk.Frame(self, bd=2, relief=tk.GROOVE)
        output_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        tk.Label(output_frame, text="Weld Evaluation", font=("Helvetica", 14), pady=5).pack()
        self.output_text = tk.Text(output_frame, height=5, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)
    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            print(f"Selected file: {file_path}")
            self.display_image(file_path)

    def display_image(self, file_path):
        # Open the image using PIL
        image = Image.open(file_path)

        # Resize the image to fit the label
        image = image.resize((300, 300), Image.LANCZOS)

        # Convert the PIL Image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    app = App()
    app.mainloop()
