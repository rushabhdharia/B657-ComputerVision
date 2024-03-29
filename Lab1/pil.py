#Pillow Library tutorial CV Class Spring 2019

#Import the Image and ImageFilter classes from PIL (Pillow)
from PIL import Image
from PIL import ImageFilter
import random

def main():
	#Load an image
	im = Image.open("example.jpg")

	#Check its width, height and number of color channels
	print("Image is %s pixels wide." % im.width)
	print("Image is %s pixels high." % im.height)
	print("Image mode is %s." % im.mode)

	#pixels are accessed via a (X,Y) tuple
	print("Pixel value is %s" % im.getpixel((10,10)))
	#pixels can be modified by specifying the coordinate and RGB value
	im.putpixel((10,10), 20)
	print("New pixel value is %s" % im.getpixel((10,10)))

	#Create a new blank color image the same size as the input
	color_im = Image.new("RGB", (im.width, im.height), color = 0)

	#Loops over the new color image and fills in any area that was white in the 
	#first grayscale image we loaded with random colors!

	for x in range(im.width):
		for y in range(im.height):
			if im.getpixel((x,y)) > 200:
				R = random.randint(0,255) 
				G = random.randint(0,255)
				B = random.randint(0,255)
				color_im.putpixel((x,y), (R,G,B))
			else:
				color_im.putpixel((x,y), (0,0,0))

	#Show the image
	color_im.show()

	#Save the image
	color_im.save("output.jpg")

	#Using  Pillow ’ s  code  to  create  a  convolution  kernel  and apply  it  to  our  color  image
	#Here ,  we are  applying  the  box  blur ,  where a  kernel  of  size  3x3  is  filled  with 1
	#and the  result  is  divided  by 9
	result = color_im.filter(ImageFilter.Kernel((3,3),[1,1,1,1,1,1,1,1,1],9))
	result.show()

	pass

if __name__ == '__main__':
	main()