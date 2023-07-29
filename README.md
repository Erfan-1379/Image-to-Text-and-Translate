

# Image-to-Text-and-Translate

This project is an application that can convert your images to text and translate them if needed. This application supports Persian and English languages.

## Installation and Setup

To run this project, you need to install the following software:

- Python 3.8 or higher
- Tesseract-OCR
- PIL
- pytesseract
- googletrans

After installing the software, you need to set up your virtual environment. To do this, enter the following commands in the terminal:


python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Then, you need to enter the path of tesseract.exe in the main.py file. For example:


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


Now you can run the project with the following command:


python main.py


## Usage

To use this project, you need to place your images in the fa_picture and en_picture folders. The fa_picture folder is for Persian images and the en_picture folder is for English images.

After running the project, the program will ask you if you want to translate the English images to Persian or not. You can answer with Y or N.

The program will convert your images to text and translate them if needed. The text output will be saved in the text.txt file.

## Dependencies

This project uses the following software, libraries, and resources:

- [Python](https://www.python.org/)
- [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/)
- [PIL](https://pillow.readthedocs.io/en/stable/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [googletrans](https://pypi.org/project/googletrans/)
- [tessdata](https://github.com/tesseract-ocr/tessdata)

## Contact Me

For feedback and support, you can contact me by email:

yaghoblo41@gmail.com

You can also follow my GitHub profile:

https://github.com/Erfan-1379
