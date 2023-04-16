import os
from PIL import Image

img_path = 'C:/Users/chest/OneDrive/project 2/river_train/data_dataset_voc/SegmentationClassPNG-new'
img_path_new = img_path + '-new2' 
if not os.path.isdir(img_path_new):
    os.mkdir(img_path_new)
img_list = sorted(os.listdir(img_path))

x = 0
y = 0
pix_set = set()


for image in img_list:
	img_name = str(image)
	img = Image.open(os.path.join(img_path,image))
	img_weight = img.size[0]
	img_hight = img.size[1]
	w_range = range(img_weight)
	h_range = range(img_hight)
	for x in w_range:
		for y in h_range:
			pix = img.getpixel((x,y))
			pix_set.add(pix)
			if pix == 0: # background
				pass #pix = img.putpixel((x,y),0)
			elif pix > 0 :	
                                pix = img.putpixel((x,y),255)

	img_new = os.path.join(img_path_new, img_name)
	img.save(img_new)
	print (image + " pixel values changed and saved to " + img_name)


