import cv2
brigh_image = cv2.imread('fish.jpg')
darkening_factor = 50 
dark_image = cv2.subtract(brigh_image, darkening_factor)
dark_image = cv2.max(dark_image,0)

cv2.imshow('Original Image',brigh_image)
cv2.imshow('Dark Image', dark_image)
cv2.waitKey(0)
cv2.destroyAllwindows()





import cv2
import numpy as np
img = cv2.imread('noicy.jpg',0)
denoised = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('original Image',img)
cv2.imshow('denoised iamge',denoised)
if( cv2.waitKey() == ord('q') ):
    cv2.destroyAllWindows()




### Image compresson and storage
import cv2 
img = cv2.imread('spidy.jpg',1)
compressed_img_param = [cv2.IMWRITE_JPEG_QUALITY,50]
cv2.imwrite('compressed_sharp_img2.jpg',img,compressed_img_param)




import cv2
path = 'E:/pranav sirsufale/spidy.jpg'
img = cv2.imread('spidy.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()














import cv2
image = cv2.imread('skel.jpg', 0)
# Load as grayscale (0)
threshold_value = 127
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




'''
def plot_histogram(img,title):
    hist=cv2.calcHist([img],[0],None,[256],[0,255])
    plt.plot(hist)
bright = cv2.imread('bright.jpg',0)
dark = cv2.imread('skel.jpg',0)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plot_histogram(bright,"bright")
plt.title("bright image histogram")
plt.subplot(2,2,2)
plot_histogram(dark,"dark")
plt.title("dark image histogram")
plt.tight_layout()
plt.show()



img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_laplacian = cv2.Laplacian(img, -1 , )
fig , axis = plt.subplots(2,3,figsize = (10 , 5 ))
axis[0,0].imshow(img)
axis[0,0].set_title('original image')
axis[0,0].axis('off')

axis[1,1].imshow(gradient_laplacian)
axis[1,1].set_title('laplacian image is')
axis[1,1].axis('off')
plt.show()
cv2.waitKey()


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_sobelx = cv2.Sobel(img,-1,1,0)
fig,axis = plt.subplots(2,3,figsize=(10,5))
axis[0,0].imshow(img)
axis[0,0].set_title('Original image')
axis[0,0].axis('off')
axis[0,1].imshow(gradient_sobelx)
axis[0,1].set_title('soble x image')
axis[0,1].axis('off')
plt.show()
cv2.waitKey()



img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_sobely=cv2.Sobel(img,-1,0,1)
fig, axis = plt.subplots(2, 3, figsize=(10, 5))
#figsize is the size of the window 2 and 3 are the rows and columns respectively
axis[0,0].imshow(img)
axis[0,0].set_title('Original image')
axis[0,0].axis('off')
axis[0,2].imshow(gradient_sobely)
axis[0,2].set_title('sobel y image')
axis[0,2].axis('off')
plt.show()
cv2.waitKey()




output_bilateral = cv2.bilateralFilter(img,5,6,6)
cv2.imshow('bilateral filter',output_bilateral)

## ORIGINAL IMAGE
cv2.imshow('original image',img)
cv2.waitKey(0)









img = cv2.imread('aiim.jfif')
output_gaussian = cv2.GaussianBlur(img,(5,5), 0 )
cv2.imshow('gaussian blur',output_gaussian )
cv2.imshow('original image', img)
cv2.waitKey(0)











import cv2 
import numpy as np
import matplotlib.pyplot as plt

dark_img = cv2.imread('fish dark.png')
brightening_factor = 50

bright_img = np.clip(dark_img + brightening_factor , 0 , 255 ).astype(np.uint8)

plt.figure(figsize = (10 , 6 ) )

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(dark_img.cv2.COLOR_BGR2RGB))
plt.title('Original Dark Image ')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(dark_img , cv2.COLOR_BGR2RGB))
plt.title('Newly Brightned Image ')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destrolyAllWindows()
'''
