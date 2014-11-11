__author__ = 'chris.maue'

import config_parser

class Place(object):
    def __init__(self):
        self.anchor = str()
        self.borderMode = str()
        self.height = str()
        self.width = str()
        self.relHeight = str()
        self.relWidth = str()
        self.relX = str()
        self.relY = str()
        self.offsetX = str()
        self.offsetY = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        self.anchor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place anchor')
        self.borderMode = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place border mode')
        self.height = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place height')
        self.width = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place width')
        self.relHeight = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel height')
        self.relWidth = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel width')
        self.relX = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel x')
        self.relY = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel y')
        self.offsetX = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place offset x')
        self.offsetY = config_parser.ConfigSectionMap(self.iniFile, self.section, 'place offset y')
        return self

