from rembg import remove
from PIL import Image

input_path='input/ucen.jpg'
output_path='output/newucen.png'

input=Image.open(input_path)
output=remove(input)
output.save(output_path)