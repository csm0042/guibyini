import tkinter as tk
import config_parser
import widget_count
import gui_controls


class PlaceSettings(object):
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

    def GetPlaceSettings(self, iniFile, section):
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


class FrameWidget(object):
    def __init__(self):
        self.backgroundColor = str()
        self.borderwidth = int()
        self.colormap = str()
        self.container = str()
        self.cursor = str()
        self.height = int()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = int()
        self.padX = int()
        self.padY = int()
        self.relief = str()
        self.takeFocus = str()
        self.visual = str()
        self.width = int()
        self.iniFile = str()
        self.section = str()


    def GetFrameSettings(self, iniFile, section):
        self.iniFile = iniFile
        self.section = section
        self.backgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'background color'))
        self.borderwidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'border width'))
        self.colormap = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'color map'))
        self.container = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'container'))
        self.cursor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'cursor'))
        self.height = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'height'))
        self.highlightBackgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight background color'))
        self.highlightColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight color'))
        self.highlightThickness = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight thickness'))
        self.padX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad x'))
        self.padY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad y'))
        self.relief = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'relief'))
        self.takeFocus = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'take focus'))
        self.visual = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'visual'))
        self.width = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'width'))
        return self


class MessageWidget(object):
    def __init__(self):
        self.anchor = str()
        self.aspect = str()
        self.backgroundColor = str()
        self.borderwidth = int()
        self.cursor = str()
        self.font = str()
        self.fontSize = int()
        self.foregroundColor = str()
        self.highlightBackground = str()
        self.highlightBackgroundColor = str()
        self.highlightThickness = int()
        self.justify = str()
        self.padX = int()
        self.padY = int()
        self.relief = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.width = int()
        self.iniFile = str()
        self.section = str()

    def GetMessageSettings(self, iniFile, section):
        self.iniFile = iniFile
        self.section = section
        self.anchor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'anchor'))
        self.aspect = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'aspect'))
        self.backgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'background color'))
        self.borderwidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'border width'))
        self.cursor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'cursor'))
        self.font = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'font'))
        self.fontSize = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'font size'))
        self.foregroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'foreground color'))
        self.highlightBackground = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight background'))
        self.highlightBackgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight background color'))
        self.highlightThickness = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight thickness'))
        self.justify = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'justify'))
        self.padX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad x'))
        self.padY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad y'))
        self.relief = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'relief'))
        self.takeFocus = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'take focus'))
        self.text = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'text'))
        self.textVariable = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'text variable'))
        self.width = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'width'))
        return self


class TextWidget(object):
    def __init__(self):
        self.autoSeparators = str()
        self.backgroundColor = str()
        self.backgroundStipple = str()
        self.borderwidth = int()
        self.cursor = str()
        self.exportSelection = str()
        self.font = str()
        self.fontSize = int()
        self.foregroundColor = str()
        self.foregroundStipple = str()
        self.height = int()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = int()
        self.insertBackground = str()
        self.insertBorderwidth = int()
        self.insertOffTime = int()
        self.insertOnTime = int()
        self.insertWidth = int()
        self.justify = str()
        self.lmargin1 = str()
        self.lmargin2 = str()
        self.maxUndo = int()
        self.padX = int()
        self.padY = int()
        self.offset = str()
        self.overstrike = str()
        self.relief = str()
        self.rmargin = int()
        self.selectBackgroundColor = str()
        self.selectForegroundColor = str()
        self.selectBorderwidth = int()
        self.setGrid = str()
        self.spacing1 = int()
        self.spacing2 = int()
        self.spacing3 = int()
        self.state = str()
        self.tabs = str()
        self.takeFocus = str()
        self.text = str()
        self.underline = str()
        self.undo = str()
        self.width = int()
        self.wrap = str()
        self.xScrollCommand = str()
        self.yScrollCommand = str()
        self.iniFile = str()
        self.section = str()

    def GetTextSettings(self, iniFile, section):
        self.iniFile = iniFile
        self.section = section
        self.autoSeparators = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'auto separators'))
        self.backgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'background color'))
        self.backgroundStipple = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'background stipple'))
        self.borderwidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'border width'))
        self.cursor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'cursor'))
        self.exportSelection = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'export selection'))
        self.font = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'font'))
        self.fontSize = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'font size'))
        self.foregroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'foreground color'))
        self.foregroundStipple = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'foreground stipple'))
        self.height = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'height'))
        self.highlightBackgroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight background color'))
        self.highlightColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight color'))
        self.highlightThickness = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'highlight thickness'))
        self.insertBackground = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'insert background'))
        self.insertBorderwidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'insert border width'))
        self.insertOffTime = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'insert off time'))
        self.insertOnTime = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'insert on time'))
        self.insertWidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'insert width'))
        self.justify = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'justify'))
        self.lmargin1 = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'lmargin1'))
        self.lmargin2 = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'lmargin2'))
        self.maxUndo = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'max undo'))
        self.padX = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad x'))
        self.padY = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'pad y'))
        self.offset = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'offset'))
        self.overstrike = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'overstrike'))
        self.relief = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'relief'))
        self.rmargin = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'rmargin'))
        self.selectBackgroundColor =str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'select background color'))
        self.selectForegroundColor = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'select foreground color'))
        self.selectBorderwidth = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'select border width'))
        self.setGrid = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'set grid'))
        self.spacing1 = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'spacing1'))
        self.spacing2 = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'spacing2'))
        self.spacing3 = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'spacing3'))
        self.state = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'state'))
        self.tabs = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'tabs'))
        self.takeFocus = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'take focus'))
        self.text = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'text'))
        self.underline = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'underline'))
        self.undo = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'undo'))
        self.width = int(config_parser.ConfigSectionMap(self.iniFile, self.section, 'width'))
        self.wrap = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'wrap'))
        self.xScrollCommand = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'x scroll command'))
        self.yScrollCommand = str(config_parser.ConfigSectionMap(self.iniFile, self.section, 'y scroll command'))
        return self


class ButtonWidget(object):
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
        self.disabledForeground = str()
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










if __name__ == "__main__":
    root=tk.Tk()
    app = SpawnAppWindow(root, 'GuiConfig.ini')
    app.title('My OPC Client')
    app.mainloop()