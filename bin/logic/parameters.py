# Module to load and save parameters from JSON file

from scipy.spatial.transform import Rotation as R
import json

def load() -> dict:
    # param = None
    param = load_params()
    return param


def change_recalibrate(self):
    self.recalibrate = True


def rot_change_y(self, value):                                  #callback functions. Whenever the value on sliders are changed, they are called
    print(f"Changed y rotation value to {value}")
    self.euler_rot_y = value
    self.global_rot_y = R.from_euler('y',value,degrees=True)     #and the rotation is updated with the new value.


def rot_change_x(self, value):
    print(f"Changed x rotation value to {value}")
    self.euler_rot_x = value
    self.global_rot_x = R.from_euler('x',value-90,degrees=True)

def rot_change_z(self, value):
    print(f"Changed z rotation value to {value}")
    self.euler_rot_z = value
    self.global_rot_z = R.from_euler('z',value-180,degrees=True)


def change_scale(self, value):
    print(f"Changed scale value to {value}")
    #posescale = value/50 + 0.5
    self.posescale = value


def change_img_rot(self, val):
    print(f"Changed image rotation to {val*90} clockwise")
    self.rotate_image = self.img_rot_dict[val]


def change_smoothing(self, val, paramid = 0):
    print(f"Changed smoothing value to {val}")
    self.smoothing = val

    if paramid == 1:
        self.smoothing_1 = val
    if paramid == 2:
        self.smoothing_2 = val

def change_additional_smoothing(self, val, paramid = 0):
    print(f"Changed additional smoothing value to {val}")
    self.additional_smoothing = val

    if paramid == 1:
        self.additional_smoothing_1 = val
    if paramid == 2:
        self.additional_smoothing_2 = val

def change_camera_latency(self, val):
    print(f"Changed camera latency to {val}")
    self.camera_latency = val

def change_neck_offset(self,x,y,z):
    print(f"Hmd to neck offset changed to: [{x},{y},{z}]")
    self.hmd_to_neck_offset = [x,y,z]

def change_mirror(self, mirror):
    print(f"Image mirror set to {mirror}")
    self.mirror = mirror

def ready2exit(self):
    self.exit_ready = True

def initparams(param):
    if "neckoffset" not in param:
        param["neckoffset"] = [0.0, -0.2, 0.1]
    if "prevskel" not in param:
        param["prevskel"] = False
    if "waithmd" not in param:
        param["waithmd"] = False
    if "rotateclock" not in param:
        param["rotateclock"] = False
    if "rotatecclock" not in param:
        param["rotatecclock"] = False
    if "rotate" not in param:
        param["rotate"] = None
    if "camlatency" not in param:
        param["camlatency"] = 0.05
    if "smooth" not in param:
        param["smooth"] = 0.5
    if "feetrot" not in param:
        param["feetrot"] = False
    if "calib_scale" not in param:
        param["calib_scale"] = True
    if "calib_tilt" not in param:
        param["calib_tilt"] = True
    if "calib_rot" not in param:
        param["calib_rot"] = True
    if "use_hands" not in param:
        param["use_hands"] = False
    if "ignore_hip" not in param:
        param["ignore_hip"] = False
    if "model_complexity" not in param:
        param["model_complexity"] = 1
    if "smooth_landmarks" not in param:
        param["smooth_landmarks"] = True
    if "min_tracking_confidence" not in param:
        param["min_tracking_confidence"] = 0.5
    if "static_image" not in param:
        param["static_image"] = False
    if "advanced" not in param:
        param["advanced"] = False
    if "imgsize" not in param:
        param["imgsize"] = 640
    if "camid0" not in param:
        param["camid0"] = 'http://192.168.1.103:8080/video'
    if "camid1" not in param:
        param["camid1"] = ''
    if "camid2" not in param:
        param["camid2"] = ''
    if "camid3" not in param:
        param["camid3"] = ''
    if "camera_count" not in param:
        param["camera_count"] = 2
    # return param

def save_params(param):
    # param = {}

    with open("../saved_params.json", "w") as f:
        json.dump(param, f)

def load_params():
    try:
        with open("../saved_params.json", "r") as f:
            param = json.load(f)

        #print(param["roty"])
        #
        # self.rotate_image = self.img_rot_dict[param["rotate"]]
        # self.smoothing_1 = param["smooth1"]
        # self.smoothing_2 = param["smooth2"]
        # self.camera_latency = param["camlatency"]
        # self.additional_smoothing_1 = param["addsmooth1"]
        # self.additional_smoothing_2 = param["addsmooth2"]
        #
        # self.euler_rot_y = param["roty"]
        # self.euler_rot_x = param["rotx"]
        # self.euler_rot_z = param["rotz"]
        # self.posescale = param["scale"]
        #
        # self.calib_rot = param["calibrot"]
        # self.calib_tilt = param["calibtilt"]
        # self.calib_scale = param["calibscale"]
        #
        # self.mirror = param["mirror"]
        #
        # if self.advanced:
        #     self.hmd_to_neck_offset = param["hmd_to_neck_offset"]
        #
        # self.flip = param["flip"]
    except:
        print("Save file not found, will use default values.")
        param = {}
        initparams(param)
    finally:
        return param

if __name__ == "__main__":
    param = load()
    print(param)
    save_params(param)
    print("hehe")
#
#
# def getparams():
#     try:
#         param = pickle.load(open("params_camera.p","rb"))
#     except:
#         param = {}
#
#     initparams(param)
#
#     return param
#

