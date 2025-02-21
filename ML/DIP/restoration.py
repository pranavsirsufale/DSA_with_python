import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a sample medical image ( grayscale )
# Replace *medical_image with the path no your image
image = cv2.imread('F:/DSA/practical/ML/DIP/medical.jpg',cv2.IMREAD_GRAYSCALE)


if image is None:
    raise FileNotFoundError('Image not found. Please provide a valid path')

# Simulate noise in the iamge
noisy_image = image + np.random.normal(loc=0,scale=25,size = image.shape).astype(np.uint8)

# Apply Gaussin filter for denoising 
denoised_image = cv2.GaussianBlur(noisy_image,(5,5),0)

# Apply Gaussin filter for denoising 
denoised_image = cv2.GaussianBlur(noisy_image,(5,5),0)

# Plot the original noisy, and restored images
plt.figure(figsize=(12,8))

plt.subplot(1,3,1)
plt.title('Original Image')
plt.imshow(image,cmap='gray')



plt.subplot(1,3,2)
plt.title('Noisy Image')
plt.imshow(noisy_image,cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title('Restored Image ( Gaussian Filter )')
plt.imshow(denoised_image,cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()