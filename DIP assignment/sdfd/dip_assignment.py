path = 'F:/DSA/practical/DIP assignment/sdfd/cam.jpg'
import cv2
import numpy as np
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



# DENOISE IMAGE 
import numpy as np
img = cv2.imread(path,0)
denoised = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('noisy Image ' , img)
cv2.imshow('denoised image ',denoised)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()


#### CONVERT BRIGHT IMAGE INTO DARK IMAGE
bright_img = cv2.imread('F:/DSA/practical/DIP assignment/sdfd/cam.jpg')
darkening_factor = 50
dark_img = cv2.subtract(bright_img, darkening_factor)
dark_img = cv2.max(dark_img,0)

cv2.imshow("ORIGINAL IMAGE", bright_img)
cv2.imshow('DARK IMAGE ', dark_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

## cONVERT DARK IMAGE INTO BRIGHT IMAGE
import matplotlib.pyplot as plt

dark_img = cv2.imread(path)
brightening_factor = 50
bright_img = np.clip(dark_img + brightening_factor , 0 , 255).astype(np.uint8)
plt.figure(figsize = (10, 6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(dark_img, cv2.COLOR_BGR2RGB))
plt.title('dark image ')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(dark_img,cv2.COLOR_BGR2RGB))
plt.title('brightend image')

plt.tight_layout()
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()





           


















