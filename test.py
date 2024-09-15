import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Text

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, text)

root = tk.Tk()
root.title("Tesseract")

open_button = tk.Button(root, text="open image", padx=10, pady=5, command=open_image)
open_button.pack()

result_text = Text(root, wrap=tk.WORD, padx=10, pady=5)
result_text.pack()

root.mainloop()