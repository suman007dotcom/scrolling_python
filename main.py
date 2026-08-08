import cv2
from hand_tracking import Hand_tracker

def main():
    # 1. Open webcam 0 (default system camera)
    cap = cv2.VideoCapture(0)

    # 2. Create HandTracker object instance
    tracker = Hand_tracker()

    print("Webcam starting... Press 'q' in the video window to quit.")

    while True:
        # 3. Read camera frame
        success, img = cap.read()
        if not success:
            print("Failed to access camera frame.")
            break

        # 4. Process frame with hand tracker
        img = tracker.find_hand(img)

        # 5. Display frame in a GUI window
        cv2.imshow("Gesture OS - Hand Detection", img)

        # 6. Check for exit key ('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 7. Release webcam and close window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()