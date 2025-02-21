# Import requird libraries 
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load the pre-trained YOLOv8 model
model = YOLO('yolov8s.pt') 

# Load an image
image_path = r'F:/DSA/practical/ML/DIP/per.jpg'
image = cv2.imread(image_path)

## Check if the image is loaded
if image is None:
    print('Error : Unable to load the image. Check the file path')
    exit()


# Performr object detection 
results = model.predict(image)


# amotate the detected objects
annoted_image = results[0].plot() 

# SAve the annoted image
output_path = r'F:/DSA/practical/ML/DIP/per.jpg' ## Save in the correct location
cv2.imwrite(output_path,annoted_image)

print(f'Annoted image saved at {output_path}')

# Display the original and detected images side by side
plt.figure(figsize=(12,6))

# Original image 
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Original Image')

# Object Detection Output
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(annoted_image,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Object Detection Output')

plt.show()


