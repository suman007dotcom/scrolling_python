class GestureDetector:
    def __init__(self):
        self.tip_ids = [4, 8, 12, 16, 20]

    def get_finger_states(self, lm_list):
        fingers = []
        if len(lm_list) == 0:
            return [0, 0, 0, 0, 0]

        if lm_list[self.tip_ids[0]][1] > lm_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)  # Thumb extended
        else:
            fingers.append(0)  # Thumb folded

        for id in range(1, 5):
            tip_y = lm_list[self.tip_ids[id]][2]
            pip_y = lm_list[self.tip_ids[id] - 2][2]

            if tip_y < pip_y:   
                fingers.append(1)  # Finger extended
            else:
                fingers.append(0)  # Finger folded

        return fingers  # Returns array like [0, 1, 0, 0, 0]

    def detect_gesture(self, lm_list):
        if len(lm_list) == 0:
            return "NONE"

        fingers = self.get_finger_states(lm_list)
        total_open = fingers.count(1)

        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            return "SCROLL_UP"

        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            return "SCROLL_DOWN"

        elif total_open >= 4:
            return "STOP"

        return "NONE"