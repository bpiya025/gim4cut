import tkinter as tk
from tkinter import messagebox
import cv2
import os

class PhotoBoothApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Booth App")
        self.master.geometry("400x300")

        self.home_button = tk.Button(self.master, text="Home", command=self.show_start_screen)
        self.home_button.pack(side=tk.BOTTOM)

        self.start_button = tk.Button(self.master, text="Start", command=self.show_photo_screen)
        self.start_button.pack()

    def show_start_screen(self):
        self.clear_screen()
        self.start_button.pack()

    def show_photo_screen(self):
        self.clear_screen()

        # Capture photos
        for i in range(4):
            self.capture_photo(i+1)

        messagebox.showinfo("Success", "Photos captured successfully!")

        # Upload photos to HTML
        self.upload_photos_to_html()

    def capture_photo(self, index):
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            messagebox.showerror("Error", "Unable to access the webcam!")
            return

        ret, frame = cap.read()
        if ret:
            filename = f"img{index}.jpg"
            cv2.imwrite(filename, frame)

        cap.release()

    def upload_photos_to_html(self):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Photo Booth</title>
        </head>
        <body>
            <h1>Photos Taken</h1>
            <div class="photos">
                <img src="img1.jpg" alt="Photo 1" width="200" height="150">
                <img src="img2.jpg" alt="Photo 2" width="200" height="150">
                <img src="img3.jpg" alt="Photo 3" width="200" height="150">
                <img src="img4.jpg" alt="Photo 4" width="200" height="150">
            </div>
        </body>
        </html>
        """

        with open("photos.html", "w") as f:
            f.write(html_content)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()

def main():
    root = tk.Tk()
    app = PhotoBoothApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
