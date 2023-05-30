import pytesseract

from PIL import Image

pic = Image.open('captcha.jpg')
text = pytesseract.image_to_string(pic,'eng')
print(text)