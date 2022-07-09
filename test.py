import face_recognition
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, False)

#test_image = face_recognition.load_image_file("/home/pi/doorlock/test.jpg")
#hun_face_encoding = face_recognition.face_encodings(test_image)[0]
#np.save('hun.npy',hun_face_encoding)

# hun_face_encoding = np.load('hun.npy')



video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        if face_locations :
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            np.save('/home/pi/doorlock/test1.npy',face_encodings[0])
            break
            
    process_this_frame = not process_this_frame
    
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()