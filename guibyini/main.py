__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import logging
import os
import gui_class_definition




#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
projectPath = os.path.split(__file__)
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'gui_setup.ini'))




#######################################################################################################################
# Start program logger / debugger
#######################################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('[Main] Program Logger Started')
logging.info('[Main] Logging to file: %s' % debugLogFile)
logging.info('[Main] Using GUI configuration file: %s' % guiIniFile)





#######################################################################################################################
# Define Data types
#######################################################################################################################
class application_IO(object):
    def __init__(self):
        self.input = [bool() for i in range(32)]
        self.output = [bool() for i in range(32)]




#######################################################################################################################
# Define Data tags used for interlocking between application window and IO monitor threads
#######################################################################################################################
IoTable = application_IO()
IoTableCache = application_IO()
IoTableOS = application_IO()





#######################################################################################################################
# Start application window (runs in main thread)
#######################################################################################################################
gui_object = gui_class_definition.gui(guiIniFile, debugLogFile, IoTable)
gui_object.create_window()