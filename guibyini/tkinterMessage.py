__author__ = 'chris.maue'

import config_parser

class Message(object):
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

    def read_settings(self, iniFile, section):
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

    def apply_settings(self):
        if self.messageSettings[self.messagesCreated].anchor != "":
            self.message.config(anchor=self.messageSettings[self.messagesCreated].anchor)
        if self.messageSettings[self.messagesCreated].aspect != "":
            self.message.config(aspect=self.messageSettings[self.messagesCreated].aspect)
        if self.messageSettings[self.messagesCreated].backgroundColor != "":
            self.message.config(background=self.messageSettings[self.messagesCreated].backgroundColor)
        if self.messageSettings[self.messagesCreated].borderwidth != "":
            self.message.config(borderwidth=self.messageSettings[self.messagesCreated].borderwidth)
        if self.messageSettings[self.messagesCreated].cursor != "":
            self.message.config(cursor=self.messageSettings[self.messagesCreated].cursor)
        if self.messageSettings[self.messagesCreated].font != "" and \
                        self.messageSettings[self.messagesCreated].fontSize != "":
            self.message.config(font=(self.messageSettings[self.messagesCreated].font,
                                      int(self.messageSettings[self.messagesCreated].fontSize)))
        if self.messageSettings[self.messagesCreated].foregroundColor != "":
            self.message.config(foreground=self.messageSettings[self.messagesCreated].foregroundColor)
        if self.messageSettings[self.messagesCreated].highlightBackground != "":
            self.message.config(highlightbackground=self.messageSettings[self.messagesCreated].highlightBackground)
        if self.messageSettings[self.messagesCreated].highlightBackgroundColor != "":
            self.message.config(highlightcolor=self.messageSettings[self.messagesCreated].highlightBackgroundColor)
        if self.messageSettings[self.messagesCreated].highlightThickness != "":
            self.message.config(highlightthickness=int(self.messageSettings[self.messagesCreated].highlightThickness))
        if self.messageSettings[self.messagesCreated].justify != "":
            self.message.config(justify=self.messageSettings[self.messagesCreated].justify)
        if self.messageSettings[self.messagesCreated].padX != "":
            self.message.config(padx=int(self.messageSettings[self.messagesCreated].padX))
        if self.messageSettings[self.messagesCreated].padY != "":
            self.message.config(pady=int(self.messageSettings[self.messagesCreated].padY))
        if self.messageSettings[self.messagesCreated].relief != "":
            self.message.config(relief=self.messageSettings[self.messagesCreated].relief)
        if self.messageSettings[self.messagesCreated].takeFocus != "":
            self.message.config(takefocus=self.messageSettings[self.messagesCreated].takeFocus)
        if self.messageSettings[self.messagesCreated].text != "":
            self.message.config(text=self.messageSettings[self.messagesCreated].text)
        if self.messageSettings[self.messagesCreated].textVariable != "":
            self.message.config(textvariable=self.messageSettings[self.messagesCreated].textVariable)
        if self.messageSettings[self.messagesCreated].width != "":
            self.message.config(width=int(self.messageSettings[self.messagesCreated].width))
        if self.messagesPlace[self.messagesCreated].anchor != '':
            self.message.place_configure(anchor=self.messagesPlace[self.messagesCreated].anchor)
        if self.messagesPlace[self.messagesCreated].borderMode != '':
            self.message.place_configure(bordermode=self.messagesPlace[self.messagesCreated].borderMode)
        if self.messagesPlace[self.messagesCreated].height != '':
            self.message.place_configure(height=int(self.messagesPlace[self.messagesCreated].height))
        if self.messagesPlace[self.messagesCreated].relHeight != '':
            self.message.place_configure(relheight=int(self.messagesPlace[self.messagesCreated].relHeight))
        if self.messagesPlace[self.messagesCreated].width != '':
            self.message.place_configure(width=int(self.messagesPlace[self.messagesCreated].width))
        if self.messagesPlace[self.messagesCreated].relWidth != '':
            self.message.place_configure(relwidth=int(self.messagesPlace[self.messagesCreated].relWidth))
        if self.messagesPlace[self.messagesCreated].relX != '':
            self.message.place_configure(relx=int(self.messagesPlace[self.messagesCreated].relX))
        if self.messagesPlace[self.messagesCreated].relY != '':
            self.message.place_configure(rely=int(self.messagesPlace[self.messagesCreated].relY))
        if self.messagesPlace[self.messagesCreated].offsetX != '':
            self.message.place_configure(x=int(self.messagesPlace[self.messagesCreated].offsetX))
        if self.messagesPlace[self.messagesCreated].offsetY != '':
            self.message.place_configure(y=int(self.messagesPlace[self.messagesCreated].offsetY))