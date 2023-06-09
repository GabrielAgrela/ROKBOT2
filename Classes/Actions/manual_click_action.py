import time
from Actions.action import Action
from manual_click import ManualClick
from window_handler import WindowHandler

class ManualClickAction(Action):
    def __init__(self,x=50,y=50, delay=0):
        self.manual_click = ManualClick()
        self.window_handler = WindowHandler()
        self.delay = delay
        self.window_title = 'Rise of Kingdoms'
        self.x = x
        self.y = y



    def execute(self):
        time.sleep(self.delay)
        self.manual_click.click(self.window_handler.get_window(self.window_title),self.x,self.y)
        return True
