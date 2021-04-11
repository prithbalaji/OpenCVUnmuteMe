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
start_speaking_delay = 1
stop_speaking_delay = 120

app_enable = True #default is enabled
muted = False #case where muted starts as true?
talking = 0


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
    global talking
    if (app_enable):
      m_open = mouthd.get_mouth_state()
      if (muted and m_open):
        switch()
        talking = 5
      elif ((not muted) and (not m_open)):
        if (talking >0):
            talking = talking -1
        else:
          switch()
      elif (m_open and (not muted)):
        talking = 5
  
    draw_test_label(talking)
    if (talking>0):
      root.after(stop_speaking_delay, poll_webcam) # reschedule event
    else:
       root.after(start_speaking_delay, poll_webcam)


def draw_mute_label(t,c):
    mute_label = tk.Label(root, text= t, fg=c, bd= 4, font=('Arial', 14, 'bold'), background='yellow')
    canvas1.create_window(80, 150, window=mute_label)

def draw_enable_label(e):
    enable_label = tk.Label(root, text= e, fg="black", bd= 4, font=('Arial', 14, 'bold'), background='yellow')
    canvas1.create_window(220, 150, window=enable_label)

def draw_test_label(test):
    test_label = tk.Label(root, text= test, fg="blue", font=('helvetica', 12, 'bold'))
    canvas1.create_window(200, 200, window=test_label)

def on_closing():
    if (muted):
      switch()
    root.destroy()


#define app
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, background='yellow')
canvas1.pack()

##todo how to check if system muted already?

disable()

#define widgets   
mute_button = tk.Button(text='Toggle Mute',command=switch, bg='red', bd=4, fg='white', font=font1, height=2)
enable_button = tk.Button(text='enable app',command=enable_toggle, bg='red', bd=4, fg='white', font=font1, height=2)
draw_mute_label("unmuted","green")
draw_enable_label("disabled")


#add widgets to canvas 
canvas1.create_window(80, 50, window=mute_button)
canvas1.create_window(220, 50, window=enable_button)


#mouthd.initialize_capture()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.after(start_speaking_delay, poll_webcam)
root.mainloop()
