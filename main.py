import cv2
from hand_tracking import Hand_tracker
from gesture_detector import GestureDetector

def main():
    # cv2.VideoCapture(0) opens the default computer camera (webcam index 0)
    cap = cv2.VideoCapture(0)

    # Instantiate hand tracker and gesture detector objects
    tracker = Hand_tracker()
    detector = GestureDetector()

    print("Webcam starting... Press 'q' in the video window to quit.")

    while True:
        # Read a frame from webcam
        success, img = cap.read()
        if not success:
            print("Failed to access camera frame.")
            break

        # 1. Detect hands and draw landmarks on image
        img = tracker.find_hand(img)

        # 2. Get landmark pixel coordinates [[id, x, y], ...]
        lm_list = tracker.get_landmark_positions(img)

        # 3. Classify current hand gesture
        gesture = detector.detect_gesture(lm_list)

        # 4. Draw detected gesture text on video window (top-left at coordinates x=20, y=50)
        cv2.putText(
            img, 
            f"Gesture: {gesture}", 
            (20, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1.0, 
            (0, 255, 0), 
            2
        )

        # 5. Display frame in a pop-up window
        cv2.imshow("Gesture OS - Phase 2", img)

        # Exit loop when user presses 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up camera connection and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()