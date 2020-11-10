#!/bin/python3

import os
from pynput.keyboard import Key, Listener

# Push to talk hotkey
KEY = Key.scroll_lock

pstate = False
def mute(state):
    global pstate
    if pstate == state:
        return
    if state:
        os.system("amixer set Capture nocap")
    else:
        os.system("amixer set Capture cap")
    pstate = state

mute(True)

def on_press(key):
    if key == KEY:
        mute(False)

def on_release(key):
     if key == KEY:
        mute(True)
   

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
