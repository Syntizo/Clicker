# Counter-Strike: Global Offensive Pose Recognition and Clicker

Automate enemy detection and clicking in Counter-Strike: Global Offensive using Python and MediaPipe Pose.

## Features

- **Pose Detection:** Utilizes MediaPipe Pose to detect enemy positions based on their body posture.
- **Automatic Clicking:** Performs automatic clicks on enemies, following predefined rules.
- **Configurability:** Easily configurable rules to define when to click based on enemy pose.
- **Window Capture:** Uses MSS for efficient screen capturing with configurable window size.

## Requirements

- Python 3
- OpenCV
- PyGetWindow
- NumPy
- Mediapipe
- PyAutoGUI
- MSS (Screen Capture Library)

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Clicker.git


# 2. Navigate to the project directory:
cd Clicker


# 3. Run the script:
python Clicker.py


Configuration:
Customize the rules in the should_click function in main.py. Adjust the window size in the capture_game_window function if needed.

Notes:
Ensure Counter-Strike: Global Offensive is running and visible. Adjust the window title in capture_game_window based on your game window title.




