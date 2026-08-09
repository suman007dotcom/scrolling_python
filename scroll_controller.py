import pyautogui
import time

pyautogui.PAUSE = 0.0

class ScrollController:

    def __init__(self, scroll_speed=150, scroll_cooldown=0.05):
        self.scroll_speed = scroll_speed
        
        self.enabled = True
        
        self.scroll_cooldown = scroll_cooldown
        self.last_scroll_time = 0

    def toggle_control(self):
        self.enabled = not self.enabled
        return self.enabled

    def scroll_up(self):
        pyautogui.scroll(self.scroll_speed)

    def scroll_down(self):
        pyautogui.scroll(-self.scroll_speed)

    def process_gesture(self, gesture):
        if not self.enabled:
            return

        current_time = time.time()
        
        if current_time - self.last_scroll_time >= self.scroll_cooldown:
            if gesture == "SCROLL_UP":
                self.scroll_up()
                self.last_scroll_time = current_time
            elif gesture == "SCROLL_DOWN":
                self.scroll_down()
                self.last_scroll_time = current_time
            elif gesture == "STOP":
                pass  # Open palm -> pause scrolling
            else:
                pass  # 'NONE' or unrecognized gesture -> do nothing