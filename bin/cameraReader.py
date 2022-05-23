import queue
import time

import cv2

class CameraThread:
    def __init__(self, src, width, height, image_out_queue: queue):

        # global cameraid #image_from_thread, image_ready
        # self.cam_params = params[f"Camera_{cameraIdx}"]

        # cameraid = int(self.cam_params["cameraid"])
        self.cap = cv2.VideoCapture(src)
        # if "camera_height" in self.cam_params:

        # if "camera_width" in self.cam_params:
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        # self.isError = not cap.isOpened()
        # if (not self.isError):
        #     print("Camera opened!")
        self.image_out_queue = image_out_queue

    def start(self):
        self.isError = not self.cap.isOpened()
        if (self.isError):
            print("camera cap failed to open.")
            return
        while True:
            ret, img = self.cap.read()

            # image_ready = True

            assert ret, "Camera capture failed! Check the cameraid parameter."
            if (ret):
                self.image_out_queue.put(img)

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
