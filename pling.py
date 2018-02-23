import time
import serial
import win32api
import winsound
import os
import logging
from pycaw.pycaw import AudioUtilities

def setup_logger(name, log_file):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


status_log = setup_logger('pling_status', 'pling_status.log')
pling_log = setup_logger('pling_count', 'pling_count.log')

# used to keep track of when the PC is switched on
status_log.info('Opened pling!')

# Setup arduino
ard = serial.Serial()


# Iterate through available com-ports
def tryPort(com):
    port_name = "COM" + str(com)
    try:
        global ard
        # attempt to set ard to the current serial port
        ard = serial.Serial(port_name, 9600, timeout=0)
        return True
    except:
        return False


def init():
    available = False
    # @NBB, COM1 was busy, iterating from 2.
    for comPort in range(2, 12):
        if tryPort(comPort):
            available = True
            time.sleep(2)
            break
    if available:
        print ('Klar til pling!')


def new_file(name):
    return os.path.join(os.getcwd(), name) + '.wav'


# play the .WAV file in /dist directory
def play(sound):
    winsound.PlaySound(sound, winsound.SND_FILENAME)


def toggle_volume(mute=True):
    apps = ['Spotify.exe', 'chrome.exe']
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() in apps:
                volume.SetMute(mute, None)



if __name__ == "__main__":
    #  init()
    # IMPORTANT:
    # ONLY include the file name here, not the file extension
    # .WAV is added in the function new_file
    warning = new_file('warning')
    song = new_file('song')
    while True:
        #  read "1" from the arduino when the switch is toggled
        data = ard.readline()[:-2]  # ignore newline
        if data:
            toggle_volume() # mute spotify og chrome!
            #log this event!
            pling_log.info("ny pling!")
            play(warning)
            #  play(song)
            toggle_volume(mute=False)
