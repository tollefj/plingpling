import time
import serial
import win32api
import winsound
import os
PLAY_PAUSE = 0xB3
PP_MAP = win32api.MapVirtualKey(PLAY_PAUSE, 0)
# SETUP ARDUINO
ard = serial.Serial()

def tryPort(com):
    port_name = "COM" + str(com)
    try:
        global ard
        ard = serial.Serial(port_name, 9600, timeout=0)
        return True
    except:
        #  print(port_name + " unavailable")
        return False

def init():
    available = False
    for comPort in range(1, 12):
        if tryPort(comPort):
            available = True
            print ("Connection established: COM" +
                   str(comPort) + ", please wait.")
            time.sleep(2)
            break
    if available:
        print ("KLAR TIL PLING!")

def new_file(name):
    return os.path.join(os.getcwd(), name) + '.wav'

def play(sound):
    winsound.PlaySound(sound, winsound.SND_FILENAME)

if __name__ == "__main__":
    init()
    dasdass = new_file('das-dass')
    horn = new_file('horn')
    while True:
        data = ard.readline()[:-2]  # ignore newline plz
        if data:
            win32api.keybd_event(PLAY_PAUSE, PP_MAP)
            play(horn)
            play(dasdass)
            win32api.keybd_event(PLAY_PAUSE, PP_MAP)
            data = False
