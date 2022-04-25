import pytesseract
from PIL import Image

image = Image.open('test01.jpg')
image = image.point(lambda x: 0 if x < 143 else 255)
image.save('test01new.jpg')
imagenew = Image.open('test01new.jpg')
text = pytesseract.image_to_string(imagenew)
print(text)