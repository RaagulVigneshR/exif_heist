from tkinter import *
from tkinter import filedialog

import os
import csv
import time
from core.exif import Exif
from core.configs import (
    Config,
    Colors
)

#using tkinter GUI we are getting the path of the file//
window = Tk()
filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("All files","*.**"),("all files","*.*")))

  
#processing time(Let the window wait for any events)
time.sleep(2)
Config.banner()
image_path = filename
option = str(input(Config.CHOOSE_FROM_MENU))
exif = Exif()
if option in ["1", "01"]:
    exif_data = exif.extract_data(image_path)
    if not exif_data:
     print(f"No Exif data found in '{image_path}'")
     exit()
_csv_file = "exif_data.csv"
#Deleting old data if already found
if os.path.exists(_csv_file):
        print(f"Deleting old '{_csv_file}' ...")
        os.remove(_csv_file)
with open(_csv_file, "a", newline="") as f:
            csv_writer = csv.writer(f)
            for i in exif_data.items():
             csv_writer.writerow(i)
             print(f"Data saved in '{_csv_file}' ...")
            
exit(5)
window.mainloop()

