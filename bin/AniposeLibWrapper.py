# Wrap the aniposelib APIs.

from aniposelib.boards import CharucoBoard

def define_board_parameters(height, width, sq_len=25, marker_len=19, marker_bits=4, dict_size=50):
    board = CharucoBoard(height, width,
                         square_length=sq_len,  # here, in mm but any unit works
                         marker_length=marker_len,
                         marker_bits=marker_bits, dict_size=dict_size)
    return board


def do_calibration(board, vidnames, cgroup):
    cgroup.calibrate_videos(vidnames, board)
