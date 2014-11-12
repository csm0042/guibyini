__author__ = 'chris.maue'

import logging
import os
import SpawnGuiFromIni
import tkinter as tk
import threading
import time


# Determine project path and auto-set debug log file and gui configuration file names as appropriate
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui.ini'))


# Start program logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('[Main] Program Logger Started')


class AppWindow(threading.Thread):
    def __init__(self, iniFile, logFile):
        self.iniFile = iniFile
        self.logFile = logFile
        threading.Thread.__init__(self)
        logging.info('[Main] Application window init complete at t = +%f' % float(time.time()-starttime))

    def run(self):
        self.root=tk.Tk()
        logging.info('[Main] Calling SpawnAppWindow function at t = +%f' % float(time.time()-starttime))
        SpawnGuiFromIni.AppWindow(self.root, self.iniFile, self.logFile)
        logging.info('[Main] Setting window title at t = +%f' % float(time.time()-starttime))
        self.root.title('My Application Window')
        logging.info('[Main] Starting tkinter main loop at t = +%f' % float(time.time()-starttime))
        self.root.mainloop()


starttime = time.time()
logging.info('[Main] Begin generation of application window at t = +%f' % float(starttime-starttime))
appWindowThread = AppWindow(guiIniFile, debugLogFile)
logging.info('[Main] Starting application window thread at t = +%f' % float(time.time()-starttime))
appWindowThread.start()



