import cv2
import face_detection
import face_recognition
import numpy as np

# Load known face
know_image_path = r'F:/DSA/practical/ML/DIP/panu.jpg'
known_image = face_recognition.load_image_file(know_image_path)


# Get face encondings
known_encoding = face_recognition.face_encoding(known_image)

# Check if face is detected
if len(known_encoding) == 0:
    print('No face detected in the known image. Try another image')
else : 
    known_encoding = known_encoding[0]

# Load the group image ( test image )
test_image_path = r'F:/DSA/practical/ML/DIP/panu.jpg'

text_image = face_recognition.load_image_file(test_image_path)

#

