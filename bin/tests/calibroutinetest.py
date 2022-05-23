# calibration routine, where the user can hold up the chessboard in sync with TTS.
from bin.view.Calibration import CalibrationStart
import tkinter as tk

def do_calibration_routine(tk):
    CalibrationStart()

    stop_calibration_flag = False
    while(stop_calibration_flag is False):
        # view.openModal("continue")
        pass

if __name__ == "__main__":
    root = tk.Tk()
    do_calibration_routine(root)
