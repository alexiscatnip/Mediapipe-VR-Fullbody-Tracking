"""
test :
    1. we can open up the SynchronisedCameras,
    2. take the images,
    3. and finally write them to .avi files.
"""
import time
from bin.api.SynchronisedCameraCapture import SynchronisedCameraCapture
import cv2

def synchronised_camera_capture_to_files(calibration_hz: int):
    """
    :param calibration_hz: the rate at which to pull the images from the cameras.
                            I set it to half of camera FPS.
    :return:
    """

    # spin up cameras.
    camera_images = []
    caps = SynchronisedCameraCapture([], camera_images)
    print("spinning up camera 0...")
    caps.add_camera("0")
    print("spinning up camera 1...")
    caps.add_camera("1")
    print("spinning up camera 2...")
    caps.add_camera("2")

    time.sleep(2)  # wait 2 seconds for cameras to turn on.

    camera_up = caps.get_camera_up(0) and \
                caps.get_camera_up(1) and \
                caps.get_camera_up(2)
    if not camera_up:
        print("failed to open one of the cameras")
        return -1

    print("spun up cameras :)")

    assert len(camera_images) == 3, "there should be 3 camera image streams"

    fmt = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
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
    calibration_period = 1 / calibration_hz
    try:
        while True:
            # extract frame.
            images = caps.get_images_copy()

            # if all cameras give image, then save them.
            # otherwise, don't save any image for this frame.
            if all(image is not None for image in images):
                video_writer1.write(images[0])
                video_writer2.write(images[1])
                video_writer3.write(images[2])
                print("written 1 frame to file.")
            time.sleep(calibration_period)

    except KeyboardInterrupt:
        print("stopped by ctrl-c")
        caps.close()
        return 0


if __name__ == "__main__":
    synchronised_camera_capture_to_files(15)
