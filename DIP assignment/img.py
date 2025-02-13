'''
import cv2
path = 'E:/pranav sirsufale/spidy.jpg'
img = cv2.imread('spidy.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


### Image compresson and storage
import cv2 
img = cv2.imread('spidy.jpg',1)
compressed_img_param = [cv2.IMWRITE_JPEG_QUALITY,50]
cv2.imwrite('compressed_sharp_img2.jpg',img,compressed_img_param)

import cv2
import numpy as np
img = cv2.imread('noicy.jpg',0)
denoised = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('original Image',img)
cv2.imshow('denoised iamge',denoised)
if( cv2.waitKey() == ord('q') ):
    cv2.destroyAllWindows()


import cv2
brigh_image = cv2.imread('fish.jpg')
darkening_factor = 50 
dark_image = cv2.subtract(brigh_image, darkening_factor)
dark_image = cv2.max(dark_image,0)

cv2.imshow('Original Image',brigh_image)
cv2.imshow('Dark Image', dark_image)
cv2.waitKey(0)
cv2.destroyAllwindows()

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
dark_img = cv2.imread('fish dark.jpg')
brightness_factor = 50 

bright_img = np.clip(dark_img + brightness_factor , 0 , 255).astype(np.uint8)

plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(dark_img,cv2.COLOR_BGR2RGB))
plt.title('Original Dark Image')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(bright_img, cv2.COLOR_BGR2RGB))
plt.title('Newly Brghted Image')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()



