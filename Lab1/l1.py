#Lab 1 - Applying 4 convolution filters

from PIL import Image
from PIL import ImageFilter

def main():

	im = Image.open("SuccessKidMeme.jpg")
	identity = [0,0,0,0,1,0,0,0,0]
	box_blur = [1,1,1,1,1,1,1,1,1]
	approx_gauss = [0.003,]

	result = im.filter(ImageFilter.Kernel((3,3), identity))
	result.show()

	result = im.filter(ImageFilter.Kernel((3,3), box_blur, 9))
	result.show()
	pass

if __name__ == '__main__':
	main()