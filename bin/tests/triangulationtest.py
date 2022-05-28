# test if triangulation on the calibrated cameras yield an acceptable reprojection error
import numpy as np
from aniposelib.cameras import CameraGroup
from aniposelib.utils import load_pose2d_fnames

from bin.api.AniposeLibWrapper import define_board_parameters

if __name__ == "__main__":

    cam_names = ['A', 'B', 'C']
    vidnames = [['calib-charuco-camA-compressed.MOV'],
                ['calib-charuco-camB-compressed.MOV'],
                ['calib-charuco-camC-compressed.MOV']]

    board = define_board_parameters(6, 10)

    # 2 check calibration loading can work.
    cgroup = CameraGroup.from_names(cam_names, fisheye=True)
    cgroup = CameraGroup.load('calibration.toml')




    fname_dict = {
        'A': '2019-08-02-vid01-camA.h5',
        'B': '2019-08-02-vid01-camB.h5',
        'C': '2019-08-02-vid01-camC.h5',
    }

    d = load_pose2d_fnames(fname_dict, cam_names=cgroup.get_names())

    score_threshold = 0.5

    n_cams, n_points, n_joints, _ = d['points'].shape
    points = d['points']
    scores = d['scores']

    bodyparts = d['bodyparts']

    # remove points that are below threshold
    points[scores < score_threshold] = np.nan

    points_flat = points.reshape(n_cams, -1, 2)
    scores_flat = scores.reshape(n_cams, -1)

    p3ds_flat = cgroup.triangulate(points_flat, progress=True)
    reprojerr_flat = cgroup.reprojection_error(p3ds_flat, points_flat, mean=True)

    p3ds = p3ds_flat.reshape(n_points, n_joints, 3)
    reprojerr = reprojerr_flat.reshape(n_points, n_joints)

    print(reprojerr)
    print("median of reprojerr : ", np.median(reprojerr))
