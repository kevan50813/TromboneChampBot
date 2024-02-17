import pyautogui as screenshot
import pyscreenshot as ImageGrab

def screenshot():
    # fullscreen
    im=ImageGrab.grab()
    im.show()

    # part of the screen
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.show()
    return im