from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = Translator()

text = ""
ans = input("Do you want translated to persian?(Y/N): ")

for path in pathlib.Path("fa_picture").iterdir():
    if path.is_file():
        pic = path
        text += pytesseract.image_to_string(Image.open(pic), lang="fas")
        text += 50 * "-" + "\n"

for path in pathlib.Path("en_picture").iterdir():
    if path.is_file():
        pic = path
        en = pytesseract.image_to_string(Image.open(pic), lang="eng")
        if "y" in ans.lower():
            txt = str(translator.translate(en, src="en", dest="fa"))
            start_index = txt.find("text=")
            end_index = txt.find(",", start_index)
            text += txt[start_index + len("text="):end_index].strip() + "\n"
        else:
            text += en
        text += 50 * "-" + "\n"

with open("text.txt", "w", encoding="utf8") as f:
    f.write(text)

