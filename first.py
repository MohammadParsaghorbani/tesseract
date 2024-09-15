import pytesseract
from PIL import Image
while True:
    try:
        choice = int(input("option:\n\t1) png\n\t2) jpg\n\t3) exit\n"))
        if choice == 1:
            try:
                option = input("enter the file name: ")
                img = Image.open(f"{option}.png")
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                result = pytesseract.image_to_string(img,lang="eng")
                print(result)
            except FileNotFoundError:
                print("file not found!")
        elif choice == 2:
            try:
                option = input("enter the file name: ")
                img = Image.open(f"{option}.jpg")
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                result = pytesseract.image_to_string(img,lang="eng")
                print(result)
            except FileNotFoundError:
                print("file not found!")
        elif choice == 3:
            print("goodbye!")
            break
        else:
            print("wrong option")
    except ValueError:
        print("you should enter a number!")