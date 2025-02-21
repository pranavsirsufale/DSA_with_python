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

# Convert images for OpenCV display
known_image_bgr = cv2.cvtColor(known_image,cv2.COLOR_RGB2BGR)
original_group_image = cv2.cvtColor(text_image, cv2.COLOR_RGB2BGR)

# Detect faces in the group image
face_location = face_recognition.face_locations(text_image)
face_encding = face_recognition.face_encoding(text_image,face_location)


for(top, right, bottom,left),face_encding in zip(face_location,face_encding):
    matches = face_recognition.compare_faces([known_encoding],face_encding)
    name = 'UNKKNOWN'
    if True in matches:
        name = "Pranav . Sirsufale"


    # Draw a box around each detected face
    cv2.rectangle(text_image,(left,top),(right,bottom),(0,255,0),3)

    # Adjust text position to avoid overlap
    font_scale = max((right - left) / 300 , 0.6) ## Dynamic scaling
    thickness = 2 
    text_size = cv2.getTextSize(name,cv2.FONT_HERSHEY_SIMPLEX,font_scale,thickness)[0]

