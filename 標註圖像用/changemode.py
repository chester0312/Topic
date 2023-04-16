import os
from PIL import Image

img_path = 'C:/Users/chest/OneDrive/project 2/river_train/data_dataset_voc/SegmentationClassPNG-new'
img_path_new = img_path + '-new' 
if not os.path.isdir(img_path_new):
    os.mkdir(img_path_new)
img_list = sorted(os.listdir(img_path))

for image in img_list:
    img_name = str(image)
    img0 = Image.open(os.path.join(img_path,image))
    img = img0.convert('L')
    path_img = os.path.join(img_path_new, img_name)
    img.save(path_img)
    print (image + " pixel values changed and saved to " + img_name)


