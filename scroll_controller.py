import pyautogui
pyautogui.PAUSE = 0.0
class ScrollController:

    def __init__(self, scroll_speed=150):
        self.scroll_speed = scroll_speed
    def scroll_up(self):
        pyautogui.scroll(self.scroll_speed)
    def scroll_down(self):
        pyautogui.scroll(-self.scroll_speed)
    def process_gesture(self, gesture):
        if gesture == "SCROLL_UP":
            self.scroll_up()
        elif gesture == "SCROLL_DOWN":
            self.scroll_down()
        elif gesture == "STOP":
            # Open palm -> do nothing (pause scrolling)
            pass
        else:
            # 'NONE' or unhandled gestures -> do nothing
            pass
