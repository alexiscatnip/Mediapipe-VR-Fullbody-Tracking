# test that opening the camera is OK.
# debug any problem in openCV webcam part.

import time
import os

os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2


def run():
    try:
        # cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # we set fourcc twice, since the earlier one might not take effect.
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        cap.set(cv2.CAP_PROP_FOURCC, fourcc)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
        # cap.set(cv2.CAP_PROP_EXPOSURE, 5)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)

        # we set fourcc at the end again.
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        cap.set(cv2.CAP_PROP_FOURCC, fourcc)

        time.sleep(0.4)

        prev_frame_time = 0
        while True:
            _, frame = cap.read()
            if _:
                new_frame_time = time.time()
                fps = 1 / (new_frame_time - prev_frame_time)
                prev_frame_time = new_frame_time
                fps = (str(fps))
                print(fps)
                dimensions = frame.shape
                print("height " + str(dimensions[0]))
                print("width " + str(dimensions[1]))

                cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
                cv2.imshow("Frame", frame)

                cv2.waitKey(1)


    except KeyboardInterrupt:
        print("stopped by ctrl-c")
        cap.release()
        return 0


if __name__ == "__main__":
    run()
