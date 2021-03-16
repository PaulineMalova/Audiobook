from tkinter import Tk
from tkinter.filedialog import askopenfilename


def pick_pdf_file():
    # we don't want a full GUI, so keep the root window from appearing
    Tk().withdraw()
    # open the dialog GUI
    filelocation = askopenfilename()
    return filelocation
