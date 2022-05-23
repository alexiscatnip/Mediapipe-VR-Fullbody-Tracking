from bin.logic.parameters import getparams


def set_advanced(window,param):
    param["switch_advanced"] = True
    window.quit()

# provide default values to param, if not existing

# use pickle to get parameters from file.
# if a parameter is not defined, initparams will fill a default value.
#
# def gui_stuff():
#     window = tk.Tk()
#
#     tk.Label(text="Camera IP or ID:", width = 50).pack()
#     camid = tk.Entry(width = 50)
#     camid.pack()
#     camid.insert(0,param["camid"])
#
#     tk.Button(text='add one more camera', command=lambda *args: add_camera(window, param)).pack()
#
#     if not param["advanced"]:
#         tk.Label(text="NOTE: Increasing resolution may decrease performance.\n Unless you have problems with opening camera, leave it at default.", width = 50).pack()
#
#     tk.Label(text="Camera width:", width = 50).pack()
#     camwidth = tk.Entry(width = 20)
#     camwidth.pack()
#     camwidth.insert(0,param["camera_width"])
#
#     tk.Label(text="Camera height:", width = 50).pack()
#     camheight = tk.Entry(width = 20)
#     camheight.pack()
#     camheight.insert(0,param["camera_height"])
#
#     if not param["advanced"]:
#         tk.Label(text="NOTE: Opening camera settings may change camera behaviour. \nSome cameras may only work with this enabled, some only with this \ndisabled, and it may change which camera ID you have to use.", width = 55).pack()
#
#     varcamsettings = tk.IntVar(value = param["camera_settings"])
#     cam_settings_check = tk.Checkbutton(text = "Attempt to open camera settings", variable = varcamsettings)
#     cam_settings_check.pack()
#
#     if param["advanced"]:
#         tk.Label(text="Maximum image size:", width = 50).pack()
#         maximgsize = tk.Entry(width = 20)
#         maximgsize.pack()
#         maximgsize.insert(0,param["imgsize"])
#
#     tk.Label(text="-"*50, width = 50).pack()
#
#     if True:
#
#         tk.Label(text="Offset of HMD to neck:", width = 50).pack()
#         hmdoffsettext = tk.Entry(width = 50)
#         hmdoffsettext.pack()
#         hmdoffsettext.insert(0," ".join(map(str,param["neckoffset"])))
#
#     if True:
#         tk.Label(text="Smoothing:", width = 50).pack()
#         smoothingtext = tk.Entry(width = 50)
#         smoothingtext.pack()
#         smoothingtext.insert(0,param["smooth"])
#
#         tk.Label(text="Camera latency:", width = 50).pack()
#         camlatencytext = tk.Entry(width = 50)
#         camlatencytext.pack()
#         camlatencytext.insert(0,param["camlatency"])
#
#     """
#     varhmdwait = tk.IntVar(value = param["waithmd"])
#     hmdwait_check = tk.Checkbutton(text = "Dont wait for hmd", variable = varhmdwait)
#     hmdwait_check.pack()
#     """
#     if True:
#         varclock = tk.IntVar(value = param["rotateclock"])
#         rot_clock_check = tk.Checkbutton(text = "Rotate camera clockwise", variable = varclock)
#         rot_clock_check.pack()
#
#         varcclock = tk.IntVar(value = param["rotatecclock"])
#         rot_cclock_check = tk.Checkbutton(text = "Rotate camera counter clockwise", variable = varcclock)
#         rot_cclock_check.pack()
#
#     varfeet = tk.IntVar(value = param["feetrot"])
#     rot_feet_check = tk.Checkbutton(text = "Enable experimental foot rotation", variable = varfeet)
#     rot_feet_check.pack()
#
#     if True:
#
#         varscale = tk.IntVar(value = param["calib_scale"])
#         scale_check = tk.Checkbutton(text = "Enable automatic scale calibration", variable = varscale)
#         scale_check.pack()
#
#         vartilt = tk.IntVar(value = param["calib_tilt"])
#         tilt_check = tk.Checkbutton(text = "Enable automatic tilt calibration", variable = vartilt)
#         tilt_check.pack()
#
#         varrot = tk.IntVar(value = param["calib_rot"])
#         rot_check = tk.Checkbutton(text = "Enable automatic rotation calibration", variable = varrot)
#         rot_check.pack()
#
#     if not param["advanced"]:
#         tk.Label(text="NOTE: VRChat requires a hip tracker. Only disable it if you \nuse another software for hip tracking, such as  owoTrack.", width = 55).pack()
#
#     varhip = tk.IntVar(value = param["ignore_hip"])
#     hip_check = tk.Checkbutton(text = "Disable hip tracker", variable = varhip)
#     hip_check.pack()
#
#     tk.Label(text="-"*50, width = 50).pack()
#
#     if param["advanced"]:
#
#         varhand = tk.IntVar(value = param["use_hands"])
#         hand_check = tk.Checkbutton(text = "DEV: spawn trackers for hands", variable = varhand)
#         hand_check.pack()
#
#         varskel = tk.IntVar(value = param["prevskel"])
#         skeleton_check = tk.Checkbutton(text = "DEV: preview skeleton in VR", variable = varskel)
#         skeleton_check.pack()
#
#         tk.Label(text="-"*50, width = 50).pack()
#
#         tk.Label(text="[ADVANCED] MediaPipe estimator parameters:", width = 50).pack()
#
#         tk.Label(text="Model complexity:", width = 50).pack()
#         modelc = tk.Entry(width = 20)
#         modelc.pack()
#         modelc.insert(0,param["model_complexity"])
#
#         varmsmooth = tk.IntVar(value = param["smooth_landmarks"])
#         msmooth_check = tk.Checkbutton(text = "Smooth landmarks", variable = varmsmooth)
#         msmooth_check.pack()
#
#         tk.Label(text="Min tracking confidence:", width = 50).pack()
#         trackc = tk.Entry(width = 20)
#         trackc.pack()
#         trackc.insert(0,param["min_tracking_confidence"])
#
#         varstatic = tk.IntVar(value = param["static_image"])
#         static_check = tk.Checkbutton(text = "Static image mode", variable = varstatic)
#         static_check.pack()
#
#     param["switch_advanced"] = False
#     if param["advanced"]:
#         tk.Label(text="-"*50, width = 50).pack()
#         tk.Button(text='Disable advanced mode', command=lambda *args: set_advanced(window,param)).pack()
#     else:
#         tk.Button(text='Enable advanced mode', command=lambda *args: set_advanced(window,param)).pack()
#
#     tk.Button(text='Save and continue', command=window.quit).pack()
#
#     window.mainloop()
#
#     cameraid = camid.get()
#     #hmd_to_neck_offset = [float(val) for val in hmdoffsettext.get().split(" ")]
#
#     dont_wait_hmd = False #bool(varhmdwait.get())
#
#     #camera_latency = float(camlatencytext.get())
#     #smoothing = float(smoothingtext.get())
#     feet_rotation = bool(varfeet.get())
#
#     ignore_hip = bool(varhip.get())
#     camera_settings = bool(varcamsettings.get())
#     camera_height = camheight.get()
#     camera_width = camwidth.get()
#
#     if param["advanced"]:
#         maximgsize = int(maximgsize.get())
#
#         preview_skeleton = bool(varskel.get())
#         use_hands = bool(varhand.get())
#
#         mp_smoothing = bool(varmsmooth.get())
#         model_complexity = int(modelc.get())
#         min_tracking_confidence = float(trackc.get())
#         static_image = bool(varstatic.get())
#     else:
#         maximgsize = 640
#
#         preview_skeleton = False
#         use_hands = False
#
#         mp_smoothing = True
#         model_complexity = 1
#         min_tracking_confidence = 0.5
#         static_image = False
#
#     switch_advanced = param["switch_advanced"]
#
#     advanced = param["advanced"]
#
#     param = {}
#     param["camid"] = cameraid
#     param["imgsize"] = maximgsize
#     #param["neckoffset"] = hmd_to_neck_offset
#     param["prevskel"] = preview_skeleton
#     param["waithmd"] = dont_wait_hmd
#
#     #param["smooth"] = smoothing
#     #param["camlatency"] = camera_latency
#     param["feetrot"] = feet_rotation
#     param["use_hands"] = use_hands
#     param["ignore_hip"] = ignore_hip
#
#     param["camera_settings"] = camera_settings
#     param["camera_height"] = camera_height
#     param["camera_width"] = camera_width
#
#     param["model_complexity"] = model_complexity
#     param["smooth_landmarks"] = mp_smoothing
#     param["static_image"] = static_image
#     param["min_tracking_confidence"] = min_tracking_confidence
#
#     if switch_advanced:
#         param["advanced"] = not advanced
#     else:
#         param["advanced"] = advanced
#
#     pickle.dump(param,open("params.p","wb"))
#
#     window.destroy()
#
#     if switch_advanced:
#         return None
#     else:
#         return param

if __name__ == "__main__":
    print(getparams())
