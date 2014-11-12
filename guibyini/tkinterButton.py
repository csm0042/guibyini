__author__ = 'chris.maue'


class Button(object):
    def __init__(self):
        self.activeBackgroundColor = str()
        self.activeForegroundColor = str()
        self.anchor = str()
        self.backgroundColor = str()
        self.bitmap = str()
        self.borderwidth = int()
        self.command = int()
        self.compound = str()
        self.cursor = str()
        self.default = str()
        self.disableForeground = str()
        self.font = str()
        self.fontSize = int()
        self.foregroundColor = str()
        self.height = int()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = int()
        self.image = str()
        self.justify = str()
        self.overRelief = str()
        self.padX = int()
        self.padY = int()
        self.relief = str()
        self.repeatDelay = int()
        self.repeatInterval = int()
        self.state = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.underline = str()
        self.width = int()
        self.wrapLength = int()
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
        self.bitmap = dict1['bitmap']
        self.borderwidth = dict1['border width']
        self.command = dict1['command']
        self.compound = dict1['compound']
        self.cursor = dict1['cursor']
        self.default = dict1['default']
        self.disableForeground = dict1['disable foreground']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.image = dict1['image']
        self.justify = dict1['justify']
        self.overRelief = dict1['over relief']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.repeatDelay = dict1['repeat delay']
        self.repeatInterval = dict1['repeat interval']
        self.state = dict1['state']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.underline = dict1['underline']
        self.width = dict1['width']
        self.wrapLength = dict1['wrap length']

        return self