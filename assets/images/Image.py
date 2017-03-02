from PIL import Image
import sys
import os


size = 374, 260
im = Image.open(sys.argv[1])
im_res = im.resize(size,Image.ANTIALIAS)
os.rename(sys.argv[1], "Orig_" + sys.argv[1])
im_res.save(sys.argv[1], "JPEG")
