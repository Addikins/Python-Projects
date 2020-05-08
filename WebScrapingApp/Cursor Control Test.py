import pyautogui, time, keyboard


def searchText():
    pyautogui.click(465, 15)
    pyautogui.moveTo(565, 470)
    pyautogui.dragTo(1530, 470, duration=0.3)

    pyautogui.hotkey("ctrl", "c")
    time.sleep(.5)
    pyautogui.hotkey("ctrl", "t")
    time.sleep(.5)
    pyautogui.press("\"")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("\"")
    pyautogui.press("enter")


def searchPage():
    pyautogui.hotkey("ctrl", "f")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")


while True:
    if keyboard.is_pressed('+'):
        searchText()
    elif keyboard.is_pressed("-"):
        searchPage()
