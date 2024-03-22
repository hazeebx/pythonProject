import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weld Defect Prediction")
        self.geometry("800x800")

        # Prevent the window from being resized
        self.resizable(width=True, height=False)

        # Adding a button
        upload_button = tk.Button(self, text="Upload Weld Image", command=self.upload_image)
        upload_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

        # Placeholder for the uploaded image
        self.image_label = tk.Label(self)
        self.image_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        # Weld Parameters
        weld_params_label = tk.Label(self, text="Weld Parameters", font=("Helvetica", 16))
        weld_params_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        # Parameter Inputs
        self.parameters = ["Current", "Length of Arc", "Angle", "Manipulation", "Speed"]
        self.parameter_entries = {}
        for i, parameter in enumerate(self.parameters):
            label = tk.Label(self, text=parameter + ":")
            label.grid(row=i+3, column=0, pady=5, padx=10, sticky="w")
            entry = tk.Entry(self)
            entry.grid(row=i+3, column=1, pady=5, padx=10, sticky="ew")
            self.parameter_entries[parameter] = entry

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=self.submit_parameters)
        submit_button.grid(row=len(self.parameters) + 4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Output Area
        output_frame = tk.Frame(self, bd=2, relief=tk.GROOVE)
        output_frame.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="news")
        output_label = tk.Label(output_frame, text="Weld Evaluation", font=("Helvetica", 14))
        output_label.pack(pady=5)
        self.output_text = tk.Text(output_frame, height=5, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Graph Area
        graph_frame = tk.Frame(self, bd=2, relief=tk.GROOVE)
        graph_frame.grid(row=0, column=2, rowspan=9, pady=10, padx=10, sticky="news")
        self.figure, self.ax = plt.subplots()
        self.graph_canvas = FigureCanvasTkAgg(self.figure, master=graph_frame)
        self.graph_canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.graph_canvas.draw()

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


    def submit_parameters(self):
        # Get the parameter values
        parameter_values = self.get_parameter_values()

        # Example: Print the parameter values to the console
        print("Parameter values:", parameter_values)

        # Example: Plot parameter values on the graph
        x_values = list(parameter_values.keys())
        y_values = [float(value) for value in parameter_values.values()]

        self.ax.clear()
        self.ax.bar(x_values, y_values)
        self.ax.set_xlabel('Parameters')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Parameter Values')
        self.graph_canvas.draw()
    def get_parameter_values(self):
        parameter_values = {}
        for parameter, entry in self.parameter_entries.items():
            parameter_values[parameter] = entry.get()
        return parameter_values

if __name__ == "__main__":
    app = App()
    app.mainloop()
