import glob
from PIL import Image
import os

# filepaths
fp_in = "../gen_like_quentin/pngs/*"
fp_out = "../gen_like_quentin/gifs/test1.gif"

files = glob.glob(fp_in)
files.sort(key=os.path.getmtime)
img, *imgs = [Image.open(f) for f in files]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)