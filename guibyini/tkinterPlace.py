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
        
        self.anchor = dict1['place anchor']
        self.borderMode = dict1['place border mode']
        self.height = dict1['place height']
        self.width = dict1['place width']
        self.relHeight = dict1['place rel height']
        self.relWidth = dict1['place rel width']
        self.relX = dict1['place rel x']
        self.relY = dict1['place rel y']
        self.offsetX = dict1['place offset x']
        self.offsetY = dict1['place offset y']

        return self

