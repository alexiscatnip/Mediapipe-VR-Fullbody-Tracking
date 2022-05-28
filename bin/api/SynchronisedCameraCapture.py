from collections import deque
from bin import Camera_Thread

class SynchronisedCameraCapture:
    """Just a wrapper class to encapsulate a bunch of camera threads."""

    # camera_sources : list of each cameras's source path (strings)
    # image_streams : list of deques' of camera

    def __init__(self, camera_sources, image_streams):
        self.image_streams = image_streams
        self.camera_sources = camera_sources

        self.camera_threads = []

        # open the desired cameras listed in @self.camera_sources
        for idx, cam_source in self.camera_sources:
            self.add_camera(cam_source)
        # assert (len(camera_sources) == 0) #todo. fixme

    def add_camera(self, camera_src):
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

        camera_thread.start()      #start camera capture

    def get_images_copy(self):
        """
        obtain a COPY of the images in the current instance
        need COPY - because sequential read by-reference can result in reading from different frames
        """
        images = []
        for image_stream in self.image_streams:
            image_ref = image_stream.pop()
            if image_ref is None:
                images.append(None)
                continue
            image = image_ref.copy()
            images.append(image)

        return images


def getCameraCount(params):
    return params["camera_count"]