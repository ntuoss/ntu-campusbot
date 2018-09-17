import os
from io import BytesIO
from scipy import misc
from urllib import request
import time
import datetime


CAM_BASE_IMAGE_URL = "https://webcam.ntu.edu.sg/upload/slider/"
LOCATIONS = {
    "Administration Cluster, Fastfood level": "fastfood",
    "Administration Cluster, Foodcourt": "foodcourt",
    "Lee Wee Nam Library": "lwn-inside",
    "Quad": "quad",
    "Onestop@SAC": "onestop_sac",
    "Walkway between North and South Spines": "WalkwaybetweenNorthAndSouthSpines",
    }

if not os.path.exists('cam_images'):
    os.mkdir('cam_images')
for location in LOCATIONS.values():
    if not os.path.exists(os.path.join('cam_images', location)):
        os.mkdir(os.path.join('cam_images', location))

datetime.datetime.now()

for i in range(30):
    print('{}: {}'.format(i, str(datetime.datetime.now()).split('.')[0]))
    for location in LOCATIONS.values():
        image_url = CAM_BASE_IMAGE_URL + location + ".jpg"
        request.urlretrieve(image_url, os.path.join('cam_images', location, (str(datetime.datetime.now()) + ".jpg").replace(' ', '-').replace(':', '-').split('.')[0]) + '.jpg')

    time.sleep(30)
