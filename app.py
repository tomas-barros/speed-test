import base
from tkinter import *

root = Tk()

# variables
uploadspeed = StringVar()
downloadspeed = StringVar()

# labels
uploadlabel = Label(root, textvariable=uploadspeed, text="Upload speed:\nPlease wait...")
uploadspeed.set('Upload speed:\nPlease wait...')
uploadlabel.pack()

downloadlabel = Label(root, textvariable=downloadspeed, text="Download speed:\nPlease wait...")
downloadspeed.set('Download speed:\nPlease wait...')
downloadlabel.pack()

# function
def refresh():
    uploadspeed.set('Upload speed:\nRefreshing data...')
    downloadspeed.set('Download speed:\nRefreshing data...')
    uploadspeed.set(base.get_upload_speed())
    downloadspeed.set(base.get_download_speed())
    print('Data has ben succesfully refreshed')

# buttons
refreshdata = Button(root, command=refresh, text="Refresh data...")
refreshdata.pack()


root.mainloop()