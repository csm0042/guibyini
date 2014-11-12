__author__ = 'chris.maue'

import config_parser

class Window(object):
    def __init__(self):
        self.width = str()
        self.height = str()
        self.posX = str()
        self.posY = str()
        self.title = str()
        self.backgroundColor = str()
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

        self.width = dict1['width']
        self.height = dict1['height']
        self.posX = dict1['pos x']
        self.posY = dict1['pos y']
        self.title = dict1['title']
        self.backgroundColor = dict1['background color']

        #self.width = config_parser.ConfigSectionMap(self.iniFile, self.section, 'width')
        #self.height = config_parser.ConfigSectionMap(self.iniFile, self.section, 'height')
        #self.posX = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos x')
        #self.posY = config_parser.ConfigSectionMap(self.iniFile, self.section, 'pos y')
        #self.title = config_parser.ConfigSectionMap(self.iniFile, self.section, 'title')
        #self.backgroundColor = config_parser.ConfigSectionMap(self.iniFile, self.section, 'background color')

        return self