# calibration routine, where the user can hold up the chessboard in sync with TTS.
from bin.view.Calibration import CalibrationStart

import tkinter as tk
from tkinter import ttk


class ChooseCameraStart(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 100)

        self.label = ttk.Label(self, text="Let's choose your cameras")
        self.label.pack()

        self.cameraname = ttk.Entry(self)
        self.cameraname.pack()

        self.button = ttk.Button(self, text="This is my camera", command=self.GetCamera)
        self.button.pack(side="top")

        self.skip = ttk.Button(self, text="Use saved cameras from previous run", command=self.Skip)
        self.skip.pack(side="top")

        window = tk.Tk

    def Skip(self):
        self.quit()
        CalibrationStart()

    def GetCamera(self):
        # openCamera()
        pass
def choosecamera_routine(tk):
    ui = ChooseCameraStart()
    ui.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    choosecamera_routine(root)
