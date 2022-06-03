import cv2


def open_camera__windows(src):
    """
    open camera in windows OS.
    :return: the OpenCV 'capture' object
    """
    if len(src) <= 2:
        # case: webcam is referenced by "index"
        src = int(src)
    else :
        raise NotImplementedError

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
    return cap

# todo: delete these.
# self.cap.set(cv2.CAP_PROP_FPS, 30)
# print(str(self.cap.get(cv2.CAP_PROP_FPS)))
# self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# print(str(self.cap.get(cv2.CAP_PROP_AUTOFOCUS)))
# self.cap.set(cv2.CAP_PROP_FOCUS, 0)
# print(str(self.cap.get(cv2.CAP_PROP_FOCUS)))
