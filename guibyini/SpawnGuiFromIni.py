# cmd /k c:\python34\python.exe "C:\Users\cmaue\OneDrive\MyPythonProjects\OPC_Tool\OPC_Tool\Main.py"

import tkinter as tk
import config_parser
import widget_count
import gui_controls

class SpawnAppWindow:
    def __init__(self, parent, windowIniFile):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.windowIniFile = windowIniFile
        self.windowSection = str()
        self.frameCount = 0
        self.framesCreated = 0
        self.frameSection = str()
        self.buttonCount = 0
        self.buttonsCreated = 0
        self.buttonSection = str()
        self.appWindowFrameSizeX = 0
        self.appWindowFrameSizeY = 0
        self.appWindowPosX = 0
        self.appWindowPosY = 0
        self.appWindowTitle = str()
        self.appWindowColor = str()
        self.frameAnchor = str()
        self.frameSizeX = str()
        self.frameSizeY = str()
        self.framePosX = str()
        self.framePosY = str()
        self.frameBorderWidth = str()
        self.frameRelief = str()
        self.buttonAnchor = str()
        self.buttonSizeX = str()
        self.buttonSizeY = str()
        self.buttonPosX = str()
        self.buttonPosY = str()
        self.buttonBackgroundColor = str()
        self.buttonBitmap = str()
        self.buttonText = str()
        self.buttonBorderWidth = str()
        self.buttonRelief = str()
        self.buttonJustify = str()
        self.buttonTextWrapLength = str()
        self.initialize()




    def initialize(self):
        # Spawn main window
        self.windowSection = 'main window'
        self.DrawWindow()

        # Add frames
        self.frameCount = widget_count.CountWidgetByType(self.windowIniFile, "frame")
        self.framesCreated = 0
        while self.framesCreated < self.frameCount:
            self.framesCreated += 1
            self.frameSection = "frame" + str(self.framesCreated)
            self.frame[self.framesCreated] = self.DrawFrame()

        # Add buttons
        self.buttonCount = widget_count.CountWidgetByType(self.windowIniFile, "button")
        self.buttonsCreated = 0
        while self.buttonsCreated < self.buttonCount:
            self.buttonsCreated += 1
            self.buttonSection = "button" + str(self.buttonsCreated)
            self.button[self.buttonsCreated] = self.DrawButton()

        # Add text
        self.textCount = widget_count.CountWidgetByType(self.windowIniFile, "text")
        self.textCreated = 0
        while self.textCreated < self.textCount:
            self.textCreated += 1
            self.textSection = "text" + str(self.textCreated)
            self.text[self.textCreated] = self.DrawText()




    def DrawWindow(self):
        self.appWindowFrameSizeX = int(config_parser.ConfigSectionMap(self.windowIniFile,
                                    self.windowSection, 'size_x'))
        self.appWindowFrameSizeY = int(config_parser.ConfigSectionMap(self.windowIniFile,
                                    self.windowSection, 'size_y'))
        self.appWindowPosX = int(config_parser.ConfigSectionMap(self.windowIniFile, self.windowSection, 'pos_x'))
        self.appWindowPosY = int(config_parser.ConfigSectionMap(self.windowIniFile, self.windowSection, 'pos_y'))
        self.parent.geometry("%sx%s+%s+%s" % (self.appWindowFrameSizeX, self.appWindowFrameSizeY, self.appWindowPosX,
                                       self.appWindowPosY))
        self.appWindowTitle = config_parser.ConfigSectionMap(self.windowIniFile, self.windowSection, 'title')
        self.parent.title(self.appWindowTitle)
        self.appWindowColor = config_parser.ConfigSectionMap(self.windowIniFile, self.windowSection, 'color')
        self.parent.configure(background=self.appWindowColor)




    def DrawFrame(self):
        self.frame = tk.Frame(self.parent)
        self.frameAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'anchor')
        self.frameSizeX = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'size_x')
        self.frameSizeY = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'size_y')
        self.framePosX = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'pos_x')
        self.framePosY = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'pos_y')
        self.frame.place(anchor=self.frameAnchor, height=int(self.frameSizeY), width=int(self.frameSizeX),
                         x=int(self.framePosX), y=int(self.framePosY))
        self.frameBorderWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'border_width')
        if self.frameBorderWidth != '':
            self.frame.config(borderwidth=int(self.frameBorderWidth))
        self.frameRelief = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'relief')
        if self.frameRelief != '':
            self.frame.config(relief=self.frameRelief)




    def DrawButton(self):
        self.buttonAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'anchor')
        self.buttonSizeX = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'size_x')
        self.buttonSizeY = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'size_y')
        self.buttonPosX = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'pos_x')
        self.buttonPosY = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'pos_y')
        self.button = tk.Button(height=int(self.buttonSizeY), width=int(self.buttonSizeX))
        self.button.place(anchor=self.buttonAnchor, height=int(self.buttonSizeY), width=int(self.buttonSizeX),
                          x=int(self.buttonPosX), y=int(self.buttonPosY))

        self.buttonBackgroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                    'background color')
        if self.buttonBackgroundColor != '':
            self.button.config(background=self.buttonBackgroundColor)

        self.buttonBitmap = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'bitmap')
        if self.buttonBitmap != '':
            self.button.config(bitmap=self.buttonBitmap)

        self.buttonText = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'text')
        if self.buttonText != '':
            self.button.config(text=self.buttonText)

        self.buttonBorderWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'borderwidth')
        if self.buttonBorderWidth != '':
            self.button.config(borderwidth=self.buttonBorderWidth)

        self.buttonRelief = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'relief')
        if self.buttonRelief != '':
            self.button.config(relief=self.buttonRelief)

        self.buttonJustify = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'justify')
        if self.buttonJustify != '':
            self.button.config(justify=self.buttonJustify)

        self.buttonTextWrapLength = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                   'wraplength')
        if self.buttonTextWrapLength != '':
            self.button.config(wraplength=self.buttonTextWrapLength)

        self.buttonCmd = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'command')
        if self.buttonCmd != '':
            self.button.config(command=lambda instance = int(self.buttonCmd):
                                gui_controls.callback(self.parent, instance))




    def DrawText(self):
        # Create text widget
        self.text = tk.Text(self.parent)
        # Feed desired text to widget to display
        self.textToDisplay = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'text')
        if self.textToDisplay != "":
            self.text.insert(tk.INSERT, self.textToDisplay)
        # Set word-wrap option
        self.textWrap = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'wrap')
        if self.textWrap != "":
            self.text.config(wrap=self.textWrap)
        self.textBackgroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection,
                                                                  'background color')
        if self.textBackgroundColor != "":
            self.text.config(bg=self.textBackgroundColor)
        self.textPadX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'pad x')
        if self.textPadX != "":
            self.text.config(padx=self.textPadX)
        self.textPadY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'pad y')
        if self.textPadY != "":
            self.text.config(pady=self.textPadY)
        self.textBorderWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'border width')
        if self.textBorderWidth != "":
            self.text.config(bd=self.textBorderWidth)
        self.textFont = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'font')
        self.textFontSize = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'font size')
        if self.textFont != "" and self.textFontSize != "":
            self.text.config(font=(self.textFont, int(self.textFontSize)))

        # Set "place" parameters to place text widget into the correct location in the application window
        self.textAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place anchor')
        self.textSizeX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place width')
        self.textSizeY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place height')
        self.textOffsetX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place offset x')
        self.textOffsetY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place offset y')
        self.text.place(anchor=self.textAnchor, height=int(self.textSizeY), width=int(self.textSizeX),
                          x=int(self.textOffsetX), y=int(self.textOffsetY))
        #self.textBorderMode = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place bordermode')
        #if self.textBorderMode != "":
        #    self.text.config(bordermode=self.textBorderMode)
        #self.textRelHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place relheight')
        #if self.textRelHeight != "":
        #    self.text.config(relheight=self.textRelHeight)
        #self.textRelWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place relwidth')
        #if self.textRelWidth != "":
        #    self.text.config(relwidth=self.textRelWidth)
        #self.textRelX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place rel x')
        #if self.textRelX != "":
        #    self.text.config(relx=self.textRelX)
        #self.textRelY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place rel y')
        #if self.textRelY != "":
        #    self.text.config(rely=self.textRelY)






if __name__ == "__main__":
    app1 = SpawnAppWindow(None)
    app1.title('My OPC Client')
    app1.mainloop()