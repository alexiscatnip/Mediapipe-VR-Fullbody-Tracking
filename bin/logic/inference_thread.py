# this thread outputs the data (tracker poses) to steamVR
from bin.api.MediapipeWrapper import MediapipeWrapper
from bin.logic.helpers import mediapipeTo3dpose, get_rot_mediapipe, get_rot_hands, draw_pose, keypoints_to_original, normalize_screen_coordinates, get_rot, sendToSteamVR

import time

# input: list of image queues (C * RGB, where C is camera count)
# output: list of detected 3D keypoints (N * 3D_transform, where N is number-of-keypoints of the human body)
class InferenceAndTriangulationThread:
    def __init__(self, input, output, cgroup):
        self.pose_detectors = self.init_inference_models(len(input))
        self.init_inference_models(len(input))
        self.cgroup = cgroup #calibrated camera group.

        self.image_local_buffer = [] # C * RGB
        self.detector_results = [] #C * 2D_vector

        self.triangulation_results = [] #N * 3D_vector

    def start(self):
        while True:
            # quickly copy each image from the queue into a local buffer;
            # - if inference takes long time, img1 and img3 will have many frames difference.
            for idx, img_queue in enumerate(input):
                image_in_queue = img_queue.pop()
                self.image_local_buffer[idx] = image_in_queue.copy()

            # do detections on the images.
            # todo: skip inference if the image is unchanged from previous.
            for idx, detector, img in enumerate(zip(self.pose_detectors, input)):
                self.detector_results[idx] = detector.process(img)

            #do triangulation
            p3ds_flat = self.cgroup.triangulate(self.detector_results, progress=True)
            reprojerr_flat = self.cgroup.reprojection_error(p3ds_flat, points_flat, mean=True)
            # print(reprojerr_flat)

            self.triangulation_results = p3ds_flat

    def init_inference_models(self, camera_count) -> list:
        print("Starting pose detectors ...")

        model_complexity = 2
        smooth_landmarks = True
        static_image = True
        min_tracking_confidence = 0.8
        min_detection_confidence = 0.5

        pose_detectors = []
        camera_count = 3

        for i in range(camera_count):
            pose_detector = MediapipeWrapper.create_pose_detector(
                model_complexity,
                min_detection_confidence,
                min_tracking_confidence,
                smooth_landmarks,
                static_image
            )
            pose_detectors.append(pose_detector)

        return pose_detectors