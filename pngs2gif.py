import glob
from PIL import Image
import os

# filepaths
fp_in = "pngs/radom*"
fp_out = "gifs/radom2D.gif"

files = glob.glob(fp_in)
print(files)
files.sort(key=os.path.getmtime)
img, *imgs = [Image.open(f) for f in files]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)