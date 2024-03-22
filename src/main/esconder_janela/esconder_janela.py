import win32gui
import win32console
import win32con

def hide_console_window():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, win32con.SW_HIDE)