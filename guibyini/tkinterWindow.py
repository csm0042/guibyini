__author__ = 'chris.maue'

import config_parser

class Window(object):
    def __init__(self):
        self.width = str()
        self.height = str()
        self.posX = str()
        self.posY = str()
        self.title = str()
        self.color = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        self.width = config_parser.ConfigSectionMap(self.iniFile, self.section, 'width')
        self.height = config_parser.ConfigSectionMap(self.iniFile, self.section, 'height')
        self.posX = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos x')
        self.posY = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos y')
        self.title = config_parser.ConfigSectionMap(self.iniFile, self.section, 'title')
        self.color = config_parser.ConfigSectionMap(self.iniFile, self.section, 'color')
        return self