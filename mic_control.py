#in order to run this use 
#pip install pywin32
import win32api
import win32gui


WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000


def mic_mute_toggle():
  hwnd_active = win32gui.GetForegroundWindow()
  win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
