import numpy as np
import tkinter as tk
from tkinter import ttk

from bin.api.SynchronisedCameraCapture import getCameraCount
from bin.logic import parameters
from PIL import Image
from PIL import ImageTk

use_steamvr = True

class CameraWindow(tk.Frame):
    def __init__(self, root, model, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        
        self.model = model
        self.root = root

        self.camera_src_entries = []
        self.fill_camera_src_from_model()

        tk.Label(self.root, text="Here you can set up and view your camera feed:").pack(side='top')
        self.put_separator()
        tk.Label(self.root, text="Total number of cameras: ").pack(side='top')
        self.camera_count = tk.IntVar(root, getCameraCount(model.params))
        self.cam_count_field = tk.Entry(self.root, width=50, textvariable=self.camera_count)
        self.cam_count_field.pack(side='top')
        tk.Button(self.root, text="Set number of cameras", command=self.set_camera_count).pack()
        self.put_separator()

        i = 0
        while i < self.camera_count.get():
            i += 1
            self.add_one_camera_gui(model, i)

        self.put_separator()
        tk.Button(self.root, text="Set the above camera parameters", command=self.set_camera).pack()

        # exit
        tk.Button(self.root, text='close', command=self.close).pack()

    def close(self):
        self.root.destroy()

    # append one camera view into the root/frame
    def add_one_camera_gui(self, model, camera_index):
        tk.Label(self.root, text="Camera IP or ID:", width=50).pack()

        self.camera_src_entries.append()

        self.camera_src[camera_index] = tk.Entry(self.root, width=50, )
        self.camera_src[camera_index].pack()

        if (camid.get().strip() == "") or camid.get() is None:
            print("not adding the camera as it is null stirng")
            pass
        else:
            add_a_camera_thread(model.camera_threads, model.camera_src, model.cameras_feeds, model.params[camera_index])

        #create panel for show_frames
        self.image_label = tk.Label(self.root)
        self.image_label.pack(side="top")
        self.show_frames()

    # shows the initial frame of img, then updates it every X ms
    def show_frames(self):
        # image = np.full((200, 200), 255, dtype=np.uint8)

        image = self.model.get_camera_image(0)
        if (image == None):
            err_image = Image.open('cam_error.png')
            imgtk = ImageTk.PhotoImage(err_image)
            self.image_label.configure(image=imgtk)
            self.image_label.image =imgtk
            return

        else :
            image = Image.fromarray(image)
            # ...and then to ImageTk format
            imgtk = ImageTk.PhotoImage(image)


            # label = tk.Label(self)
            # label.imgtk = imgtk
            self.image_label.configure(image=imgtk)
            # Repeat after an interval to capture continiously
            self.root.after(20, self.show_frames)

    def change_neck_offset_frame(self,frame):
        tk.Label(frame, text="HMD to neck offset:", width = 20).pack(side='left')
        
        text1 = tk.Entry(frame, width = 5)
        text1.pack(side='left')
        text1.insert(0, self.params.hmd_to_neck_offset[0])
        
        text2 = tk.Entry(frame, width = 5)
        text2.pack(side='left')
        text2.insert(0, self.params.hmd_to_neck_offset[1])
        
        text3 = tk.Entry(frame, width = 5)
        text3.pack(side='left')
        text3.insert(0, self.params.hmd_to_neck_offset[2])

        tk.Button(frame, text='Update', command=lambda *args: self.params.change_neck_offset(float(text1.get()),float(text2.get()),float(text3.get()))).pack(side='left')


    def set_camera_count(self):
        self.model.setCameraCount(self.cam_count_field.get())

    def put_separator(self): 
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.pack(fill='x')

    def set_camera(self):
        #read the fields and set in the model.


        for idx, src in enumerate(self.model.camera_src):
            self.model.set_camera_thread_src(idx, src)

    def CameraConfig(self):
        self.root.destroy()

    def fill_camera_src_from_model(self):
        # count = self.model.getCameraCount()
        # for x in range(count):
        #     camera_src_entries = self.model.camera_src[x]
        self.camera_src_entries = self.model.camera_src



# def launchGUIandBlock(_params):
#     CameraWindow(root, params).pack(side="top", fill="both", expand=True)
#
#     root.mainloop()

if __name__ == "__main__":
    # launchGUIandBlock(parameters.load())
    print("hehe")


