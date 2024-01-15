import cv2
import pygetwindow
import numpy as np
import mediapipe as mp
import pyautogui
import threading
import time
from mss import mss

# Initialize MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to capture the game window
def capture_game_window():
    game_window = pygetwindow.getWindowsWithTitle("Counter-Strike: Global Offensive")[0]

    with mss() as sct:
        monitor = {"top": game_window.top, "left": game_window.left, "width": 400, "height": 400}
        game_frame = np.array(sct.grab(monitor))

    game_frame = cv2.cvtColor(game_frame, cv2.COLOR_BGR2RGB)
    return game_frame

# Detect key points of the enemy's head
def detect_enemy(image):
    results = pose.process(image)
    if results.pose_landmarks is not None:
        landmarks = results.pose_landmarks.landmark
        # Get the coordinates of the head key point
        head_x, head_y = int(landmarks[mp_pose.PoseLandmark.NOSE].x * image.shape[1]), int(landmarks[mp_pose.PoseLandmark.NOSE].y * image.shape[0])
        return head_x, head_y
    return None

# Rule: Click if the head is in the upper half of the screen
def should_click(head_position, screen_height):
    return head_position[1] < screen_height // 2

# Click thread
def click_thread():
    while True:
        game_frame = capture_game_window()

        # Get the enemy's head position
        enemy_position = detect_enemy(game_frame)

        # Click action if the enemy's head is detected (based on the rule)
        if enemy_position and should_click(enemy_position, game_frame.shape[0]):
            pyautogui.click(x=enemy_position[0], y=enemy_position[1])

        # Add other click logics here
        # ...

        # Delay for a certain time
        time.sleep(0.1)

# Start the click thread
click_thread = threading.Thread(target=click_thread)
click_thread.start()

# Main loop
with mp_pose.Pose() as pose:
    while True:
        game_frame = capture_game_window()

        # Get the enemy's head position
        enemy_position = detect_enemy(game_frame)

        # Click action if the enemy's head is detected
        if enemy_position:
            # Add precise click action here
            pass

        # Display the recognized game window
        cv2.imshow("Recognized Game Window", game_frame)

        # Wait for key events, delay 1 millisecond
        key = cv2.waitKey(1)

        # If the Esc key is pressed, exit the loop
        if key == 27:
            break
