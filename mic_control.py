

import sys 

if (sys.platform == "win32"):
  #in order to run this use 
  #pip install pywin32
  #only works on windows using the Win32 api
  import win32api
  import win32gui

  WM_APPCOMMAND = 0x319
  APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

  def mic_mute_toggle():
    hwnd_active = win32gui.GetForegroundWindow()
    win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

elif (sys.platform == "darwin"):
  SET_VOLUME_COMMAND = "set volume input volume {value}"
  GET_INPUT_VOL_COMMAND = "input volume of (get volume settings)"
  DEFAULT_VOLUME = 75 

  def execute_apple_script(command):
      result = subprocess.run(["osascript", "-e", command], stdout=subprocess.PIPE)
      output = result.stdout.decode("utf-8")
      result = output.strip()
      try:
          return int(result)
      except ValueError:
          return 0

  def mic_mute_toggle():
      volume = execute_apple_script(GET_INPUT_VOL_COMMAND)
      if (volume != 0):
          execute_apple_script(SET_VOLUME_COMMAND.format(value = 0))
      else:
          execute_apple_script(SET_VOLUME_COMMAND.format(value = DEFAULT_VOLUME))
else:
  raise Exception("bad platform: not supported, this application only works on Windows and Mac")
