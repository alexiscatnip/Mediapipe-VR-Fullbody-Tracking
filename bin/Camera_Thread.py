import threading
import time
from collections import deque
import cv2

class CameraThread(threading.Thread):
    def __init__(self, src, width: int, height: int, image_out_queue: deque):
        threading.Thread.__init__(self)

        if len(src) <= 2:
            #handle case of webcam referenced by its integer index
            src = int(src)
            self.cap = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        else :
            raise NotImplementedError
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        # self.isError = not cap.isOpened()
        # if (not self.isError):
        #     print("Camera opened!")
        self.image_out_queue = image_out_queue

        print("opened camera with width " + str(self.cap.get(3)) +
              " height " + str(self.cap.get(4)))

    def run(self):
        self.isError = not self.cap.isOpened()
        if self.isError:
            print("camera cap failed to open.")
            return
        while True:
            ret, img = self.cap.read()

            assert ret, "Camera capture failed! Check the cameraid parameter."
            #todo: time.sleep(.01) for assert failed case.
            if ret:
                self.image_out_queue.append(img)
                time.sleep(.01)

    def set_src(self, src, width, height):
        if (self.cap is not None):
            self.cap.release()

        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

        self.start()
        # if "camera_height" in self.cam_params:
        #     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.cam_params["camera_height"]))
        #
        # if "camera_width" in self.cam_params:
        #     cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.cam_params["camera_width"]))
        # self.isError = not cap.isOpened()
        # if (not self.isError):
        #     print("Camera opened!")
