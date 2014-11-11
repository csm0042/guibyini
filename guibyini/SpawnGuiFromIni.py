import tkinter as tk
import config_parser
import widget_count
import gui_controls
import parseFromIni


class SpawnAppWindow:
    def __init__(self, parent, iniFile):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.iniFile = iniFile
        self.windowSection = str()
        self.frameCount = widget_count.CountWidgetByType(self.iniFile, "frame")
        self.frameDataRead = 0
        self.framesCreated = 0
        self.frameSection = str()
        self.frameSettings = [FrameWidget()]
        self.framesPlace = [PlaceSettings()]
        self.messageCount = widget_count.CountWidgetByType(self.iniFile, "message")
        self.messageDataRead = 0
        self.messagesCreated = 0
        self.messagesSection = str()
        self.messageSettings = [MessageWidget()]
        self.messagesPlace = [PlaceSettings()]
        self.textCount = widget_count.CountWidgetByType(self.iniFile, "text")
        self.textDataRead = 0
        self.textCreated = 0
        self.textSection = str()
        self.textSettings = [TextWidget()]
        self.textPlace = [PlaceSettings()]
        self.buttonCount = widget_count.CountWidgetByType(self.iniFile, "button")
        self.buttonDataRead = 0
        self.buttonsCreated = 0
        self.buttonsSection = str()
        self.buttonSettings = [ButtonWidget()]
        self.buttonsPlace = [PlaceSettings()]
        self.initialize()
        self.build()



    def initialize(self):
        while self.frameDataRead < self.frameCount:
            self.frameDataRead += 1
            self.frameSection = "frame" + str(self.frameDataRead)
            if self.frameDataRead <= 1:
                self.frameSettings = parseFromIni.FrameWidget.GetFrameSettings(self.iniFile, self.frameSection)
                self.framesPlace = parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.frameSection)
            else:
                self.frameSettings.append(parseFromIni.FrameWidget.GetFrameSettings(self.iniFile, self.frameSection))
                self.framesPlace.append(parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.frameSection))

        while self.messageDataRead < self.messageCount:
            self.messageDataRead += 1
            self.messageSection = "message" + str(self.messageDataRead)
            if self.messageDataRead <= 1:
                self.messageSettings = parseFromIni.messageWidget.GetmessageSettings(self.iniFile, self.messageSection)
                self.messagesPlace = parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.messageSection)
            else:
                self.messageSettings.append(parseFromIni.messageWidget.GetmessageSettings(self.iniFile,
                                                                                          self.messageSection))
                self.messagesPlace.append(parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile,
                                                                                      self.messageSection))
        while self.textDataRead < self.textCount:
            self.textDataRead += 1
            self.textSection = "text" + str(self.textDataRead)
            if self.textDataRead <= 1:
                self.textSettings = parseFromIni.textWidget.GettextSettings(self.iniFile, self.textSection)
                self.textsPlace = parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.textSection)
            else:
                self.textSettings.append(parseFromIni.textWidget.GettextSettings(self.iniFile, self.textSection))
                self.textsPlace.append(parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.textSection))

        while self.buttonDataRead < self.buttonCount:
            self.buttonDataRead += 1
            self.buttonSection = "button" + str(self.buttonDataRead)
            if self.buttonDataRead <= 1:
                self.buttonSettings = parseFromIni.buttonWidget.GetbuttonSettings(self.iniFile, self.buttonSection)
                self.buttonsPlace = parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile, self.buttonSection)
            else:
                self.buttonSettings.append(parseFromIni.buttonWidget.GetbuttonSettings(self.iniFile,
                                                                                       self.buttonSection))
                self.buttonsPlace.append(parseFromIni.PlaceSettings.GetPlaceSettings(self.iniFile,
                                                                                     self.buttonSection))


    def build(self):
        self.DrawWindow()
        while self.framesCreated < self.frameCount:
            self.framesCreated += 1
            self.frameSection = "frame" + str(self.framesCreated)
            if self.framesCreated <= 1:
                self.frame = tk.Frame().place()
            else:
                self.frame.append(tk.Frame().place())
            self.ConfigureFrame()
        while self.messagesCreated < self.messageCount:
            self.messagesCreated += 1
            self.messageSection = 'message' + str(self.messagesCreated)
            if self.messagesCreated <= 1:
                self.message = tk.Message().place()
            else:
                self.message.append(tk.Message().place())
            self.ConfigureMessage()
        while self.textCreated < self.textCount:
            self.textCreated += 1
            self.textSection = 'text' + str(self.textCreated)
            if self.textCreated <= 1:
                self.text = tk.Text().place()
            else:
                self.text.append(tk.Text().place())
            self.ConfigureText()
        while self.buttonsCreated < self.buttonCount:
            self.buttonsCreated += 1
            self.buttonsSection = 'button' + str(self.buttonsCreated)
            if self.buttonsCreated <= 1:
                self.button = tk.Button().place()
            else:
                self.button.append(tk.Button().place())
            self.ConfigureButton()



    def DrawWindow(self):
        self.appWindowFrameSizeX = int(config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'size_x'))
        self.appWindowFrameSizeY = int(config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'size_y'))
        self.appWindowPosX = int(config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'pos_x'))
        self.appWindowPosY = int(config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'pos_y'))
        self.parent.geometry("%sx%s+%s+%s" % (self.appWindowFrameSizeX, self.appWindowFrameSizeY, self.appWindowPosX,
                                              self.appWindowPosY))
        self.appWindowTitle = config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'title')
        self.parent.title(self.appWindowTitle)
        self.appWindowColor = config_parser.ConfigSectionMap(self.iniFile, self.windowSection, 'color')
        self.parent.configure(background=self.appWindowColor)


    def ConfigureFrame(self):
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


    def ConfigureMessage(self):
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




    def ConfigureText(self):
        if self.textAutoSeparators != "":
            self.text.config(autoseparators=self.textAutoSeparators)
        if self.textBackgroundColor != "":
            self.text.config(bg=self.textBackgroundColor)
        if self.textBgStipple != "":
            self.text.config(bgstipple=self.textBgStipple)
        if self.textBorderWidth != "":
            self.text.config(bd=int(self.textBorderWidth))
        if self.textFgStipple != "":
            self.text.config(fgstipple=self.textFgStipple)
        if self.textCursor != "":
            self.text.config(cursor=self.textCursor)
        if self.textExportSelection != "":
            self.text.config(exportselection=self.textExportSelection)
        if self.textFont != "" and self.textFontSize != "":
            self.text.config(font=(self.textFont, int(self.textFontSize)))
        if self.textForegroundColor != "":
            self.text.config(foreground=self.textForegroundColor)
        if self.textForegroundStipple != "":
            self.text.config(fgstipple=self.textForegroundStipple)
        if self.textHeight != "":
            self.text.config(height=int(self.textHeight))
        if self.textHighlightBackground != "":
            self.text.config(highlightbackground=self.textHighlightBackground)
        if self.textHighlightColor != "":
            self.text.config(highlightcolor=self.textHighlightColor)
        if self.textHighlightThickness != "":
            self.text.config(highlightthickness=int(self.textHighlightThickness))
        if self.textInsertBackground != "":
            self.text.config(insertbackground=self.textInsertBackground)
        if self.textInsertBorderwidth != "":
            self.text.config(insertBorderwidth=int(self.textInsertBorderwidth))
        if self.textInsertOffTime != "":
            self.text.config(insertOffTime=int(self.textInsertOffTime))
        if self.textInsertOnTime != "":
            self.text.config(insertOnTime=int(self.textInsertOnTime))
        if self.textInsertWidth != "":
            self.text.config(insertWidth=int(self.textInsertWidth))
        if self.textJustify != "":
            self.text.config(justify=self.textJustify)
        if self.textLmargin1 != "":
            self.text.config(lmargin1=int(self.textLmargin1))
        if self.textLmargin2 != "":
            self.text.config(lmargin2=int(self.textLmargin2))
        if self.textMaxUndo != "":
            self.text.config(maxundo=int(self.textMaxUndo))
        if self.textPadX != "":
            self.text.config(padx=int(self.textPadX))
        if self.textPadY != "":
            self.text.config(PadY=int(self.textPadY))
        if self.textOffset != "":
            self.text.config(offset=int(self.textOffset))
        if self.textOverstrike != "":
            self.text.config(overstrike=self.textOverstrike)
        if self.textRelief != "":
            self.text.config(offset=self.textRelief)
        if self.textRmargin != "":
            self.text.config(overstrike=int(self.textRmargin))
        if self.textSelectBackgroundColor != "":
            self.text.config(selectbackground=self.textSelectBackgroundColor)
        if self.textSelectForegroundColor != "":
            self.text.config(selectforeground=self.textSelectForegroundColor)
        if self.textSelectBorderwidth != "":
            self.text.config(selectborderwidth=int(self.textSelectBorderwidth))
        if self.textSetGrid != "":
            self.text.config(setgrid=self.textSetGrid)
        if self.textSpacing1 != "":
            self.text.config(spacing1=int(self.textSpacing1))
        if self.textSpacing2 != "":
            self.text.config(spacing2=int(self.textSpacing2))
        if self.textSpacing3 != "":
            self.text.config(spacing3=int(self.textSpacing3))
        if self.textState != "":
            self.text.config(state=self.textState)
        if self.textTabs != "":
            self.text.config(tabs=self.textTabs)
        if self.textTakeFocus != "":
            self.text.config(takefocus=self.textTakeFocus)
        if self.textToDisplay != "":
            self.text.insert(tk.INSERT, self.textToDisplay)
        if self.textUnderline != "":
            self.text.config(underline=self.textUnderline)
        if self.textUndo != "":
            self.text.config(undo=int(self.textUndo))
        if self.textWidth != "":
            self.text.config(width=int(self.textWidth))
        if self.textWrap != "":
            self.text.config(wrap=self.textWrap)
        if self.textScrollX != "":
            self.text.config(xscrollcommand=int(self.textScrollX))
        if self.textScrollY != "":
            self.text.config(yscrollcommand=int(self.textScrollY))
        if self.textPlaceAnchor != '':
            self.text.place_configure(anchor=self.textPlaceAnchor)
        if self.textPlaceBordermode != '':
            self.text.place_configure(bordermode=self.textPlaceBordermode)
        if self.textPlaceHeight != '':
            self.text.place_configure(height=int(self.textPlaceHeight))
        if self.textPlaceRelHeight != '':
            self.text.place_configure(relheight=int(self.textPlaceRelHeight))
        if self.textPlaceWidth != '':
            self.text.place_configure(width=int(self.textPlaceWidth))
        if self.textPlaceRelWidth != '':
            self.text.place_configure(relwidth=int(self.textPlaceRelWidth))
        if self.textPlaceRelX != '':
            self.text.place_configure(relx=int(self.textPlaceRelX))
        if self.textPlaceRelY != '':
            self.text.place_configure(rely=int(self.textPlaceRelY))
        if self.textPlaceOffsetX != '':
            self.text.place_configure(x=int(self.textPlaceOffsetX))
        if self.textPlaceOffsetY != '':
            self.text.place_configure(y=int(self.textPlaceOffsetY))




    def ConfigureButton(self):
        if self.buttonSettings[self.buttonsCreated].backgroundColor != '':
            self.button.config(background=self.buttonSettings[self.buttonsCreated].backgroundColor)
        if self.buttonBitmap != '':
            self.button.config(bitmap=self.buttonBitmap)
        if self.buttonBorderwidth != '':
            self.button.config(borderwidth=int(self.buttonBorderwidth))
        if self.buttonCommand != '':
            self.button.config(command=lambda instance=int(self.buttonCommand): gui_controls.callback(self.parent, instance))
        if self.buttonCompound != '':
            self.button.config(compound=self.buttonCompound)
        if self.buttonCursor != '':
            self.button.config(cursor=self.buttonCursor)
        if self.buttonDefault != '':
            self.button.config(default=self.buttonDefault)
        if self.buttonDisableForeground != '':
            self.button.config(disableforeground=self.buttonDisableForeground)
        if self.buttonFont != '':
            self.button.config(font=(self.buttonFont, int(self.buttonFontSize)))
        if self.buttonForegroundColor != '':
            self.button.config(foreground=self.buttonForegroundColor)
        if self.buttonHeight != '':
            self.button.config(height=int(self.buttonHeight))
        if self.buttonHighlightBackground != '':
            self.button.config(highlightbackground=self.buttonCommand)
        if self.buttonHighlightColor != '':
            self.button.config(highlightcolor=self.buttonCommand)
        if self.buttonHighlightThickness != '':
            self.button.config(highlightthickness=int(self.buttonHighlightThickness))
        if self.buttonImage != '':
            self.button.config(image=self.buttonImage)
        if self.buttonJustify != '':
            self.button.config(justify=self.buttonJustify)
        if self.buttonOverRelief != '':
            self.button.config(overrelief=self.buttonOverRelief)
        if self.buttonPadX != '':
            self.button.config(padx=int(self.buttonPadX))
        if self.buttonPadY != '':
            self.button.config(pady=int(self.buttonPadY))
        if self.buttonRelief != '':
            self.button.config(relief=self.buttonRelief)
        if self.buttonRepeatDelay != '':
            self.button.config(repeatdelay=int(self.buttonRepeatDelay))
        if self.buttonRepeatInterval != '':
            self.button.config(repeatinterval=int(self.buttonRepeatInterval))
        if self.buttonState != '':
            self.button.config(state=self.buttonState)
        if self.buttonTakeFocus != '':
            self.button.config(takefocus=self.buttonTakeFocus)
        if self.buttonText != '':
            self.button.config(text=self.buttonText)
        if self.buttonTextVariable != '':
            self.button.config(textvariable=self.buttonTextVariable)
        if self.buttonUnderline != '':
            self.button.config(underline=self.buttonUnderline)
        if self.buttonWidth != '':
            self.button.config(width=int(self.buttonWidth))
        if self.buttonWrapLength != '':
            self.button.config(wraplength=int(self.buttonWrapLength))
        if self.buttonPlaceAnchor != '':
            self.button.place_configure(anchor=self.buttonPlaceAnchor)
        if self.buttonPlaceBordermode != '':
            self.button.place_configure(bordermode=self.buttonPlaceBordermode)
        if self.buttonPlaceHeight != '':
            self.button.place_configure(height=int(self.buttonPlaceHeight))
        if self.buttonPlaceWidth != '':
            self.button.place_configure(width=int(self.buttonPlaceWidth))
        if self.buttonPlaceRelHeight != '':
            self.button.place_configure(relheight=int(self.buttonPlaceRelHeight))
        if self.buttonPlaceRelWidth != '':
            self.button.place_configure(relwidth=int(self.buttonPlaceRelWidth))
        if self.buttonPlaceRelX != '':
            self.button.place_configure(relx=int(self.buttonPlaceRelX))
        if self.buttonPlaceRelY != '':
            self.button.place_configure(rely=int(self.buttonPlaceRelY))
        if self.buttonPlaceOffsetX != '':
            self.button.place_configure(x=int(self.buttonPlaceOffsetX))
        if self.buttonPlaceOffsetY != '':
            self.button.place_configure(y=int(self.buttonPlaceOffsetY))




if __name__ == "__main__":
    root=tk.Tk()
    app = SpawnAppWindow(root, 'GuiConfig.ini')
    app.title('My OPC Client')
    app.mainloop()