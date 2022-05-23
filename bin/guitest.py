import tkinter as tk
import pickle
import cv2
from bin.logic.parameters import getparams


def openInitSettingsWindow():
    param = getparams()

    window = tk.Tk()

    tk.Label(text="Camera IP or ID:", width = 50).pack()
    camid = tk.Entry(width = 50)
    camid.pack()
    camid.insert(0,param["camid"])

    tk.Label(text="Maximum image size:", width = 50).pack()
    maximgsize = tk.Entry(width = 20)
    maximgsize.pack()
    maximgsize.insert(0,param["imgsize"])

    tk.Label(text="Offset of HMD to neck:", width = 50).pack()
    hmdoffsettext = tk.Entry(width = 50)
    hmdoffsettext.pack()
    hmdoffsettext.insert(0," ".join(map(str,param["neckoffset"])))
    
    tk.Label(text="Smoothing:", width = 50).pack()
    smoothingtext = tk.Entry(width = 50)
    smoothingtext.pack()
    smoothingtext.insert(0,param["smooth"])
    
    tk.Label(text="Camera latency:", width = 50).pack()
    camlatencytext = tk.Entry(width = 50)
    camlatencytext.pack()
    camlatencytext.insert(0,param["camlatency"])

    """
    varhmdwait = tk.IntVar(value = param["waithmd"])
    hmdwait_check = tk.Checkbutton(text = "Dont wait for hmd", variable = varhmdwait)
    hmdwait_check.pack()
    """
    
    varclock = tk.IntVar(value = param["rotateclock"])
    rot_clock_check = tk.Checkbutton(text = "Rotate camera clockwise", variable = varclock)
    rot_clock_check.pack()

    varcclock = tk.IntVar(value = param["rotatecclock"])
    rot_cclock_check = tk.Checkbutton(text = "Rotate camera counter clockwise", variable = varcclock)
    rot_cclock_check.pack()
    
    varfeet = tk.IntVar(value = param["feetrot"])
    rot_feet_check = tk.Checkbutton(text = "Enable experimental foot rotation", variable = varfeet)
    rot_feet_check.pack()
    
    varscale = tk.IntVar(value = param["calib_scale"])
    scale_check = tk.Checkbutton(text = "Enable automatic scale calibration", variable = varscale)
    scale_check.pack()
    
    vartilt = tk.IntVar(value = param["calib_tilt"])
    tilt_check = tk.Checkbutton(text = "Enable automatic tilt calibration", variable = vartilt)
    tilt_check.pack()
    
    varrot = tk.IntVar(value = param["calib_rot"])
    rot_check = tk.Checkbutton(text = "Enable automatic rotation calibration", variable = varrot)
    rot_check.pack()
    
    varhip = tk.IntVar(value = param["ignore_hip"])
    hip_check = tk.Checkbutton(text = "Don't use hip tracker", variable = varhip)
    hip_check.pack()
    
    tk.Label(text="-"*50, width = 50).pack()
    
    varhand = tk.IntVar(value = param["use_hands"])
    hand_check = tk.Checkbutton(text = "DEV: spawn trackers for hands", variable = varhand)
    hand_check.pack()
    
    varskel = tk.IntVar(value = param["prevskel"])
    skeleton_check = tk.Checkbutton(text = "Spawn trackers in front of you for preview purposes. DO NOT USE IN GAMES.", variable = varskel)
    skeleton_check.pack()

    tk.Button(text='Save and continue', command=window.quit).pack()

    window.mainloop()

    cameraid = camid.get()
    maximgsize = int(maximgsize.get())
    hmd_to_neck_offset = [float(val) for val in hmdoffsettext.get().split(" ")]
    preview_skeleton = bool(varskel.get())
    dont_wait_hmd = False #bool(varhmdwait.get()) 
    if varclock.get():
        if varcclock.get():
            rotate_image = cv2.ROTATE_180
        else:
            rotate_image = cv2.ROTATE_90_CLOCKWISE
    elif varcclock.get():
        rotate_image = cv2.ROTATE_90_COUNTERCLOCKWISE
    else:
        rotate_image = None
    camera_latency = float(camlatencytext.get())
    smoothing = float(smoothingtext.get())
    feet_rotation = bool(varfeet.get())
    calib_scale = bool(varscale.get())
    calib_tilt = bool(vartilt.get())
    calib_rot = bool(varrot.get())
    use_hands = bool(varhand.get())
    ignore_hip = bool(varhip.get())

    param = {}
    param["camid"] = cameraid
    param["imgsize"] = maximgsize
    param["neckoffset"] = hmd_to_neck_offset
    param["prevskel"] = preview_skeleton
    param["waithmd"] = dont_wait_hmd
    param["rotateclock"] = bool(varclock.get())
    param["rotatecclock"] = bool(varcclock.get())
    param["rotate"] = rotate_image
    param["smooth"] = smoothing
    param["camlatency"] = camera_latency
    param["feetrot"] = feet_rotation
    param["calib_scale"] = calib_scale
    param["calib_tilt"] = calib_tilt
    param["calib_rot"] = calib_rot
    param["use_hands"] = use_hands
    param["ignore_hip"] = ignore_hip
    
    pickle.dump(param,open("params.p","wb"))
    
    window.destroy()
    
    return param

if __name__ == "__main__":
    print(openInitSettingsWindow());
