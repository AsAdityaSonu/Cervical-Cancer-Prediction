# Use this program to get details of the images in the directory
# --------------------------------------------------------------
DIR = './2-gb'
classes = ['class 1', 'Class 2', 'Class 3', 'Class 4']
image_ext = {".jpg"}
# --------------------------------------------------------------
import os
from PIL import Image

# --------------------------------------------------------------
# Directory info and img count
for c in classes:
    classDir = os.path.join(DIR, c)
    if os.path.exists(classDir):
        image_files = [f for f in os.listdir(classDir) if (os.path.splitext(f)[1].lower() in image_ext)]
        print(f"Number of images in class '{c}': {len(image_files)}")
    else:
        print(f"Directory does not exist: {classDir}")

# --------------------------------------------------------------
# Image size
# Image size
for c in classes:
    classDir = os.path.join(DIR, c)
    if os.path.exists(classDir):
        image_files = [f for f in os.listdir(classDir) if (os.path.splitext(f)[1].lower() in image_ext)]
        for image_file in image_files:
            with Image.open(os.path.join(classDir, image_file)) as img:
                width, height = img.size
                print(f"Size of image '{image_file}' in class '{c}': {width}x{height}")
    else:
        print(f"Directory does not exist: {classDir}")
