__author__ = 'chris.maue'

import os
import SpawnGuiFromIni
import tkinter as tk

# The following line of code calls the GUI builder class defined in the "SpawnGuiFromIni.py" file.
appWindowCfgFileName = 'GuiConfig.ini'
path = os.path.dirname(os.path.realpath(__file__))
appWindowCfgFile = os.path.join(path, appWindowCfgFileName)

root = tk.Tk()
MainApplication = SpawnGuiFromIni.SpawnAppWindow(root, appWindowCfgFile)
root.title('My OPC Client 2')

# Run Tkinter main loop
root.mainloop()

# Destroy root window if still open once program exits tkinter main loop
try:
    root.destroy()
    print('Application closed')
except:
    pass