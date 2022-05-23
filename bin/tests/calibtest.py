# test for the calibration routine.
from aniposelib.cameras import CameraGroup

from bin.AniposeLibWrapper import define_board_parameters, do_calibration

import cv2

def image2video(imgs, width, height):
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
    out = cv2.VideoWriter("image2video.mp4", fourcc, 20.0, (width, height))

    for img in imgs:
        out.write(img) # Write out frame to video
    out.release()

if __name__ == "__main__":
    #1 check calibration can work.
    cam_names = ['A', 'B', 'C']
    vidnames = [['calib-charuco-camA-compressed.MOV'],
                ['calib-charuco-camB-compressed.MOV'],
                ['calib-charuco-camC-compressed.MOV']]

    board = define_board_parameters(6, 10)
    cgroup = CameraGroup.from_names(cam_names, fisheye=True)
    do_calibration(board, vidnames, cgroup)
    print(cgroup.dump('calibration.toml'))

    #2 check calibration loading can work.
    cgroup2 = CameraGroup.from_names(cam_names, fisheye=True)
    cgroup2 = CameraGroup.load('calibration.toml')
    print(cgroup2.dump('calibration2.toml'))

    #3 check that we can stitch images into videos.
    imgs_names = ["image/toast_1.PNG",
                  "image/toast_2.PNG"]
    imgs = []
    for img_name in imgs_names:
        img = cv2.imread(img_name)
        imgs.append(img)

    image2video(imgs, 1920, 1080)