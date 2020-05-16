import sys
import os
from PIL import Image

# Grab the first and Second Args
image_folder = sys.argv[1]
newPath = sys.argv[2]

if not os.path.exists(newPath):
    os.mkdir(newPath)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{newPath}{clean_name}.png", "png")
    print("All Done..!")
