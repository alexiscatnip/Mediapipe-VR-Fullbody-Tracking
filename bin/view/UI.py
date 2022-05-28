# a control panel to manage the calibration and stuff
# import tkinter as tk
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel

from bin.view import camera_gui, tk_helpers, inference_gui
# from bin.view.camera_gui import CameraWindow

class Main_UI(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.setFixedSize(QSize(400, 300))

        self.model = model

        lbl1 = QLabel('Welcome to uwuPose')

        self.setCentralWidget(lbl1)
        # tk_helpers.put_separator(root)
        # tk.Label(self.master, text='First, you must set up the following:').pack()
        #
        # tk.Button(self.master, text='1. Setup Cameras',
        #           command=self.newWindow_SetupCameras).pack()
        #
        # tk.Button(self.master, text='2. Calibrate Cameras',
        #           command=self.newWindow_CalibrateCameras).pack()
        # tk_helpers.put_separator(root)
        #
        # tk.Label(self.master, text='Then, you can run the main program.').pack()
        #
        # tk.Button(self.master, text='3. Start the main program ',
        #           command=self.closeWindow_MainProgram).pack()

    # def newWindow_SetupCameras(self):
    #     self.SetupCamerasWindow = tk.Toplevel(self.master)
    #     self.app = CameraWindow(self.SetupCamerasWindow, self.model)

    def newWindow_CalibrateCameras(self):
        raise NotImplementedError
        # ui = camera_gui.CameraWindow(self)
        # ui.mainloop()

    def closeWindow_MainProgram(self):
        self.root.destroy()
        inference_gui.windowOpen(self.model)
        # self.SetupCamerasWindow = tk.Toplevel(self.master)
        # self.app = CameraWindow(self.SetupCamerasWindow, self.model)
#
# def windowOpen(model):
#     root = tk.Tk()
#     ControlPanel(root, model).pack(side="top", fill="both", expand=True)
#     root.mainloop()

def start(model):
    app = QApplication()

    # Create a Qt widget, which will be our window.
    window = Main_UI(model)
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()
