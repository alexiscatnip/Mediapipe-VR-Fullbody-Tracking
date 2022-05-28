# to load and save camera calibration to file.
from aniposelib.cameras import CameraGroup

def save_calib(cgroup):
    cgroup.dump('calibration.toml')

def load_calib():
    cgroup = CameraGroup.load('calibration.toml')
    return cgroup

if __name__ == "__main__":
    print("hehe")
