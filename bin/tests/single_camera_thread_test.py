# threaded variant of single_camera_DSHOW_test.py
# in other words: test that 'threaded camera' works for single camera.
import time
from bin.api.SynchronisedCameraCapture import SynchronisedCameraCapture
import cv2


def run(calibration_hz=150):
    # spin up cameras.
    camera_images = []
    caps = SynchronisedCameraCapture([], camera_images)
    print("spinning up camera...")
    caps.add_camera("1")

    time.sleep(2)

    print("spun up cameras :)")

    calibration_period = 1 / calibration_hz
    prev_frame_time = 0
    try:
        while True:
            # extract frame.
            images = caps.get_images_copy()

            # save frame to video.
            # only if all frames are present.
            if images[0] is not None:
                new_frame_time = time.time()
                fps = 1 / (new_frame_time - prev_frame_time)
                prev_frame_time = new_frame_time
                fps = str(fps)
                frame = cv2.resize(images[0], (500, 300))
                cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
                cv2.imshow("Frame", frame)
                cv2.waitKey(1)

            time.sleep(calibration_period)

    except KeyboardInterrupt:
        print("stopped by ctrl-c")
        caps.close()
        return 0


if __name__ == "__main__":
    run()
