# camera-calibration related view

import tkinter as tk
from tkinter import ttk

from bin.logic import parameters


class CalibrationStart(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 100)

        self.label = ttk.Label(self, text="Calibrate the cameras")
        self.label.pack()

        self.label = ttk.Label(self, text="After you click start, there will be a countdown. Then we take an image. Then repeat. To pause it, press the space bar.")
        self.label.pack()


        self.button = ttk.Button(self, text="Start the calibrate sequence", command=self.OnBtnDown_Calibrate)
        self.button.pack(side="top")


    def OnBtnDown_Calibrate(self):
        self.window.quit
        Calibrate()

class Calibrate(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 100)

        self.label = ttk.Label(self, text="Let's gather calibration Images")
        self.label.pack()

        self.button = ttk.Button(self, text="Yes, calibrate", command=self.OnBtnDown_Calibrate)
        self.button.pack(side="top")

def launchGUIandBlock(_params):
    root = tk.Tk()
    CalibrationStart(root, _params).pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    launchGUIandBlock(parameters.load())