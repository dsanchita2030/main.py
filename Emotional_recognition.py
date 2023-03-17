import cv2
from deepface import DeepFace
import numpy as np

from cam_setup import cascadePath,cam
faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach
font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type


while True:
    _,frame = cam.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5)

    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        try:
            attributes = ['emotion']
            analyze = DeepFace.analyze(frame,attributes)
            emotion = analyze[0]['dominant_emotion']
            print(emotion)
            # print(analyze)
        except:
            print('No face Detect')

    cv2.putText(img, str(emotion), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

    cv2.imshow('Ai Sanchi', frame)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting cam
    if k == 27:
        break

cam.release()

# angry
# disgust
# fear
# happy
# sad
# surprise
# neutral