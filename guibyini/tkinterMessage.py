__author__ = 'chris.maue'


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
        
        self.anchor = dict1['anchor']
        self.aspect = dict1['aspect']
        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.highlightBackground = dict1['highlight background']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightThickness = dict1['highlight thickness']
        self.justify = dict1['justify']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.width = dict1['width']

        return self
