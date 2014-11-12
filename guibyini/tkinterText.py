__author__ = 'chris.maue'

import config_parser

class Text(object):
    def __init__(self):
        self.autoSeparators = str()
        self.backgroundColor = str()
        self.backgroundStipple = str()
        self.borderwidth = str()
        self.cursor = str()
        self.exportSelection = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.foregroundStipple = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.insertBackground = str()
        self.insertBorderwidth = str()
        self.insertOffTime = str()
        self.insertOnTime = str()
        self.insertWidth = str()
        self.justify = str()
        self.lmargin1 = str()
        self.lmargin2 = str()
        self.maxUndo = str()
        self.padX = str()
        self.padY = str()
        self.offset = str()
        self.overstrike = str()
        self.relief = str()
        self.rmargin = str()
        self.selectBackgroundColor = str()
        self.selectForegroundColor = str()
        self.selectBorderwidth = str()
        self.setGrid = str()
        self.spacing1 = str()
        self.spacing2 = str()
        self.spacing3 = str()
        self.state = str()
        self.tabs = str()
        self.takeFocus = str()
        self.text = str()
        self.underline = str()
        self.undo = str()
        self.width = str()
        self.wrap = str()
        self.xScrollCommand = str()
        self.yScrollCommand = str()
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
        
        self.autoSeparators = dict1['auto separators']
        self.backgroundColor = dict1['background color']
        self.backgroundStipple = dict1['background stipple']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.exportSelection = dict1['export selection']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.foregroundStipple = dict1['foreground stipple']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.insertBackground = dict1['insert background']
        self.insertBorderwidth = dict1['insert border width']
        self.insertOffTime = dict1['insert off time']
        self.insertOnTime = dict1['insert on time']
        self.insertWidth = dict1['insert width']
        self.justify = dict1['justify']
        self.lmargin1 = dict1['lmargin1']
        self.lmargin2 = dict1['lmargin2']
        self.maxUndo = dict1['max undo']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.offset = dict1['offset']
        self.overstrike = dict1['overstrike']
        self.relief = dict1['relief']
        self.rmargin = dict1['rmargin']
        self.selectBackgroundColor =dict1['select background color']
        self.selectForegroundColor = dict1['select foreground color']
        self.selectBorderwidth = dict1['select border width']
        self.setGrid = dict1['set grid']
        self.spacing1 = dict1['spacing1']
        self.spacing2 = dict1['spacing2']
        self.spacing3 = dict1['spacing3']
        self.state = dict1['state']
        self.tabs = dict1['tabs']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.underline = dict1['underline']
        self.undo = dict1['undo']
        self.width = dict1['width']
        self.wrap = dict1['wrap']
        self.xScrollCommand = dict1['x scroll command']
        self.yScrollCommand = dict1['y scroll command']
        
        return self