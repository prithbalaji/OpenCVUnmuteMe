#To turn this into windows executable
#run: pip install pyinstaller
#in the project directory run: pyinstaller --onefile RUNME.py
#then the executable will appear under the \dist folder
#note: uses python 3.5+ 

import tkinter as tk
import mic_control as mic
import read_data as mouthd
import tkinter.font as tkFont

#define global variables 

#webcam_connected = False
webcam_poll_delay = 50

app_enable = True
muted = False #case where muted starts as true?

dynamic_buttons = []

#define functions 
def switch():
  t = "unmuted" #default value
  c = "green" #default value
  if (app_enable): #only do anything if enabled
    mic.mic_mute_toggle()
    global muted
    muted = not muted
    if (muted):
        t = "muted"
        c = 'red'
    else:
        t = "unmuted"
        c= 'green'
  draw_mute_label(t,c)

def enable_toggle():
    global app_enable
    app_enable = not app_enable
    if (app_enable):
      e = "enabled"
    else:
      e = "disabled"
    draw_enable_label(e)

def poll_webcam():
    print(mouthd.get_mouth_state())
    root.after(webcam_poll_delay, poll_webcam)  # reschedule event 

def draw_mute_label(t,c):
    mute_label = tk.Label(root, text= t, fg=c, bd= 4, font=('Arial', 14, 'bold'), background='yellow')
    canvas1.create_window(80, 150, window=mute_label)

def draw_enable_label(e):
    enable_label = tk.Label(root, text= e, fg="black", bd= 4, font=('Arial', 14, 'bold'), background='yellow')
    canvas1.create_window(220, 150, window=enable_label)

#define app
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, background='yellow')
canvas1.pack()
  
font1 = tkFont.Font(family="Arial", size=12, weight="bold")

#define widgets   
mute_button = tk.Button(text='Toggle Mute',command=switch, bg='red', bd=4, fg='white', font=font1, height=2)
enable_button = tk.Button(text='enable app',command=enable_toggle, bg='red', bd=4, fg='white', font=font1, height=2)
draw_mute_label("unmuted","green")
draw_enable_label("enabled")

#add widgets to canvas 
canvas1.create_window(80, 50, window=mute_button)
canvas1.create_window(220, 50, window=enable_button)


mouthd.initialize_capture()
root.after(webcam_poll_delay, poll_webcam)
root.mainloop()
