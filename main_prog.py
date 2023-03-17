from voice import speak, takecommand
global U
U =[]

def mainRun():
    # import time
    import sys
    import Age_Gender_recognition
    global A, G
    A = Age_Gender_recognition.det_age
    G = Age_Gender_recognition.det_gen
    data2 = Age_Gender_recognition.data2
    Age_Gender_recognition.result()
    import Face_recognition
    name = Face_recognition.NAMEs
    data = Face_recognition.data
    while True:
        if 'Female' in G:
            # print('Hi Mam')
            speak('Hi Mam')
            U.append('Hi Mam')
            # L1['text'] = G
            speak('may i help you ? ')
            user = takecommand()
            # user = input('may i help you?: ')
            if ' ' in user or 'none' in user:
                speak("i dont understand! write your command")
                user = input('write: ')
                if 'yes' in user or 'yaha' in user or 'sure' in user:
                    Face_recognition.Run()
                    # print(A)
                elif 'model train' in user or 'train model' in user:
                    import Face_model_train
                    Face_model_train.train()
                    break
                else:
                    sys.exit()
            elif 'yes' in user or 'yaha' in user or 'sure' in user:
                Face_recognition.Run()
                # print(A)
            elif 'model train' in user or 'train model' in user:
                import Face_model_train
                Face_model_train.train()
                break
            else:
                sys.exit()

        if 'Male' in G:
            speak('Hi Sir')
            U.append('Hi Sir')
            # L1['text'] = G
            speak('may i help you ? ')

            user = takecommand()
            # user = input('may i help you?: ')
            if ' ' in user or 'none' in user:
                speak("i dont understand! write your command")
                user = input('write: ')
                if 'yes' in user or 'yaha' in user or 'sure' in user:
                    Face_recognition.Run()
                    # print(A)
                elif 'model train' in user or 'train model' in user:
                    import Face_model_train
                    Face_model_train.train()
                    break
                else:
                    sys.exit()
            elif 'yes' in user or 'yaha' in user or 'sure' in user:
                Face_recognition.Run()
                # print(A)
            elif 'model train' in user or 'train model' in user:
                import Face_model_train
                Face_model_train.train()
                break
            else:
                sys.exit()

        if 'unknown' in name:
            print(" Sorry I dont Remember You ! Please Say Your Name")
            import Face_model_train
            Face_model_train.unknownTrain()
            break
        else:

            import output1

            break

mainRun()
