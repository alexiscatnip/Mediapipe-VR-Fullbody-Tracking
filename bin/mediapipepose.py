from bin.cameraReader import CameraThread
from bin.logic.model import Model

print("Importing libraries....")

import os
import sys

sys.path.append(os.getcwd())    #embedable python doesnt find local modules without this line

import time
import threading
import cv2
from bin.logic.helpers import mediapipeTo3dpose, get_rot_mediapipe, get_rot_hands, get_rot, sendToSteamVR
from scipy.spatial.transform import Rotation as R

from bin.view import camera_gui, inference_gui, controlpanel_gui
from bin.logic import parameters

import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

use_steamvr = True

# 1. get parameters
print("Reading parameters...")
params = parameters.load()

# 2. create model using params
model = Model(params)

# 3. open control-panel view
print("Opening control panel view...")
controlpanel_gui.windowOpen(model)

# we reach this line after the (above) control panel GUI is closed.

# 4. open the main inference app.
print("Opening main app view...")
inference_gui.windowOpen(model)

# 5. hopefully this call kills the threads.
model.exit()
