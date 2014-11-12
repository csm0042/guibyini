__author__ = 'chris.maue'

import config_parser

class Frame(object):
    def __init__(self):
        self.backgroundColor = str()
        self.borderwidth = str()
        self.colormap = str()
        self.container = str()
        self.cursor = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.visual = str()
        self.width = str()
        self.iniFile = str()
        self.section = str()

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.colormap = dict1['color map']
        self.container = dict1['container']
        self.cursor = dict1['cursor']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.visual = dict1['visual']
        self.width = dict1['width']

        return self