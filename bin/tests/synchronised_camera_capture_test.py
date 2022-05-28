# code routines, where we take a video from camer images with the frames synced up.
# for the purpose of intrinsic and extrinsic calibration.
import time

from bin.api.SynchronisedCameraCapture import SynchronisedCameraCapture
import cv2

# 1. spins up the cameras.
# 2. extracts the latest frames from the cameras at a fixed HZ
# 3. save the final frames into videos - one file for each camera


def synchronised_camera_capture_to_files(camera_count, calibration_period=0.1):
    """
    :param camera_count: duh.
    :param calibration_period: time between each synchronised capture.
            It is long by default, because the calibration takes a long time to process many frames.
    :return:
    """

    #spin up cameras.
    camera_images = []
    caps = SynchronisedCameraCapture([], camera_images)
    print("spinning up camera...")
    caps.add_camera("0")
    print("spinning up camera...")
    caps.add_camera("1")
    print("spinning up camera...")
    caps.add_camera("2")
    print("spun up cameras :)")

    assert(len(camera_images) == 3)

    fmt = cv2.VideoWriter_fourcc('M','J','P','G')
    frame_width = 1920
    frame_height = 1080
    frame_size = (frame_width, frame_height)
    video_writer1 = cv2.VideoWriter('calibration1.avi',
                                    fmt,
                                    1,
                                    frame_size)
    video_writer2 = cv2.VideoWriter('calibration2.avi',
                                    fmt,
                                    1,
                                    frame_size)
    video_writer3 = cv2.VideoWriter('calibration3.avi',
                                    fmt,
                                    1,
                                    frame_size)

    while True:
        # extract frame.
        try:
            images = caps.get_images_copy()
        except IndexError:
            continue

        # save frame to video.
        video_writer1.write(images[0])
        video_writer2.write(images[1])
        video_writer3.write(images[2])

        print("written 1 frame to file.")

        time.sleep(calibration_period)



if __name__ == "__main__":
    try:
        synchronised_camera_capture_to_files(3)
    except:
        pass