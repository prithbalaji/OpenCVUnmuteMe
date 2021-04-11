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

app_enable = True #default is enabled
muted = False #case where muted starts as true?


#define functions 
def switch():
  global muted
  # t = "unmuted" #default value
  # c = "green" #default value

  #if (app_enable): #no longer necessary
  mic.mic_mute_toggle()

  muted = not muted
  if (muted):
      t = "muted"
      c = 'red'
  else:
      t = "unmuted"
      c= 'green'
  draw_mute_label(t,c)

def disable():
  global app_enable
  app_enable = False
  e = "disabled"
  mouthd.clear_capture()
  draw_enable_label(e)

def enable():
    global app_enable
    app_enable = True
    e = "enabled"
    mouthd.initialize_capture()
    draw_enable_label(e)
  
def enable_toggle():
  if (app_enable):
    disable()
  else:
    enable()

def poll_webcam():
    if (app_enable):
      m_open = mouthd.get_mouth_state()
      if ((muted and m_open) or ((not muted) and (not m_open))):
        switch()
        draw_test_label(muted)
    root.after(webcam_poll_delay, poll_webcam)  # reschedule event 

def draw_mute_label(t,c):
    mute_label = tk.Label(root, text= t, fg=c, font=('helvetica', 12, 'bold'))
    canvas1.create_window(50, 150, window=mute_label)

def draw_enable_label(e):
    enable_label = tk.Label(root, text= e, fg="black", font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=enable_label)

def draw_test_label(test):
    test_label = tk.Label(root, text= test, fg="blue", font=('helvetica', 12, 'bold'))
    canvas1.create_window(200, 200, window=test_label)

def on_closing():
    if (muted):
      switch()
    root.destroy()

#define app
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

##todo how to check if system muted already?

disable()

#define widgets   
mute_button = tk.Button(text='Toggle Mute',command=switch, bg='brown',fg='white')
enable_button = tk.Button(text='enable app',command=enable_toggle, bg='brown',fg='white')
draw_mute_label("unmuted","green")
draw_enable_label("disabled")

#add widgets to canvas 
canvas1.create_window(50, 50, window=mute_button)
canvas1.create_window(150, 50, window=enable_button)


#mouthd.initialize_capture()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.after(webcam_poll_delay, poll_webcam)
root.mainloop()
