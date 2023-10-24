
# Developer Name :- Ravi Kumawat
# Date :- 24-10-2023
# Code :- To read any image in our Pc

import os
import cv2 # ================ import library

paths = os.listdir(r'C:\Users\pc\PycharmProjects\pythonProject\rv_saveimg')
for path in paths:

    img_0 = cv2.imread(fr'C:\Users\pc\PycharmProjects\pythonProject\rv_saveimg\{path}') # ======== this is a path from image for in your system

    cv2.imshow('image',img_0) # ========================= this is only variable
    cv2.waitKey(0) # ============== cv2.waitkey(0) open image and hold it

