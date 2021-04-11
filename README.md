# OpenCVUnmuteMe
# HackIllinois 2021 project: using OpenCV to detect visual cues to see if someone is speaking or not, then muting or unmuting their microphone accordingly.

### Inspiration

The true inspiration for this project comes from our team’s vested interest in silencing the petty annoyances of our daily lives. This project aims to reduce background noise in voice calls. Quite simply, we are seeking to create an app that mutes someone when they are not speaking and unmutes them when they are. It is essentially a convenient form of courtesy in voice calls. It is especially helpful in large calls, meetings, or classes when small amounts of background noise can create distractions and generally pull attention away from whatever the subject of the meeting is. In this way, our app solves a real problem.

The inspiration also comes from our desire to learn. We have a common interest in computer vision and its applications. Since we are all freshmen and for most of us this is our first hackathon, we wanted to create something simple.

### What it does

OpenCVUnmuteMe is an application that uses Open-cv python to use someone’s webcam to track their face. The face tracker detects when someone is speaking or not. When enabled, it mutes a person when they are not speaking. The purpose is to eliminate background noise in a voice call. This is why it uses visual cues to determine if someone is speaking as opposed to audio cues. Our app allows this face tracking feature to be enabled or disabled. Also, there is a feature to manually mute or unmute yourself, although only really works when face tracking is disabled. When it comes down to it, this app does one thing and it does it pretty well.

### How we built it

We used OpenCV-Python, a library in Python which allows us to solve computer vision problems, to accomplish this project. Additionally, we used Dlib, a cross-platform software library, which detects facial cues with pre-trained models. Pywin32 api was used to toggle the microphone on and off. Tkinter was used to create the gui which allows someone to use our app.

### Challenges we ran into

The first major challenge was getting opencv to track someone’s face. Tutorials were instrumental in helping to implement this portion. Next we had to use the output from Open-cv and turn it into a boolean that we could use to mute or unmute the microphone. Since we were using tkinter as a interface, we had to disassemble the loop we had used to run the face tracking and convert it into a repeated function call. Finally, part of our group was running on mac and there were a lot of compatibility issues which we had to deal with. However, we do believe it runs on mac now.

### Accomplishments that we're proud of

Solving a real problem
The fact that our solution works pretty well
Cross platform compatibility (windows and mac)
Getting familiar with open-cv and computer vision(none of us had used it before or had any experience)
What we learned

First and foremost, this project helped all of us develop our teamwork and collaboration skills greatly. We were able to delegate tasks per each of our strengths and interests. On top of that, we all helped each other test and troubleshoot the application throughout the entire development process.

Aside from this, we learned how to use libraries like dlib and openCV which none of us had any prior experience with using. We became very familiar with these libraries and learned how to manipulate them and have them interact with and manipulate our computer microphone. We also learned how to use the mic controller python API which took a lot of patience and research to get working properly on both Windows and MacOS platforms. Many of us were also inexperienced in python, which was heavily leveraged on this project. We have to look through lots of python documentation while developing. On top of this, we had to learn how to work with the anaconda and windows command prompts to test and develop our application which was developed in Visual Studio Code.

### What's next for OpenCVUnmuteMe

Unfortunately, our app does not currently allow face tracking to work simultaneously with a video call. This is a major drawback and something we were unable to implement on the last day of the hackathon. Once this is added as a feature, our app would probably work on integrating our application with various video conferencing applications such as Zoom, Microsoft Teams, Discord calls, Facetime, etc.


## How to run this project 

### windows 

* have ptyhon3 installed  
* download the [github](https://github.com/awandke/OpenCVUnmuteMe) files to a repository
* install dlib for python, there are countless resources for this on the web 
  * [dlib site](http://dlib.net/compile.html#:~:text=Using%20dlib%20from%20Python,to%20use%20dlib%20from%20Python.)
* install [OpenCV-Python](https://docs.opencv.org/4.5.0/d5/de5/tutorial_py_setup_in_windows.html)
* extra installations 
```
  pip install --upgrade imutils
  pip install opencv-contrib-python
  pip install pywin32
```
* in order to launch the app, run RUNME from the directory:
```
python RUNME.py
```

### mac
