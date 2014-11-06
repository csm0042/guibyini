__author__ = 'chris.maue'

import os
import SpawnGuiFromIni
import tkinter as tk
import threading
import time

appRunning = 0

# The following rungs start the thread and call the code to build the application window
appWindowCfgFileName = 'GuiConfig.ini'
path = os.path.dirname(os.path.realpath(__file__))
appWindowCfgFile = os.path.join(path, appWindowCfgFileName)
root = tk.Tk()
appWindow = SpawnGuiFromIni(root, appWindowCfgFile)

root.mainloop()



while appRunning == 1:
    print(time.strftime("%c"))
    time.sleep(1)


