import tkinter as tk
import mic_control as mic

app_enable = True
muted = False #case where muted starts as true?

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()



def switch():
    mic.mic_mute_toggle()
    global muted
    muted = not muted
    if (muted):
        t = "muted"
        c = 'red'
    else:
        t = "unmuted"
        c= 'green'
    label1 = tk.Label(root, text= t, fg=c, font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

def enable_toggle():
    global app_enable
    app_enable = not app_enable
  

button1 = tk.Button(text='Toggle Mute',command=switch, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()