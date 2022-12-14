import win32gui
import win32con
import win32api
import pywintypes
import keyboard
from time import sleep

import win32ui

hwnd = win32gui.FindWindow(None, "Roblox")
offset = (100, 100)

print(hwnd)

while True:
    if win32api.GetAsyncKeyState(win32con.VK_CONTROL):
        print("Closed!")
        break
    if any(win32api.GetAsyncKeyState(i) for i in range(1, 255)):
        print("Continued")
        sleep(1)
        continue

    current_foreground_window = win32gui.GetForegroundWindow()

    try:
        win32gui.SetForegroundWindow(hwnd)
    except pywintypes.error:
        print("Could not set foreground window")

    prev_mouse_pos = win32api.GetCursorPos()

    rect = win32gui.GetWindowRect(hwnd)

    win32api.SetCursorPos((rect[0] + offset[0], rect[1] + offset[1]))

    # Get the width and height of the screen
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    x, y = rect[0], rect[1]

    while True:
        if not (x < 0 or x > screen_width or y < 0 or y > screen_height):
            x, y = win32api.GetCursorPos()
            if x == rect[0] + offset[0] and y == rect[1] + offset[1]:

                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                break
            else:
                win32api.SetCursorPos((rect[0] + offset[0], rect[1] + offset[1]))
            sleep(0.01)
        else:
            print("Window out of screen!")
            break

    # Set the previous foreground window back as the active window
    # try:
    #     sleep(.01)
    #     win32gui.SetForegroundWindow(current_foreground_window)
    # except pywintypes.error:
    #     print("Could not set window")
    win32api.SetCursorPos(prev_mouse_pos)
