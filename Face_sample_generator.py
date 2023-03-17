# import random
# import time
import sys
import cv2
import os
from voice import speak, takecommand

# Haar Cascade classifier is an effective object detection approach
# while True:

global user, user_id
user = []
user_id = []
# speak4("Taking samples, look at camera ")

def sampleTake():
    from cam_setup import cascadePath,cam
    cam.set(3, 640)  # set video FrameWidth
    cam.set(4, 480)  # set video FrameHeight

    detector = cv2.CascadeClassifier(cascadePath)

    file = open('source/user_names/names.txt', 'a')
    count = 0  # Initializing sampling face count
    speak('What is Your Name?')
    name = takecommand()
    if 'stop' in name or 'cancel' in name or 'sorry' in name:
        # break
        sys.exit()
    speak("its correct ?")
    c = takecommand()
    if "no" in c:
        speak("ok write your name")
        name = input('write: ')
        file.write(name + "\n")
        file.close()
        user.append(name)
        f = open('source/user_names/names.txt', mode='r')
        no_of_lines = 0
        for line in f:
            no_of_lines += 1

        # file2 =
        face_id = no_of_lines - 1  # Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)
        user_id.append(face_id)

    elif ' ' in name or 'none' in name:
        speak("i dont understand! write your name")
        name = input('write: ')
        file.write(name + "\n")
        file.close()
        user.append(name)
        f = open('source/user_names/names.txt', mode='r')
        no_of_lines = 0
        for line in f:
            no_of_lines += 1

        # file2 =
        face_id = no_of_lines - 1  # Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)
        user_id.append(face_id)



    else:

        file.write(name + "\n")
        file.close()
        user.append(name)
        f = open('source/user_names/names.txt', mode='r')
        no_of_lines = 0
        for line in f:
            no_of_lines += 1

        # file2 =
        face_id = no_of_lines - 1  # Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)
        user_id.append(face_id)
    print('Look At camera..')
    while True:

        ret, img = cam.read()  # read the frames using the above created object
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another
        faces = detector.detectMultiScale(converted_image, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # used to draw a rectangle on any image
            count += 1
            if not os.path.exists("source/face_samples/"):
                # if the demo_folder directory is not present
                # then create it.
                os.makedirs("source/face_samples/")

            cv2.imwrite("source/face_samples/" + str(name) + "." + str(face_id) + '.' + str(count) + ".jpg",
                        converted_image[y:y + h, x:x + w])
            # To capture & Save images into the datasets folder

            cv2.imshow('Sample Generate', img)  # Used to display an image in a window

        k = cv2.waitKey(100) & 0xff  # Waits for a pressed key
        if k == 27:  # Press 'ESC' to stop
            break
        elif count >= 100:  # Take 50 sample (More sample --> More accuracy)
            break

        print('Face Storing... ')


    # time.sleep(4)
    cam.release()
    cv2.destroyAllWindows()

    # import Age_Gender_recognition

    # import Face_model_train
    # Face_model_train.train()

# sampleTake()