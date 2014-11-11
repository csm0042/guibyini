__author__ = 'chris.maue'

import config_parser

class Frame(object):
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

    def read_settings(self, iniFile, section):
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

    def apply_settings(self):
        if self.frameSettings[self.framesCreated].backgroundColor != '':
            self.frame.config(background=self.frameSettings[self.framesCreated].backgroundColor)
        if self.frameSettings[self.framesCreated].borderwidth != '':
            self.frame.config(borderwidth=int(self.frameSettings[self.framesCreated].borderwidth))
        if self.frameSettings[self.framesCreated].colormap != '':
            self.frame.config(colormap=self.frameSettings[self.framesCreated].colormap)
        if self.frameSettings[self.framesCreated].container != '':
            self.frame.config(container=self.frameSettings[self.framesCreated].container)
        if self.frameSettings[self.framesCreated].cursor != '':
            self.frame.config(cursor=self.frameSettings[self.framesCreated].cursor)
        if self.frameSettings[self.framesCreated].height != '':
            self.frame.config(height=int(self.frameSettings[self.framesCreated].height))
        if self.frameSettings[self.framesCreated].highlightBackgroundColor != '':
            self.frame.config(highlightbackground=self.frameSettings[self.framesCreated].highlightBackgroundColor)
        if self.frameSettings[self.framesCreated].highlightColor != '':
            self.frame.config(highlightcolor=self.frameSettings[self.framesCreated].highlightColor)
        if self.frameSettings[self.framesCreated].highlightThickness != '':
            self.frame.config(highlightthickness=int(self.frameSettings[self.framesCreated].highlightThickness))
        if self.frameSettings[self.framesCreated].padX != '':
            self.frame.config(padx=int(self.frameSettings[self.framesCreated].padX))
        if self.frameSettings[self.framesCreated].padY != '':
            self.frame.config(pady=int(self.frameSettings[self.framesCreated].padY))
        if self.frameSettings[self.framesCreated].relief != '':
            self.frame.config(relief=self.frameSettings[self.framesCreated].relief)
        if self.frameSettings[self.framesCreated].takeFocus != '':
            self.frame.config(takefocus=self.frameSettings[self.framesCreated].takeFocus)
        if self.frameSettings[self.framesCreated].visual != '':
            self.frame.config(visual=self.frameSettings[self.framesCreated].visual)
        if self.frameSettings[self.framesCreated].width != '':
            self.frame.config(width=int(self.frameSettings[self.framesCreated].width))
        if self.framesPlace[self.framesCreated] != '':
            self.frame.place_configure(anchor=self.framesPlace[self.framesCreated].anchor)
        if self.framesPlace[self.framesCreated].borderMode != '':
            self.frame.place_configure(bordermode=self.framesPlace[self.framesCreated].borderMode)
        if self.framesPlace[self.framesCreated].height != '':
            self.frame.place_configure(height=int(self.framesPlace[self.framesCreated].height))
        if self.framesPlace[self.framesCreated].width != '':
            self.frame.place_configure(width=int(self.framesPlace[self.framesCreated].width))
        if self.framesPlace[self.framesCreated].relHeight != '':
            self.frame.place_configure(relheight=int(self.framesPlace[self.framesCreated].relHeight))
        if self.framesPlace[self.framesCreated].relWidth != '':
            self.frame.place_configure(relwidth=int(self.framesPlace[self.framesCreated].relWidth))
        if self.framesPlace[self.framesCreated].relX != '':
            self.frame.place_configure(relx=int(self.framesPlace[self.framesCreated].relX))
        if self.framesPlace[self.framesCreated].relY != '':
            self.frame.place_configure(rely=int(self.framesPlace[self.framesCreated].relY))
        if self.framesPlace[self.framesCreated].offsetX != '':
            self.frame.place_configure(x=int(self.framesPlace[self.framesCreated].offsetX))
        if self.framesPlace[self.framesCreated].offsetY != '':
            self.frame.place_configure(y=int(self.framesPlace[self.framesCreated].offsetY))