from cv2 import imread, imwrite
import os

input_dir = 'C:/Users/Matthias/Downloads/Gwent with Bleeding/'

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')

def generate(input_dir=input_dir):
    for in_dirname, subdirnames, fnames in os.walk(input_dir):
        for subdir in subdirnames:
            in_path = os.path.join(in_dirname, subdir)
            out_path = in_path.replace('Gwent with Bleeding', 'Gwent')
            os.mkdir(out_path)
        for fname in fnames:
            if fname.lower().endswith(IMAGE_EXTENSIONS):
                in_path = os.path.join(in_dirname, fname)
                img = imread(in_path)
                out_path = in_path.replace('Gwent with Bleeding', 'Gwent')
		print(in_path + ' > ' + out_path)
                imwrite(out_path, crop(img))
				
def crop(img):
	return img[36:1121-37,36:746-36]