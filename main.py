# you will need the win32 libraries for this snippet of code to work, Links below
import win32gui
import win32con
import win32api
import pywintypes
import keyboard
from time import sleep

# [hwnd] No matter what people tell you, this is the handle meaning unique ID,
# ["Notepad"] This is the application main/parent name, an easy way to check for examples is in Task Manager
# ["test - Notepad"] This is the application sub/child name, an easy way to check for examples is in Task Manager clicking dropdown arrow
# hwndMain = win32gui.FindWindow("Notepad", "test - Notepad") this returns the main/parent Unique ID
import win32ui

hwnd = win32gui.FindWindow(None, "Roblox")
offset = (100, 100)

# hwnd = get_window_hwnd("Roblox")
print(hwnd)

# While(True) Will always run and continue to run indefinitely
while True:
    if win32api.GetAsyncKeyState(win32con.VK_CONTROL):
        print("Closed!")
        break
    if any(win32api.GetAsyncKeyState(i) for i in range(1, 255)):
        print("Continued")
        sleep(1)
        continue

    current_foreground_window = win32gui.GetForegroundWindow()

    # Set the target window as the foreground window
    try:
        win32gui.SetForegroundWindow(hwnd)
    except pywintypes.error:
        print("Could not set foreground window")

    # Get the coordinates of where you want to send the mouse click
    prev_mouse_pos = win32api.GetCursorPos()

    # Use the mouse_event function to simulate a mouse click
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
