import cv2
import mediapipe as mp


class Hand_tracker:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):        
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_hand(self,img,draw = True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    # Draw the 21 landmark points and connecting lines onto the original frame
                    self.mp_draw.draw_landmarks(
                        img, 
                        hand_lms, 
                        self.mp_hands.HAND_CONNECTIONS
                    )
        return img

    def get_landmark_positions(self, img, hand_no=0):

        lm_list = []
        
        if self.results and self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) > hand_no:
                my_hand = self.results.multi_hand_landmarks[hand_no]
                
                h, w, c = img.shape
                
                for lm_id, lm in enumerate(my_hand.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([lm_id, cx, cy])
                    
        return lm_list