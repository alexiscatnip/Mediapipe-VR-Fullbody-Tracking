from bin.Camera_Thread import CameraThread
from bin.logic.model import Model

print("Importing libraries....")

import os
import sys

sys.path.append(os.getcwd())    #embedable python doesnt find local modules without this line

from bin.view import camera_gui, inference_gui, UI
from bin.logic import parameters

import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

use_steamvr = True

# 1. get parameters from file
print("Reading parameters...")
params = parameters.load()

# 2. create computation model using params
model = Model(params)

# 3. open the main GUI: control-panel view
print("Opening control panel view...")
UI.start(model)

# 5. hopefully this call kills the threads.
model.exit()
