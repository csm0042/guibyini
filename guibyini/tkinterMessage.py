__author__ = 'chris.maue'

import config_parser

class Message(object):
    def __init__(self):
        self.anchor = str()
        self.aspect = str()
        self.backgroundColor = str()
        self.borderwidth = str()
        self.cursor = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.highlightBackground = str()
        self.highlightBackgroundColor = str()
        self.highlightThickness = str()
        self.justify = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.width = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        self.anchor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'anchor')
        self.aspect = config_parser.ConfigSectionMap(self.iniFile, self.section, 'aspect')
        self.backgroundColor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'background color')
        self.borderwidth = config_parser.ConfigSectionMap(self.iniFile, self.section, 'border width')
        self.cursor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'cursor')
        self.font = config_parser.ConfigSectionMap(self.iniFile, self.section, 'font')
        self.fontSize = config_parser.ConfigSectionMap(self.iniFile, self.section, 'font size')
        self.foregroundColor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'foreground color')
        self.highlightBackground = config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight background')
        self.highlightBackgroundColor = config_parser.ConfigSectionMap(self.iniFile, self.section,
                                                                       'highlight background color')
        self.highlightThickness = config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight thickness')
        self.justify = config_parser.ConfigSectionMap(self.iniFile, self.section, 'justify')
        self.padX = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad x')
        self.padY = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad y')
        self.relief = config_parser.ConfigSectionMap(self.iniFile, self.section, 'relief')
        self.takeFocus = config_parser.ConfigSectionMap(self.iniFile, self.section, 'take focus')
        self.text = config_parser.ConfigSectionMap(self.iniFile, self.section, 'text')
        self.textVariable = config_parser.ConfigSectionMap(self.iniFile, self.section, 'text variable')
        self.width = config_parser.ConfigSectionMap(self.iniFile, self.section, 'width')
        return self
