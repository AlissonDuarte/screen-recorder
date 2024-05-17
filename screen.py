import cv2
import numpy as np
import pyautogui
import datetime
import uuid


# Setting the recording area
screen_width, screen_height = pyautogui.size()
fps = 20.0  # Frames per second

# Creating a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Generating a random UUID to add randomness to the filename
random_uuid = str(uuid.uuid4())[:8]  # Use the first 8 characters of the UUID

output_filename = "screen_record_{}_{}.avi".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), random_uuid)
output = cv2.VideoWriter(output_filename, fourcc, fps, (screen_width, screen_height))

# Recording the screen
print("Iniciando a gravação. Pressione Ctrl+C para parar.")
try:
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)
except KeyboardInterrupt:
    print("Gravação interrompida.")

# Freeing up resources
output.release()
print("Gravação salva como {}".format(output_filename))
