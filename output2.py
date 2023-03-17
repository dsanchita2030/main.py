
import time
import datetime
import Face_sample_generator
import Age_Gender_recognition
from voice import speak

A = Age_Gender_recognition.det_age
G = Age_Gender_recognition.det_gen
user = Face_sample_generator.user
user_id = Face_sample_generator.user_id
nameid = 0
userid = 0
ageid = 0
genid = 0
nameid = user[nameid]
userid = user_id[userid]
ageid = A[ageid]
genid = G[genid]

# speak(f'Hey {nameid} How are you?')
hour = float(datetime.datetime.now().hour)
tt = time.strftime("%I:%M %p")

if hour >= 00 and hour <= 11:
    # speak("Namastay.  Good Morning ")
    speak(f'Good Morning {nameid} ,have a nice day,How are you?')

elif hour >= 12 and hour <= 16:
    speak(f'Good Afternoon {nameid} ,How are you?')

elif hour >= 17 and hour <= 21:
    speak(f'Good Evening {nameid} ,How are you?')

else:
    speak(f'Hey {nameid} ,what am i do?')

print(f"User_Age: {ageid}")
print(f"User_Gender: {genid}")

def user_win():
    import tkinter as tk
    from PIL import Image, ImageTk
    # Window Setup
    bg_color = 'blue'
    fn_color = 'white'
    root = tk.Tk()
    root.title('User Details')
    root.iconbitmap('')
    root.config(bg='blue')
    root.attributes('-alpha',0.8)
    root.geometry("250x280+1080+150")
    root.resizable(False, False)

    # image Setup
    H = 150
    W = 150
    path = "source/user_img/user_img/" + str(nameid) + "." + str(userid) + ".png"
    male_pathe = "source/user_img/Default_img/male.png"
    female_pathe = "source/user_img/Default_img/female.png"
    try:
        pic = Image.open(path)
    except:

        if 'Male' in genid:
            pic = Image.open(male_pathe)
        elif 'Female' in genid:
            pic = Image.open(female_pathe)

        resize_pic = pic.resize((W,H))
        final_pic = ImageTk.PhotoImage(resize_pic)

        # window Customize
        name_text = tk.Label(root, font=('bold',12), text=f'{nameid}', fg=fn_color,bg=bg_color, width=15, height=1, highlightthickness=1, highlightbackground="white")
        name_text.place(x=55, y=10)

        # image = tk.Label(root, image=final_pic, width=W, height=H, highlightthickness=1, highlightbackground="blue")
        # image.place(x=50, y=50)

        gen_text = tk.Label(root, text='Gender :', fg=fn_color ,bg=bg_color, width=6, height=1)
        gen_text.place(x=8, y=235)
        gen_text2 = tk.Label(root, text=f'{genid}', fg=fn_color ,bg=bg_color, width=5, height=1)
        gen_text2.place(x=60, y=235)

        age_text = tk.Label(root, text='Age :' , fg=fn_color,bg=bg_color, width=6, height=1)
        age_text.place(x=0, y=250)
        age_text2 = tk.Label(root, text=f'Approx {ageid} years old', fg=fn_color,bg=bg_color, width=18, height=1)
        age_text2.place(x=40, y=250)

        # window run
        root.mainloop()