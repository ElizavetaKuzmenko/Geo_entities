from images2gif import writeGif
from PIL import Image
import os

PATH_MAPS = '/home/boris/Work/poetic/geo/maps_countries'

def gf_make():
    file_names = []
    for flnm in sorted(os.listdir(PATH_MAPS)):
        if not flnm.endswith('.png'):
            continue
        elif 'sm_' not in flnm:
            continue
        elif flnm == '0.png':
            continue
        elif int(flnm.replace('sm_', '').replace('.png', '')) > 1940:
            continue
        elif flnm == 'sm_0.png':
            continue
        else:
            file_names.append(flnm)
    images = [Image.open(PATH_MAPS + os.sep + fn) for fn in file_names]
    writeGif(PATH_MAPS + '/anim_countries_slow.gif', images, duration=1.7, repeat=True, dither=False)
    
def main():
    gf_make()
    return 0

if __name__ == '__main__':
	main()