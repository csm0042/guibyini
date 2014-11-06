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
        global appRunning
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
        self.frameBackgroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'background color')
        self.frameBorderwidth = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'borderwidth')
        self.frameClass = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'class')
        self.frameColormap = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'colormap')
        self.frameContainer = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'container')
        self.frameCursor = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'cursor')
        self.frameHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'height')
        self.frameHighlightBackground = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'highlight background')
        self.frameHighlightColor = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'highlight color')
        self.frameHighlightThickness = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'highlight thickness')
        self.framePadX = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'padx')
        self.framePadY = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'pady')
        self.frameRelief = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'relief')
        self.frameTakeFocus = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'take focus')
        self.frameVisual = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'visual')
        self.frameWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'width')
        self.frame = tk.Frame()
        if self.frameBackgroundColor != '': self.frame.config(background=self.frameBackgroundColor)
        if self.frameBorderwidth != '': self.frame.config(borderwidth=int(self.frameBorderwidth))
        #if self.frameClass != '': self.frame.config(class=self.frameClass)
        if self.frameColormap != '': self.frame.config(colormap=self.frameColormap)
        if self.frameContainer != '': self.frame.config(container=self.frameContainer)
        if self.frameCursor != '': self.frame.config(cursor=self.frameCursor)
        if self.frameHeight != '': self.frame.config(height=int(self.frameHeight))
        if self.frameHighlightBackground != '': self.frame.config(highlightbackground=self.frameHighlightBackground)
        if self.frameHighlightColor != '': self.frame.config(highlightcolor=self.frameHighlightColor)
        if self.frameHighlightThickness != '': self.frame.config(highlightthickness=int(self.frameHighlightThickness))
        if self.framePadX != '': self.frame.config(padx=int(self.framePadX))
        if self.framePadY != '': self.frame.config(pady=int(self.framePadY))
        if self.frameRelief != '': self.frame.config(relief=self.frameRelief)
        if self.frameTakeFocus != '': self.frame.config(takefocus=self.frameTakeFocus)
        if self.frameVisual != '': self.frame.config(visual=self.frameVisual)
        if self.frameWidth != '': self.frame.config(width=int(self.frameWidth))

        # Pull frame widget place parameters from INI file and apply them to frame widget
        self.framePlaceAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'place anchor')
        self.framePlaceBordermode = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection,
                                                                    'place bordermode')
        self.framePlaceHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'place height')
        self.framePlaceWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'place width')
        self.framePlaceRelHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection,
                                                                   'place relheight')
        self.framePlaceRelWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection,
                                                                  'place relwidth')
        self.framePlaceRelX = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'place rel x')
        self.framePlaceRelY = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection, 'place rel y')
        self.framePlaceOffsetX = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection,
                                                                 'place offset x')
        self.framePlaceOffsetY = config_parser.ConfigSectionMap(self.windowIniFile, self.frameSection,
                                                                 'place offset y')
        self.frame.place()
        if self.framePlaceAnchor != '': self.frame.place_configure(anchor=self.framePlaceAnchor)
        if self.framePlaceBordermode != '': self.frame.place_configure(bordermode=self.framePlaceBordermode)
        if self.framePlaceHeight != '': self.frame.place_configure(height=int(self.framePlaceHeight))
        if self.framePlaceRelHeight != '': self.frame.place_configure(relheight=int(self.framePlaceRelHeight))
        if self.framePlaceWidth != '': self.frame.place_configure(width=int(self.framePlaceWidth))
        if self.framePlaceRelWidth != '': self.frame.place_configure(relwidth=int(self.framePlaceRelWidth))
        if self.framePlaceOffsetX != '': self.frame.place_configure(x=int(self.framePlaceOffsetX))
        if self.framePlaceRelX != '': self.frame.place_configure(relx=int(self.framePlaceRelX))
        if self.framePlaceOffsetY != '': self.frame.place_configure(y=int(self.framePlaceOffsetY))
        if self.framePlaceRelY != '': self.frame.place_configure(rely=int(self.framePlaceRelY))




    def DrawButton(self):
        global appRunning
        self.buttonBackgroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                    'background color')
        self.buttonBitmap = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'bitmap')
        self.buttonBorderwidth = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'borderwidth')
        self.buttonCommand = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'command')
        self.buttonCompound = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'compound')
        self.buttonCursor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'cursor')
        self.buttonDefault = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'default')
        self.buttonDisableForeground = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                      'disable foreground')
        self.buttonFont = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'font')
        self.buttonFontSize = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'font size')
        self.buttonForegroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                    'foreground color')
        self.buttonHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'height')
        self.buttonHighlightBackground = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                        'highlight background')
        self.buttonHighlightColor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                   'highlight color')
        self.buttonHighlightThickness = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                       'highlight thinkness')
        self.buttonImage = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'image')
        self.buttonJustify = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'justify')
        self.buttonOverRelief = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'over relief')
        self.buttonPadX = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'padx')
        self.buttonPadY = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'pady')
        self.buttonRelief = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'relief')
        self.buttonRepeatDelay = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'repeat delay')
        self.buttonRepeatInterval = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                   'repeat interval')
        self.buttonState = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'state')
        self.buttonTakeFocus = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'take focus')
        self.buttonText = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'text')
        self.buttonTextVariable = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                 'text variable')
        self.buttonUnderline = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'underline')
        self.buttonWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'width')
        self.buttonWrapLength = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'wrap length')

        self.button = tk.Button()
        if self.buttonBackgroundColor != '': self.button.config(background=self.buttonBackgroundColor)
        if self.buttonBitmap != '': self.button.config(bitmap=self.buttonBitmap)
        if self.buttonBorderwidth != '': self.button.config(borderwidth=int(self.buttonBorderwidth))
        if self.buttonCommand != '': self.button.config(command=lambda instance=int(self.buttonCommand):
                                                        gui_controls.callback(self.parent, instance))
        if self.buttonCompound != '': self.button.config(compound=self.buttonCompound)
        if self.buttonCursor != '': self.button.config(cursor=self.buttonCursor)
        if self.buttonDefault != '': self.button.config(default=self.buttonDefault)
        if self.buttonDisableForeground != '': self.button.config(disableforeground=self.buttonDisableForeground)
        if self.buttonFont != '': self.button.config(font=(self.buttonFont, int(self.buttonFontSize)))
        if self.buttonForegroundColor != '': self.button.config(foreground=self.buttonForegroundColor)
        if self.buttonHeight != '': self.button.config(height=int(self.buttonHeight))
        if self.buttonHighlightBackground != '': self.button.config(highlightbackground=self.buttonCommand)
        if self.buttonHighlightColor != '': self.button.config(highlightcolor=self.buttonCommand)
        if self.buttonHighlightThickness != '': self.button.config(highlightthickness=int(self.buttonHighlightThickness))
        if self.buttonImage != '': self.button.config(image=self.buttonImage)
        if self.buttonJustify != '': self.button.config(justify=self.buttonJustify)
        if self.buttonOverRelief != '': self.button.config(overrelief=self.buttonOverRelief)
        if self.buttonPadX != '': self.button.config(padx=int(self.buttonPadX))
        if self.buttonPadY != '': self.button.config(pady=int(self.buttonPadY))
        if self.buttonRelief != '': self.button.config(relief=self.buttonRelief)
        if self.buttonRepeatDelay != '': self.button.config(repeatdelay=int(self.buttonRepeatDelay))
        if self.buttonRepeatInterval != '': self.button.config(repeatinterval=int(self.buttonRepeatInterval))
        if self.buttonState != '': self.button.config(state=self.buttonState)
        if self.buttonTakeFocus != '': self.button.config(takefocus=self.buttonTakeFocus)
        if self.buttonText != '': self.button.config(text=self.buttonText)
        if self.buttonTextVariable != '': self.button.config(textvariable=self.buttonTextVariable)
        if self.buttonUnderline != '': self.button.config(underline=int(self.buttonUnderline))
        if self.buttonWidth != '': self.button.config(width=int(self.buttonWidth))
        if self.buttonWrapLength != '': self.button.config(wraplength=int(self.buttonWrapLength))

        # Pull button widget place parameters from INI file and apply them to button widget
        self.buttonPlaceAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'place anchor')
        self.buttonPlaceBordermode = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                    'place bordermode')
        self.buttonPlaceHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'place height')
        self.buttonPlaceWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'place width')
        self.buttonPlaceRelHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                   'place relheight')
        self.buttonPlaceRelWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                  'place relwidth')
        self.buttonPlaceRelX = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'place rel x')
        self.buttonPlaceRelY = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection, 'place rel y')
        self.buttonPlaceOffsetX = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                 'place offset x')
        self.buttonPlaceOffsetY = config_parser.ConfigSectionMap(self.windowIniFile, self.buttonSection,
                                                                 'place offset y')
        self.button.place()
        if self.buttonPlaceAnchor != '': self.button.place_configure(anchor=self.buttonPlaceAnchor)
        if self.buttonPlaceBordermode != '': self.button.place_configure(bordermode=self.buttonPlaceBordermode)
        if self.buttonPlaceHeight != '': self.button.place_configure(height=int(self.buttonPlaceHeight))
        if self.buttonPlaceRelHeight != '': self.button.place_configure(relheight=int(self.buttonPlaceRelHeight))
        if self.buttonPlaceWidth != '': self.button.place_configure(width=int(self.buttonPlaceWidth))
        if self.buttonPlaceRelWidth != '': self.button.place_configure(relwidth=int(self.buttonPlaceRelWidth))
        if self.buttonPlaceOffsetX != '': self.button.place_configure(x=int(self.buttonPlaceOffsetX))
        if self.buttonPlaceRelX != '': self.button.place_configure(relx=int(self.buttonPlaceRelX))
        if self.buttonPlaceOffsetY != '': self.button.place_configure(y=int(self.buttonPlaceOffsetY))
        if self.buttonPlaceRelY != '': self.button.place_configure(rely=int(self.buttonPlaceRelY))





    def DrawText(self):
        # Pull configuration from INI file for text field
        self.textToDisplay = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'text')
        self.textWrap = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'wrap')
        self.textBackgroundColor = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection,
                                                                  'background color')
        self.textPadX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'pad x')
        self.textPadY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'pad y')
        self.textBorderWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'border width')
        self.textFont = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'font')
        self.textFontSize = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'font size')
        self.text = tk.Text()
        if self.textToDisplay != "": self.text.insert(tk.INSERT, self.textToDisplay)
        if self.textWrap != "": self.text.config(wrap=self.textWrap)
        if self.textBackgroundColor != "": self.text.config(bg=self.textBackgroundColor)
        if self.textPadX != "": self.text.config(padx=self.textPadX)
        if self.textPadY != "": self.text.config(pady=self.textPadY)
        if self.textBorderWidth != "": self.text.config(bd=self.textBorderWidth)
        if self.textFont != "" and self.textFontSize != "": self.text.config(font=(self.textFont,
                                                                                   int(self.textFontSize)))
        # Pull text widget place parameters from INI file and apply them to text widget
        self.textPlaceAnchor = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place anchor')
        self.textPlaceBordermode = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection,
                                                                  'place bordermode')
        self.textPlaceHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place height')
        self.textPlaceWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place width')
        self.textPlaceRelHeight = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection,
                                                                 'place relheight')
        self.textPlaceRelWidth = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place relwidth')
        self.textPlaceRelX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place rel x')
        self.textPlaceRelY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place rel y')
        self.textPlaceOffsetX = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place offset x')
        self.textPlaceOffsetY = config_parser.ConfigSectionMap(self.windowIniFile, self.textSection, 'place offset y')
        self.text.place()
        if self.textPlaceAnchor != '': self.text.place_configure(anchor=self.textPlaceAnchor)
        if self.textPlaceBordermode != '': self.text.place_configure(bordermode=self.textPlaceBordermode)
        if self.textPlaceHeight != '': self.text.place_configure(height=int(self.textPlaceHeight))
        if self.textPlaceRelHeight != '': self.text.place_configure(relheight=int(self.textPlaceRelHeight))
        if self.textPlaceWidth != '': self.text.place_configure(width=int(self.textPlaceWidth))
        if self.textPlaceRelWidth != '': self.text.place_configure(relwidth=int(self.textPlaceRelWidth))
        if self.textPlaceOffsetX != '': self.text.place_configure(x=int(self.textPlaceOffsetX))
        if self.textPlaceRelX != '': self.text.place_configure(relx=int(self.textPlaceRelX))
        if self.textPlaceOffsetY != '': self.text.place_configure(y=int(self.textPlaceOffsetY))
        if self.textPlaceRelY != '': self.text.place_configure(rely=int(self.textPlaceRelY))




if __name__ == "__main__":
    app1 = SpawnAppWindow(None)
    app1.title('My OPC Client')
    app1.mainloop()