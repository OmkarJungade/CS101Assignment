import cv2 as cv
import numpy as np

# MARKER 1
dictionary=cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)
markerImage=np.zeros((200,200),dtype=np.uint8)

for i in [33,50,78,99]:
    markerImage=cv.aruco.drawMarker(dictionary,i,300,markerImage,1)
    cv.imwrite(f'marker{i}.png',markerImage)
