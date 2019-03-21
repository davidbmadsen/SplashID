import cv2
import numpy as np
import os

def split(path, frameskip):
    video = cv2.VideoCapture(path)

    try:
        if not os.path.exists('testframes'):
            os.makedirs('testframes')
    except OSError:
        print('Error: Creating directory of data')

    current_frame = 0
    while(True):

        ret, frame = video.read()
        if ret == False:
            break

        print(ret)
        name = './video/testframes/' + str(current_frame) + '.jpg'
        cv2.imwrite(name, frame)

        current_frame += frameskip
