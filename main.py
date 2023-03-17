import time
import tkinter as tk
import main_prog
root = tk.Tk()
root.title("A!")
root.geometry("500x300+430+150")
root.resizable(False, False)
root.config(bg='blue')
# root.attributes('-alpha',0.5)
dis = main_prog.U
var = tk.StringVar()
var.set(dis)
def PgRun():
    # B1.place_forget()
    # time.sleep(10)
    from main_prog import mainRun
    mainRun()


text = tk.Label(root, textvariable=var,font=(20), fg='white', bg='blue', width=50, height=10)
text.place(x=23, y=30)

B1 = tk.Button(root,text= "START", bg='white',width=20,height=2,command = lambda:PgRun())
B1.place(x=170, y=240)
# root.mainloop()
# root.update()
root.mainloop()
