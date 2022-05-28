# calibration routine, where the user can hold up the chessboard in sync with TTS.
from bin.logic import parameters
from bin.logic.model import Model
from bin.view import UI
from bin.view.calibration_gui import CalibrationStart

import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()
    params = parameters.load()
    model = Model(params)
    controlpanel_gui.windowOpen(model)

    # wtf, i am not able to simulate a button press to test
    # the loading of the 2nd ui window - the choose camera view.


