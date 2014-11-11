__author__ = 'chris.maue'

import config_parser

class Window(object):
    def __init__(self):
        self.windowFrameSizeX = int()
        self.windowFrameSizeY = int()
        self.windowPosX = int()
        self.windowPosY = int()
        self.windowTitle = str()
        self.windowColor = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self, iniFile, section):
        self.iniFile = iniFile
        self.section = section
        self.windowFrameSizeX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'size_x'))
        self.windowFrameSizeY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'size_y'))
        self.windowPosX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos_x'))
        self.windowPosY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos_y'))
        self.windowTitle = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'title'))
        self.windowColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'color'))
        return self

    def apply_settings(self):
        self.parent.geometry("%sx%s+%s+%s" % (self.windowFrameSizeX, self.windowFrameSizeY, self.windowPosX,
                                              self.windowPosY))
        self.parent.title(self.windowTitle)
        self.parent.configure(background=self.windowColor)