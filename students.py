import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

import os
from pathlib import Path

from PIL import ImageTk, Image

##################### SQL TABLE SECTION #####################

students_table = """
CREATE table if not exists STUDENTS (
    id interger primary key,
    name text,
    last_name text,
    cohort text,
    pod text,
    comment text
);
"""
###########################################################
################ TKINTER WINDOW SECTION ###################
###########################################################
    
#ROOT Setup
root = Tk()
root.title("STUDENTS")
root.resizable(False, False)
#root.after_idle(load_viewer)

#MainFrame Window 
window = ttk.Frame(root, padding="5", width=400, height=250)
window.grid(column=0, row=0, sticky=(N, W, E, S))

#Input Variables
id_var = StringVar()
name_var = StringVar()
last_name_var = StringVar()
cohort_var = StringVar()
pod_var = StringVar()
comment_var = StringVar()

#Input Fields[Left Side]
name_lbl = ttk.Label(window, text="First name: ")
name = ttk.Entry(window, textvariable=name_var)
name_lbl.grid(column=1, row=0, sticky=W)
name.grid(column=1, row=1, sticky='we',columnspan=3)

last_name_lbl = ttk.Label(window, text="Last name: ")
last_name = ttk.Entry(window, textvariable=last_name_var)
last_name_lbl.grid(column=1, row=0, sticky=W)
last_name.grid(column=1, row=1, sticky='we',columnspan=3)

cohort_lbl = ttk.Label(window, text="Cohort: ")
cohort = ttk.Entry(window, textvariable=cohort_var)
cohort_lbl.grid(column=1, row=0, sticky=W)
cohort.grid(column=1, row=1, sticky='we',columnspan=3)

pod_lbl = ttk.Label(window, text="Pod: ")
pod = ttk.Entry(window, textvariable=pod_var)
pod_lbl.grid(column=1, row=0, sticky=W)
pod.grid(column=1, row=1, sticky='we',columnspan=3)

comment_lbl = ttk.Label(window, text="Comment: ")
comment = ttk.Entry(window, textvariable=comment_var)
comment_lbl.grid(column=1, row=0, sticky=W)
comment.grid(column=1, row=1, sticky='we',columnspan=3)


root.mainloop()
