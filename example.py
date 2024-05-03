"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import webbrowser
import pikachu
import cv2
from dice import roll_dice_game
from gaze_tracking import GazeTracking


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""
    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
        #drawing = pikachu.Draw_Pikachu()
        #drawing.start()
    elif gaze.is_left():
        text = "Looking left"
        roll_dice_game()
    elif gaze.is_up():
        text = "Looking sus"
        #url_to_open = 'https://etti.utcluj.ro/acasa.html'  # Replace with the URL you want to open
        #webbrowser.open(url_to_open)
    elif gaze.is_down():
        text = "Looking jos"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()