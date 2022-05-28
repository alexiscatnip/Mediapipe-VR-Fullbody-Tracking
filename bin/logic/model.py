# model contains the parameters and the global variables and shared data.
from collections import deque
import sys
from bin.api.SynchronisedCameraCapture import SynchronisedCameraCapture
from bin.logic import parameters, steamVR_thread, inference_thread, parameters_calibration


class Model():
    def __init__(self, params: dict):
        self.params = params
        self.inference_on = False
        self.triangulation_on = False
        self.steamVR_output_on = False

        # cameras
        self.image_streams = [] # images from the camera threads
        self.camera_src = [] # cameras's source path (as strings)
        self.sync_camera_cap_thread = SynchronisedCameraCapture(
            camera_sources = self.camera_src,
            image_streams = self.image_streams
        )

        #inference thread
        self.pipe_3d_points = deque(maxlen=1)
        self.steamVR_output_thread = inference_thread.InferenceAndTriangulationThread(
            input = self.image_streams,
            output = self.pipe_3d_points,
            cgroup = parameters_calibration.load_calib()
        )

        #output to steamvr
        self.steamVR_output_thread = steamVR_thread.SteamVRThread(
            self.pipe_3d_points
        )


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
            add_a_camera_thread(self.camera_threads, self.camera_src, self.cameras_feeds, "")

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