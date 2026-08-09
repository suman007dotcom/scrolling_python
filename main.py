import cv2
from hand_tracking import Hand_tracker
from gesture_detector import GestureDetector
from scroll_controller import ScrollController

def main():
    # cv2.VideoCapture(0) opens the default computer camera (webcam index 0)
    cap = cv2.VideoCapture(0)

    # Instantiate hand tracker, gesture detector, and scroll controller with safety
    tracker = Hand_tracker()
    detector = GestureDetector()
    scroller = ScrollController(scroll_speed=150, scroll_cooldown=0.05)

    print("Webcam starting...")
    print("Controls:")
    print(" - Press 'e' in the video window to toggle ENABLE / DISABLE safety control")
    print(" - Press 'q' in the video window to quit")

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

        # 3. Classify current hand gesture ('SCROLL_UP', 'SCROLL_DOWN', 'STOP', 'NONE')
        gesture = detector.detect_gesture(lm_list)

        # 4. Perform OS scrolling (only executes if safety control is ENABLED)
        scroller.process_gesture(gesture)

        # 5. Draw detected gesture label on video window (top-left)
        cv2.putText(
            img, 
            f"Gesture: {gesture}", 
            (20, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1.0, 
            (0, 255, 0), 
            2
        )

        # 6. Draw Safety Status overlay (Green = ENABLED, Red = DISABLED)
        status_text = "System: ENABLED" if scroller.enabled else "System: DISABLED"
        status_color = (0, 255, 0) if scroller.enabled else (0, 0, 255)
        
        cv2.putText(
            img, 
            status_text, 
            (20, 90), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.8, 
            status_color, 
            2
        )

        # 7. Draw key control instructions at bottom of feed
        cv2.putText(
            img, 
            "Press 'e' to toggle safety | 'q' to quit", 
            (20, img.shape[0] - 20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.6, 
            (255, 255, 255), 
            1
        )

        # 8. Display frame in pop-up window
        cv2.imshow("Gesture OS - Phase 4 (Safety Controls)", img)

        # Keyboard event handling
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('e'):
            # Toggle safety enable/disable state when 'e' key is pressed
            new_state = scroller.toggle_control()
            print(f"Safety status toggled: {'ENABLED' if new_state else 'DISABLED'}")

    # Clean up camera connection and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()