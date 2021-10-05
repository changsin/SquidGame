import threading
import time

import cv2
import yolov5

"""
A poor man's version of Red light-green light from Squid Game.
The correct translation of the game is actually "Mugunghwa (national flower of Korea) flowers blossomed"
The rule is also slightly different.
In red light-green light, "it" holds up either a green or red signal to control the players' movements.
In Mugunghwa game, the players are free to move while the "it" turns around and recite
"Mugunghwa flowers blossomed." After reciting is done, "it" faces the players and detects if anyone is moving.
If anyone moves during this time, he/she is eliminated (killed in the movie).

This version of the game is safe because it mimics the game in Python without killing the players.

"""
from playsound import playsound


def play(path):
    """
    Play sound file in a separate thread
    (don't block current thread)
    """
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print("Don't move")
        playsound(path)
        time.sleep(3)
    print("Stopping...")

    # play_thread = Thread(target=lambda: _playsound())
    # play_thread.start()

def detect_objects():
    model = yolov5.load('models/yolov5s.pt')

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    t = threading.Thread(target=play, args=(".\data\squid_mugunghwa.mp3",))
    t.start()

    while True:

        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        detected = model(frame)
        detected.save("results")

        cv2.imshow('Squid Game', detected.imgs[0])
        # cv2.imshow('input', frame)

        c = cv2.waitKey(1)
        # Press 'q' to quit
        if c == 113:
            break

    t.do_run = False

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_objects()
