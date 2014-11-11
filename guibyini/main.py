__author__ = 'chris.maue'

import os
import SpawnGuiFromIni
import tkinter as tk
import threading


class AppWindow(threading.Thread):
    def __init__(self, iniFile):
        self.iniFile = iniFile
        threading.Thread.__init__(self)

    def run(self):
        self.root=tk.Tk()
        SpawnGuiFromIni.SpawnAppWindow(self.root, self.iniFile)
        self.root.title('My Application Window')
        self.root.mainloop()


appWindowCfgFileName = 'gui.ini'
path = os.path.dirname(os.path.realpath(__file__))
appWindowCfgFile = os.path.join(path, appWindowCfgFileName)

appWindowThread = AppWindow(appWindowCfgFile)
appWindowThread.start()




