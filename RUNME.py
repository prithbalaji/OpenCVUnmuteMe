import tkinter as tk
import mic_control as mic
import read_data as mouthd
import tkinter.font as tkFont

#define global variables 
start_speaking_delay = 10 #delay for someone to begin speaking in ms
stop_speaking_delay = 120 #5 times this value is the time it takes to mute you after stopping in ms

app_enable = True #default is disabled
muted = False     #system defulat is unmuted
talking = 0       #used to determine if someone is talking or not


#define functions 
def switch():
  global muted
  mic.mic_mute_toggle()

  #update labels 
  muted = not muted
  if (muted):
      t = "muted"
      c = 'red'
  else:
      t = "unmuted"
      c= 'green'
  draw_mute_label(t,c)

#disables the application
def disable():
  global app_enable
  app_enable = False
  e = "disabled"
  mouthd.clear_capture()
  draw_enable_label(e)

#enables the applicaiton
def enable():
    global app_enable
    app_enable = True
    e = "enabled"
    mouthd.initialize_capture()
    draw_enable_label(e)
  
#toggles enable/disable  
def enable_toggle():
  if (app_enable):
    disable()
  else:
    enable()

#this method is called repeatedly to track face and 
#determine if someone is talking or not. 
def poll_webcam():
    global talking
    if (app_enable):
      m_open = mouthd.get_mouth_state()
      draw_test_label((m_open == True))
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
       root.after(start_speaking_delay, poll_webcam)# reschedule event


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

disable()

font1 = tkFont.Font(family="Arial", size=12, weight="bold")

#define widgets   
mute_button = tk.Button(text='Toggle Mute',command=switch, bg='red', bd=4, fg='white', font=font1, height=2)
enable_button = tk.Button(text='enable app',command=enable_toggle, bg='red', bd=4, fg='white', font=font1, height=2)
draw_mute_label("unmuted","green")
draw_enable_label("disabled")

#add widgets to canvas 
canvas1.create_window(80, 50, window=mute_button)
canvas1.create_window(220, 50, window=enable_button)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.after(start_speaking_delay, poll_webcam)
root.mainloop()
