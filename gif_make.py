from images2gif import writeGif
from PIL import Image
import os

dirpath = '../geo/maps_italy/cities_decades_log/'
result_path = '../animated_maps/'

def gif_assemble(root, file_names_raw):
    file_names = []
    for flnm in sorted(file_names_raw):
        if not flnm.endswith('.png'):
            continue
        elif flnm == '0.png':
            continue
        elif int(flnm.replace('.png', '')) > 1940:
            continue
        else:
            file_names.append(flnm)
    if len(file_names) == 0:
        return 0
    images = [Image.open(root + os.sep + fn) for fn in file_names]
    begin_path, end_path = root.spit('maps_')
    filename = end_path.replace('/', '_')
    filename += '.gif'
    writeGif(result_path + filename, images, duration=0.9, repeat=True, dither=False)

for root, dirs, files in os.walk('../'):
    if 'maps_' in root:
        if 'countries' in root:
            continue
        if 'centuries' in root:
            continue
        if 'cities_all_abs.png' in files:
            continue
        gif_assemble(root, files)    