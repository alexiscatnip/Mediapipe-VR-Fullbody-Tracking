# this thread outputs the data (tracker poses) to steamVR

from bin.logic.helpers import mediapipeTo3dpose, get_rot_mediapipe, get_rot_hands, draw_pose, keypoints_to_original, normalize_screen_coordinates, get_rot, sendToSteamVR

import time

class SteamVRThread:
    def __init__(self, model):
        # 1. initialise steamVR connection - keep looping until ok.
        self.model = model
        self.steamVR_found = False
        while not self.steamVR_found:
            self.connect_to_steamVR()

        self.totaltrackers = 3
        roles = ["TrackerRole_Waist", "TrackerRole_RightFoot", "TrackerRole_LeftFoot"]
        # 2. initialise our trackers in steamVR
        if self.use_steamvr:
            for i in range(self.numtrackers, self.totaltrackers):
                # adding a tracker into VR.
                resp = sendToSteamVR(f"addtracker MediaPipeTracker{i} {roles[i]}")
                while "error" in resp:
                    resp = sendToSteamVR(f"addtracker MediaPipeTracker{i} {roles[i]}")
                    print(resp)
                    time.sleep(0.2)
                time.sleep(0.2)

            params = {}
            params.smoothing = 0.1
            params.additional_smoothing = 0.1
            resp = sendToSteamVR(f"settings 50 {params.smoothing} {params.additional_smoothing}")
            print("settings returned this: ")
            print(resp)
            # while "error" in resp:
            #     resp = sendToSteamVR(f"settings 50 {params.smoothing} {params.additional_smoothing}")
            #     print(resp)
            #     time.sleep(1)

        # 3. send any incoming data:

    def connect_to_steamVR(self):
        if self.model.use_steamvr:
            print("Connecting to SteamVR...")

            # ask the driver, how many devices are connected to ensure we dont add additional trackers
            # if not, we try again
            self.numtrackers = sendToSteamVR("numtrackers")
            for i in range(10):
                if "error" in self.numtrackers:
                    print("Error in SteamVR connection. Retrying...")
                    time.sleep(1)
                    self.numtrackers = sendToSteamVR("numtrackers")
                else:
                    break

            if "error" in self.numtrackers:
                print("Could not connect to SteamVR after 10 retries!")
                print("Will sleep for 10s before trying to contact SteamVR again")
                time.sleep(10)

            self.numtrackers = int(self.numtrackers[2])
            self.steamVR_found = True
            print("connected to SteamVR")
