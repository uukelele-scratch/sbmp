from PIL import Image
from io import BytesIO
import os
import random
import sys

def _rgb_to_number(rgb):
	r, g, b = rgb
	return r * 256**2 + g * 256 + b

def _convert_img(img, size):
	img_d = Image.open(img)
	img_d = img_d.convert('RGB')
	resized_img = img_d.resize((size, size))
	image_data = []
	for y in range(size):
		for x in range(size):
			rgb = resized_img.getpixel((x, y))[:3]
			image_data.append(_rgb_to_number(rgb))
	data = ""
	for pixel in image_data:
		data += f"{pixel} "
	return data
	
def jpg2sbmp(filename, size, out):
	image_data = _convert_img(filename, size)
	with open(out,'w') as file:
		file.write(f"{size}\n{str(image_data)}")
		
		
if len(sys.argv) < 3:
	print("Error: Expected 3 arguments [image filename, resolution, output filename]")
	sys.exit()
	
try:
	jpg2sbmp(sys.argv[1], int(sys.argv[2]), sys.argv[3])
except Exception as e:
	print(f"Error: {e}")
