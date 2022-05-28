# Wrap the aniposelib APIs.
import numpy as np
from aniposelib.boards import CharucoBoard, Checkerboard
from aniposelib.cameras import Camera, CameraGroup
from aniposelib.utils import load_pose2d_fnames

from aniposelib.boards import CharucoBoard


#region board_and_calib
def define_board_parameters(height, width, sq_len=25, marker_len=19, marker_bits=4, dict_size=50):
    board = CharucoBoard(height, width,
                         square_length=sq_len,  # here, in mm but any unit works
                         marker_length=marker_len,
                         marker_bits=marker_bits, dict_size=dict_size)
    return board

def do_calibration(board, vidnames, cgroup):
    try:
        cgroup.calibrate_videos(vidnames, board)
    except:
        print("calibration failed due to board is not detected in all cameras.")

def get_calibrated_cameras(cam_names):
    cgroup = CameraGroup.from_names(cam_names, fisheye=True)


#region triangulation
# p3ds_flat = cgroup.triangulate(points_flat, progress=True) # output shape = Nx3
# reprojerr_flat = cgroup.reprojection_error(p3ds_flat, points_flat, mean=True) # output shape = CxNx3