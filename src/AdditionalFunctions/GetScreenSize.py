from tkinter import Tk
from typing import Tuple

#
# @breif gives screen size has (width, height)
# @returns Tuple of width, height
# 
def getScreenSize() -> Tuple[int]:
    root = Tk()
    return (
        root.winfo_screenmmwidth(), 
        root.winfo_screenheight()
    )
