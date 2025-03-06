path = 'F:/DSA/practical/DIP assignment/sdfd/cam.jpg'
fish = 'F:/DSA/practical/DIP assignment/sdfd/fish dark.jpg'
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


## cONVERT DARK IMAGE INTO BRIGHT IMAGE
import matplotlib.pyplot as plt

dark_img = cv2.imread(fish)
brightening_factor = 50
bright_img = np.clip(dark_img + brightening_factor , 0 , 255).astype(np.uint8)
plt.figure(figsize = (10, 6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(dark_img, cv2.COLOR_BGR2RGB))
plt.title('dark image ')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(bright_img,cv2.COLOR_BGR2RGB))
plt.title('Newly Brighted image')

plt.tight_layout()
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()


## TAKE AN IMAGE AND APPLY GAUSSIAN BLUR FILTER ON IT TO SHARP THE IAMGE .
img = cv2.imread(path)
output_gaussian = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Gaussian Blur', output_gaussian)
cv2.imshow('original Img ', img)
cv2.waitKey(0)


img = cv2.imread(path)
output_median_blur = cv2.medianBlur(img,5)

cv2.imshow('median blured image ', output_median_blur)
cv2.imshow('Original image ', img)
cv2.waitKey(0)


img = cv2.imread(path)
output_bilateral = cv2.bilateralFilter(img,5,6,6)
cv2.imshow('bilateral fiber',output_bilateral)

## ORIGINAL IMAGE
cv2.imshow('original image ', img)
cv2.waitKey(0)


import matplotlib.pyplot as plt
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_sobely = cv2.Sobel(img,-1,0,1)

fig,axis = plt.subplots(2,3,figsize=(10,5))

axis[0,0].imshow(img)
axis[0,0].set_title('Original image ')
axis[0,0].axis('off')

axis[0,2].imshow(gradient_sobely)
axis[0,2].set_title('image')
axis[0,2].axis('off')
plt.show()
cv2.waitKey(0)
'''


import matplotlib.pyplot as plt
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_sobelx = cv2.Sobel(img,-1,1,0)
fig,axis = plt.subplots(2,3,figsize = (10,5))

axis[0,0].imshow(img)
axis[0,0].set_title('Original image')
axis[0,0].axis('off')

axis[0,1].imshow(gradient_sobelx)
axis[0,1].set_title('Sobel x image')
axis[0,1].axis('off')

plt.show()
cv2.waitKey(0)










           


















