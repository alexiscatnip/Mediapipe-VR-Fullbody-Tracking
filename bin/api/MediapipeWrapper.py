import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class MediapipeWrapper:
    def __init__(self):
        pass



def create_pose_detector(
                         model_complexity,
                         min_detection_confidence,
                         min_tracking_confidence,
                         smooth_landmarks,
                         static_image
                         ):
    pose1 = mp_pose.Pose(                #create our detector. These are default parameters as used in the tutorial.
        model_complexity=model_complexity,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
        smooth_landmarks=smooth_landmarks,
        static_image_mode=static_image)
    return pose1