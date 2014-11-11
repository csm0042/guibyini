__author__ = 'chris.maue'

import os
import SpawnGuiFromIni
import tkinter as tk
import threading
import time


class AppWindow(threading.Thread):
    def __init__(self, IniFile):
        self.IniFile = IniFile
        threading.Thread.__init__(self)

    def run(self):
        self.root=tk.Tk()
        SpawnGuiFromIni.SpawnAppWindow(self.root, self.IniFile)
        self.root.title('My Application Window')
        self.root.mainloop()

# The following rungs start the thread and call the code to build the application window
appWindowCfgFileName = 'gui.ini'
path = os.path.dirname(os.path.realpath(__file__))
appWindowCfgFile = os.path.join(path, appWindowCfgFileName)

appWindowThread = AppWindow(appWindowCfgFile)
appWindowThread.start()

while appRunning == 1:
    print(time.strftime("%c"))
    time.sleep(1)


