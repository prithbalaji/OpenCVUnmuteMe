#To turn this into windows executable
#run: pip install pyinstaller
#in the project directory run: pyinstaller --onefile RUNME.py
#then the executable will appear under the \dist folder
#note: uses python 3.5+ 

import tkinter as tk
import mic_control as mic
import read_data as mouthd

#define global variables

#webcam_connected = False
webcam_poll_delay = 50

app_enable = True
muted = False #case where muted starts as true?
t = "unmuted"
c = 'green'

#define functions 
def switch():
    mic.mic_mute_toggle()
    global muted
    global t
    global c
    muted = not muted
    if (muted):
        t = "muted"
        c = 'red'
    else:
        t = "unmuted"
        c= 'green'
    
def enable_toggle():
    global app_enable
    app_enable = not app_enable
    
def poll_webcam():
    print(mouthd.get_mouth_state())
    root.after(webcam_poll_delay, poll_webcam)  # reschedule event
    
#define application gui    
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

#create widgets  
button1 = tk.Button(text='Toggle Mute',command=switch, bg='brown',fg='white')
label1 = tk.Label(root, text= t, fg=c, font=('helvetica', 12, 'bold'))

#add widgets to canvas
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(150, 200, window=label1)



#mouthd.initialize_capture()
#root.after(webcam_poll_delay, poll_webcam)
root.mainloop()
