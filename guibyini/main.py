__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import configparser
import logging
import os
import sys
import SpawnGuiFromIni
import tkinter as tk
import threading
import time




#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui.ini'))




#######################################################################################################################
# Start program logger / debugger
#######################################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('[Main] Program Logger Started')




#######################################################################################################################
# Define Application Io data type
#######################################################################################################################
class ApplicationIO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]




#######################################################################################################################
# Define application window class and thread
#######################################################################################################################
class AppWindow(threading.Thread):
    global startime
    def __init__(self, iniFile, logFile, ioTable):
        self.iniFile = iniFile
        self.logFile = logFile
        self.ioTable = ioTable
        threading.Thread.__init__(self)
        logging.info('[Main (thread-1)] Application window init complete at t = +%f' % float(time.time()-startime))

    def run(self):
        self.root=tk.Tk()
        logging.info('[Main (thread-1)] Calling SpawnAppWindow function at t = +%f' % float(time.time()-startime))
        SpawnGuiFromIni.AppWindow(self.root, self.iniFile, self.logFile, self.ioTable)
        logging.info('[Main (thread-1)] Setting window title at t = +%f' % float(time.time()-startime))
        self.root.title('My Application Window')
        logging.info('[Main (thread-1)] Starting tkinter main loop at t = +%f' % float(time.time()-startime))
        self.root.mainloop()




#######################################################################################################################
# Define IO Monitoring class and thread
#######################################################################################################################
class IOMonitor(threading.Thread):
    global startime
    def __init__(self, realIO, IOcache, IOos, quitCmd, appWindow):
        self.realIO = realIO
        self.IOcache = IOcache
        self.IOos = IOos
        self.quitCommand = quitCmd
        self.appWindow = appWindow
        threading.Thread.__init__(self)

    def run(self):
        while True:
            for i in range(14):
                if self.realIO.input[i] == self.IOcache.input[i]:
                    self.realIO.input[i] = False
                if self.realIO.input[i] == True and self.IOcache.input[i] == False:
                    logging.info('[Main (thread-2)] F%d pressed at t = +%f' % (int(i), float(time.time()-startime)))
                    self.IOcache.input[i] = True
                    self.IOos.input[i] = True
                elif self.realIO.input[i] == False and self.IOcache.input[i] == True:
                    self.IOcache.input[i] = False

            # Shut down application and logic loop if "quit" button is pressed in application window
            if self.IOos.input[int(self.quitCommand)] == True:
                logging.info('[Main (thread-2)] F%d has been pressed (quit) at t = +%f' %
                             (int(i), float(time.time()-startime)))
                logging.info('[Main (thread-2)] Application is closing')
                self.appWindow.root.destroy()
                sys.exit()

            time.sleep(0.20)




#######################################################################################################################
# Get global application parameters from INI file
#######################################################################################################################
Config = configparser.ConfigParser()
Config.read(guiIniFile)
iniDict1 = {}
options = Config.options('config')
for option in options:
    try:
        iniDict1[option] = Config.get('config', option)
        if iniDict1[option] == -1:
            pass
    except:
        iniDict1[option] = None
quitCommand = iniDict1['quit command']




#######################################################################################################################
# Set up I/O table used by application window (live data, cache, and one-shot)
#######################################################################################################################
appWindowIoTable = ApplicationIO()
appWindowIoTableCache = ApplicationIO()
appWindowIoTableOS = ApplicationIO()




#######################################################################################################################
# Start application window and IO monitoring threads
#######################################################################################################################
startime = time.time()

Thread1 = AppWindow(guiIniFile, debugLogFile, appWindowIoTable)
Thread2 = IOMonitor(appWindowIoTable, appWindowIoTableCache, appWindowIoTableOS, quitCommand, Thread1)

Thread1.daemon = False
Thread2.daemon = True

Thread1.start()
logging.info('Thread 1 started')
Thread2.start()
logging.info('Thread 2 started')












