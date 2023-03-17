import cv2
import numpy as np
from PIL import Image #pillow package
import os
import time
import Face_sample_generator
from voice import speak
from cam_setup import cascadePath

dir = "source/face_samples/"
path = dir  # Path for samples already taken

def unknownTrain():
    Face_sample_generator.sampleTake()

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    detector = cv2.CascadeClassifier(cascadePath)

    # Haar Cascade classifier is an effective object detection approach

    def Images_And_Labels(path):  # function to fetch the images and labels

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:  # to iterate particular image path

            gray_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_arr = np.array(gray_img, 'uint8')  # creating an array

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)

            for (x, y, w, h) in faces:
                faceSamples.append(img_arr[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids

    speak("Training faces. It will take a few seconds. Wait ...")
    # time.sleep(8)

    faces, ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('data/face_train_data/trainer.yml')  # Save the trained model as trainer.yml

    speak("Model trained Successful, Now we can recognize your face.")

    time.sleep(2)
    # from user_dpWin import run
    # run()
    import output2

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    detector = cv2.CascadeClassifier("data/face_data/haarcascade_frontalface_default.xml")

    # Haar Cascade classifier is an effective object detection approach

    def Images_And_Labels(path):  # function to fetch the images and labels

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:  # to iterate particular image path

            gray_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_arr = np.array(gray_img, 'uint8')  # creating an array

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)

            for (x, y, w, h) in faces:
                faceSamples.append(img_arr[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids

    speak("Training faces. It will take a few seconds. Wait ...")
    # time.sleep(8)

    faces, ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('data/face_train_data/trainer.yml')  # Save the trained model as trainer.yml

    speak("Model trained Successful, Now we can recognize your face.")

    time.sleep(2)