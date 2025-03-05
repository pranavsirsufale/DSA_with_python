path = 'F:/DSA/practical/DIP assignment/sdfd/cam.jpg'
import cv2
'''
#### IMAGE AQUISITION AND REPRESENTATION
import cv2
path = 'F:/DSA/practical/DIP assignment/sdfd/cam.jpg'
img = cv2.imread(path)
cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()





#### IMAGE COMPRESSION AND STORAGE 
import cv2
img = cv2.imread('F:/DSA/practical/DIP assignment/sdfd/cam.jpg',1)
compressed_img_param = [cv2.IMWRITE_JPEG_QUALITY,50]
cv2.imwrite('F:/DSA/practical/DIP assignment/sdfd/image_name_of_compressed_image.jpg',img,compressed_img_param)

'''


import numpy as np
img = cv2.imread(path,0)
denoised = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('original Image ' , img)
cv2.imshow('denoised image ',denoised)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()
