
import pytesseract, cv2
from PIL import Image
import sys, io
from PIL import Image



sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
image = Image.open('image.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

width, height = image.size
upper_half = image.crop((0, 0, width, height // 2))
lower_half = image.crop((0, height // 2, width, height))
up = pytesseract.image_to_string(upper_half, lang = "deu")
down  = pytesseract.image_to_string(lower_half, lang = "deu")
file  = pytesseract.image_to_string(image, lang = "deu")
with open('output.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(file)

with open('output2.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(down)




# for page_num, page in enumerate(doc):
#     pix = page.get_pixmap()
#     img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
#     # Speichern des Bildes zur Diagnose
#     pytesseract.pytesseract.tesseract_cmd
#     img.save(f"page_{page_num + 1}.png")  # Speichert das Bild als PNG
    
#     text = pytesseract.image_to_string(img)  # OCR auf das Bild anwenden
#     with open("output.txt", "a") as out:
#         out.write(text)
#         out.write("\n")  # Neue Zeile nach jeder Seite