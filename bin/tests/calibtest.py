# test for the calibration routine.
from aniposelib.cameras import CameraGroup
from bin.api.AniposeLibWrapper import define_board_parameters, do_calibration

if __name__ == "__main__":
    #1 check calibration from videos can work.
    cam_names = ['A', 'B', 'C']
    vidnames = [['calibration1.avi'],
                ['calibration2.avi'],
                ['calibration3.avi']]

    board = define_board_parameters(11, 15, 15, 12, dict_size = 250)
    cgroup = CameraGroup.from_names(cam_names, fisheye=False)
    do_calibration(board, vidnames, cgroup)
    cgroup.dump('calibration.toml')
    assert 0


    #2 check calibration loading can work.
    cgroup2 = CameraGroup.from_names(cam_names, fisheye=True)
    cgroup2 = CameraGroup.load('calibration.toml')
    print(cgroup2.dump('calibration2.toml'))

