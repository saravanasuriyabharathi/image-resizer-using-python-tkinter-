import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, StringVar
from PIL import Image, ImageTk

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Load the background image and resize it to fit the window
        self.bg_image = Image.open("background.jpeg")  # Use your background image path
        self.bg_image = self.bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label with the background image
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)  # Make it fill the window

        # Title
        self.title_label = Label(self.root, text="Image Resizer", font=("Arial", 24, "bold"), fg="black", bg="#d9ead3")
        self.title_label.pack(pady=20)

        # Directory Selection
        self.dir_label = Label(self.root, text="Select Image File:", font=("Arial", 12), bg="#d9ead3")
        self.dir_label.place(x=50, y=80)
        self.dir_path = StringVar()
        self.dir_entry = Entry(self.root, textvariable=self.dir_path, font=("Arial", 12), width=40)
        self.dir_entry.place(x=180, y=80)
        self.browse_button = Button(self.root, text="Browse", font=("Arial", 10), bg="#6aa84f", fg="white", command=self.browse_file)
        self.browse_button.place(x=500, y=78)

        # Resize Width and Height Inputs
        self.width_label = Label(self.root, text="Width:", font=("Arial", 12), bg="#d9ead3")
        self.width_label.place(x=50, y=130)
        self.width_entry = Entry(self.root, font=("Arial", 12), width=10)
        self.width_entry.place(x=120, y=130)

        self.height_label = Label(self.root, text="Height:", font=("Arial", 12), bg="#d9ead3")
        self.height_label.place(x=250, y=130)
        self.height_entry = Entry(self.root, font=("Arial", 12), width=10)
        self.height_entry.place(x=320, y=130)

        # Resize Button
        self.resize_button = Button(self.root, text="Resize Images", font=("Arial", 14), bg="#38761d", fg="white", command=self.resize_images)
        self.resize_button.place(x=220, y=180)

        # Footer
        self.footer_label = Label(self.root, text="Created with Pillow Library", font=("Arial", 10), bg="#d9ead3", fg="#6d9eab")
        self.footer_label.pack(side="bottom", pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.dir_path.set(file_path)

    def resize_images(self):
        file_path = self.dir_path.get()
        width = self.width_entry.get()
        height = self.height_entry.get()

        # Validation
        if not file_path:
            messagebox.showerror("Error", "Please select an image file!")
            return
        if not width.isdigit() or not height.isdigit():
            messagebox.showerror("Error", "Width and Height must be positive integers!")
            return

        width, height = int(width), int(height)
        output_dir = os.path.dirname(file_path)  # Save resized images in the same folder
        os.makedirs(output_dir, exist_ok=True)

        try:
            with Image.open(file_path) as img:
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                # Save the resized image with a modified name
                resized_img.save(os.path.join(output_dir, f"resized_{os.path.basename(file_path)}"))
                messagebox.showinfo("Success", f"Image resized and saved at {output_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to resize image: {e}")

# Run the application
if __name__ == "__main__":
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()
