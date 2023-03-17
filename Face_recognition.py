import cv2
from cam_setup import cascadePath,cam
from voice import speak

# import pyautogui
# import time

global NAMEs, name_id, data,U
name_id = []
NAMEs = []
data = []
U = []
try:
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('data/face_train_data/trainer.yml')  # load trained model
    faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 100  # number of persons you want to Recognize
    file = open('source/user_names/names.txt','r')
    read = file.readlines()
    names = []

    for line in read:
        if line[-1] == '\n':
            names.append(line[:-1])
        else:
            names.append(line)
    # print(names)
    # names = ['', 'Subhadip', 'Sanchita']  # names, leave first empty bcz counter starts from 0


    cam.set(3, 340)  # set video FrameWidht
    cam.set(4, 280)  # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # flag = True

except:
    print("face data not found !")
    data.append('face data not found !')
    import Age_Gender_recognition
    global A, G
    A = Age_Gender_recognition.det_age
    G = Age_Gender_recognition.det_gen
    if 'Female' in G:
        # print('Hi Mam')
        speak('Hi Mam')
        U.append('Hi Mam')
    if 'Male' in G:
        speak('Hi Sir')
        U.append('Hi Sir')
    import Face_sample_generator
    Face_sample_generator.sampleTake()


def Run():
    while True:

        ret, img = cam.read()  # read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image
            name_id.append(id)
            # Check if accuracy is less them 100 ==> "0" is perfect match
            if (accuracy < 100):

                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                # if (id < 100):
                # print(id, accuracy)
                NAMEs.append(id)
                # import outuput2
                # break




            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                # print("UNKNOWN ! face does not match")
                # import outuput2

                # break
                # import Face_model_train
                NAMEs.append(id)

            # cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            # cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        # cv2.imshow('camera', img)
        cv2.waitKey(10)  # & 0xff  # Press 'ESC' for exiting video
        # if k == 27:
        #     break
        try:
            if id in id:
                break
        except:
            continue

        # Do a bit of cleanup

    cam.release()
    # cv2.destroyAllWindows()

# Run()

