#installation for anaconda: conda install -c conda-forge python-sounddevice
# for windows, try: python3 -m pip install sounddevice

import sounddevice as sd
import mic_control
duration = 5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata             # feeds your input to your output

with sd.RawStream(channels=2, dtype='int24', callback=callback):
    print("not muted")
    sd.sleep(int(duration * 1000))  # wait 5 seconds
    mic_control.mic_mute_toggle()   # mute 
    print("muted")
    sd.sleep(int(duration * 1000))  # wait 5 seconds
    mic_control.mic_mute_toggle()   # unmute
    print("not muted")
    sd.sleep(int(duration * 1000))  # wait 5 more seconds
    
