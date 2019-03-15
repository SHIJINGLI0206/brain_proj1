from __future__ import absolute_import

import cv2

img = cv2.imread('test.jpg')
cv2.imshow("test.jpg",img)
cv2.waitKey()