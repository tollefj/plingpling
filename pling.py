import time
import serial
import win32api
import winsound
import os
import logging


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(time)s %(message)s'))

    logger = logging.getLogger(name)
    logger.addHandler(handler)

    return logger


status_log = setup_logger('pling_status', 'pling_status.log')
pling_log = setup_logger('pling_count', 'pling_count.log')

# used to keep track of when the PC is switched on
status_log.info('Opened pling!')

# 0xB3 is the key mapped to "play/pause" on media keyboards
# Map this key through the win32 api
PLAY_PAUSE = 0xB3
PP_MAP = win32api.MapVirtualKey(PLAY_PAUSE, 0)

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
            print ("Connection established: COM" +
                   str(comPort) + ", please wait.")
            time.sleep(2)
            break
    if available:
        print ('READY TO PLING!')


def new_file(name):
    return os.path.join(os.getcwd(), name) + '.wav'


# play the .WAV file in /dist directory
def play(sound):
    winsound.PlaySound(sound, winsound.SND_FILENAME)


# create a keyboard event, simulating the media key
def play_pause():
    win32api.keybd_event(PLAY_PAUSE, PP_MAP)


if __name__ == "__main__":
    init()
    # IMPORTANT:
    # ONLY include the file name here, not the file extension
    # .WAV is added in the function new_file
    warning = new_file('warning')
    song = new_file('song')

    while True:
        # read "1" from the arduino when the button is toggled
        data = ard.readline()[:-2]  # ignore newline
        if data:
            # log this event!
            pling_log.info("ny pling!")
            print ('PLING PLONG')
            play_pause()
            play(warning)
            play(song)
            play_pause()
            # safety net
            data = False
