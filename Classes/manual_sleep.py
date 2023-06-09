import cv2
import numpy as np
import pyautogui

class ManualSleep:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def click(self, win, y_offset):
        #click middle of the screen with pyautogui
        center_x = int(win.width // 2 + win.left)
        center_y = int(win.height // 2 + win.top)
        pyautogui.click(center_x, center_y+y_offset)
