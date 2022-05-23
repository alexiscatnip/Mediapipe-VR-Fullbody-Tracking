# model contains the parameters and the global variables and shared data.
import sys
import threading
import queue
from bin import cameraReader
from bin.logic import parameters, steamVR_thread


class Model():
    def __init__(self, params: dict):
        self.params = params

        # cameras
        self.cameras_feeds = [] # images from the camera threads
        self.camera_threads = [] # i keep track of the threads
        self.camera_src = []

        #inference thread

        #output to steamvr
        self.pipe_3d_points = queue
        self.steamVR_output_thread = steamVR_thread.SteamVRThread(
            self.pipe_3d_points
        )

    # spin up a camera thread and let it write the image to the array
    def add_a_camera_thread(self, src):
        idx = len(self.camera_threads)
        q = queue.Queue()

        self.camera_src.append(src)
        camera_thread_class = cameraReader.CameraThread(
            src,
            1920,
            1080,
            q
        )
        self.camera_threads.append(camera_thread_class)
        self.cameras_feeds.append(q) #does this work?
        print("appending camera" + str(len(self.cameras_feeds) -1))

        camera_thread_class.start()      #start our thread, which starts camera capture

    # update the path to the camera resource.
    # idx = thread id
    def set_camera_thread_src(self, idx, resource):
        cam_thread = self.camera_threads[idx]
        cam_thread.set_src(resource)

    #spin up extra camera threads if not enough
    def setCameraCount(self, count):
        self.params["camera_count"] = count
        parameters.save_params(self.params)

        while len(self.cam_thread) < count:
            self.add_a_camera_thread("")

    def getCameraCount(self):
        return self.params["camera_count"]

    #idx : index of camera in the camera array.
    def get_camera_image(self, idx):
        try:
            img = self.cameras_feeds[idx].get()
        except:
            print("error")

    def exit(self):
        #stores the model.param into the file.
        print("Saving parameters...")
        parameters.save_params(self.params)
        sys.exit()