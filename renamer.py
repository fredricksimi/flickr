import os
for filename in os.listdir('/home/freddy/flickrphotos/2Faces/'):
    os.rename(f'/home/freddy/flickrphotos/2Faces/{filename}', f'/home/freddy/flickrphotos/2Faces/{filename[:-4]}.png')