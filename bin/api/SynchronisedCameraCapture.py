from collections import deque
import numpy
from bin import Camera_Thread
from typing import List


class SynchronisedCameraCapture:
    """Just a wrapper class to encapsulate a bunch of camera threads."""

    def __init__(self, camera_sources: List[str], image_streams: List[deque]):
        """
        camera_sources : camera sources
        image_streams : camera output images. if you have 3 cameras, you have 3 deque's in here.
        """
        self.image_streams = image_streams
        self.camera_sources = camera_sources
        self.camera_threads: List[Camera_Thread] = []

        # open the desired cameras listed in @self.camera_sources
        for idx, cam_source in self.camera_sources:
            self.add_camera(cam_source)
        # assert (len(camera_sources) == 0) #todo. fixme

    def add_camera(self, camera_src: str):
        """spin up a camera thread and let it write the image to the array
        """
        image_stream = deque(maxlen=1)

        camera_thread = Camera_Thread.CameraThread(
            camera_src,
            1920,
            1080,
            image_stream
        )

        self.camera_threads.append(camera_thread)
        self.image_streams.append(image_stream)

        camera_thread.start()  # start camera capture

    def get_images_copy(self) -> List[numpy.array]:
        """
        get a COPY of the images in buffer.

        why copy?
            - because sequential read by-reference can result in reading from different frames
                    if even one of the cameras has an empty image buffer, that image will be a null.
        """
        images = []
        for idx, image_stream in enumerate(self.image_streams):
            image_ref = None  # ugly.
            # try:
            if len(image_stream) > 0:
                image_ref = image_stream.pop()
            # except IndexError:
            #     print(str(idx) + " camera has failed to get a frame")
            if image_ref is None:
                images.append(None)
            else:
                image = image_ref.copy()
                images.append(image)

        return images

    def get_camera_up(self, idx):
        """
        is camera x online?
        :param idx:
        :return:
        """
        try:
            result = self.camera_threads[idx].is_up()
            return result
        except Exception as e:
            print(str(e))

    def close(self):
        for cam_thread in self.camera_threads:
            print("closing camera thread...")
            cam_thread.release()
            cam_thread.join()


def get_camera_count(params):
    # todo: wtf is this?

    return params["camera_count"]
