__author__ = 'chris.maue'

import os
import SpawnGuiFromIni
import tkinter as tk
import threading
import time

appRunning = 0

class ThreadedAppWindow(threading.Thread):
    def __init__(self, IniFile):
        threading.Thread.__init__(self)
        self.IniFile = IniFile

    def run(self):
        self.root=tk.Tk()
        self.appWindow = SpawnGuiFromIni.SpawnAppWindow(self.root, self.IniFile)
        self.root.title('My Application Window')
        print("Frames Created: %d" % self.appWindow.framesCreated)
        self.root.mainloop()


# The following rungs start the thread and call the code to build the application window
appWindowCfgFileName = 'GuiConfig.ini'
path = os.path.dirname(os.path.realpath(__file__))
appWindowCfgFile = os.path.join(path, appWindowCfgFileName)

thread1 = ThreadedAppWindow(appWindowCfgFile)
thread1.start()
print('Frames created: %d' % thread1.appWindow.framesCreated)


while appRunning == 1:
    print(time.strftime("%c"))
    time.sleep(1)


