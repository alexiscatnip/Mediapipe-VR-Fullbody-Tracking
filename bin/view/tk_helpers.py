from tkinter import ttk


def put_separator(root):
    separator = ttk.Separator(root, orient='horizontal')
    separator.pack(fill='x')