__author__ = 'chris.maue'

import config_parser

class Place(object):
    def __init__(self):
        self.anchor = str()
        self.borderMode = str()
        self.height = int()
        self.width = int()
        self.relHeight = float()
        self.relWidth = float()
        self.relX = float()
        self.relY = float()
        self.offsetX = int()
        self.offsetY = int()
        self.iniFile = str()
        self.section = str()

    def read_settings(self, iniFile, section):
        self.iniFile = iniFile
        self.section = section
        self.anchor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place anchor'))
        self.borderMode = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place border mode'))
        self.height = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place height'))
        self.width = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place width'))
        self.relHeight = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel height'))
        self.relWidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel width'))
        self.relX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel x'))
        self.relY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place rel y'))
        self.offsetX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place offset x'))
        self.offsetY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'place offset y'))
        return self

