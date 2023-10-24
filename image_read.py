
# Developer Name :- Ravi Kumawat
# Date :- 24-10-2023
# Code :- To read any image in our Pc


import cv2 # ================ import library

img_0 = cv2.imread('C:\\Users\\pc\\Pictures\\Screenshots\\Screenshot 2023-10-24 111121.png') # ======== this is a path from image for in your system

cv2.imshow('image',img_0) # ========================= this is only variable
cv2.waitKey(0) # ============== cv2.waitkey(0) open image and hold it

