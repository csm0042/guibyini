import tkinter as tk
import widget_count
import tkinterPlace
import tkinterWindow
import tkinterFrame
import tkinterMessage
import tkinterText
import tkinterButton



class SpawnAppWindow:
    def __init__(self, parent, iniFile):
        self.parent = parent
        self.iniFile = iniFile
        self.section = str()

        self.Window = tkinterWindow.Window()

        # Create tag list for frame settings
        self.frameCount = widget_count.CountWidgetByType(self.iniFile, "frame")
        self.frameDataRead = 0
        self.framesCreated = 0
        self.Frame = [tkinterFrame.Frame() for i in range(self.frameCount)]
        self.FramePlace = [tkinterPlace.Place() for i in range(self.frameCount)]
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]

        # Create tag lists for message settings
        self.messageCount = widget_count.CountWidgetByType(self.iniFile, "message")
        self.messageDataRead = 0
        self.messagesCreated = 0
        self.Message = [tkinterMessage.Message() for i in range(self.messageCount)]
        self.MessagePlace = [tkinterPlace.Place() for i in range(self.messageCount)]
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        
        # Create tag list for text settings
        self.textCount = widget_count.CountWidgetByType(self.iniFile, "Text")
        self.textDataRead = 0
        self.textsCreated = 0
        self.Text = [tkinterText.Text() for i in range(self.textCount)]
        self.TextPlace = [tkinterPlace.Place() for i in range(self.textCount)]
        self.tkText = [tk.Text() for i in range(self.textCount)]

        # Create tag lists for button settings
        self.buttonCount = widget_count.CountWidgetByType(self.iniFile, "button")
        self.buttonDataRead = 0
        self.buttonsCreated = 0
        self.Button = [tkinterButton.Button() for i in range(self.buttonCount)]
        self.ButtonPlace = [tkinterPlace.Place() for i in range(self.buttonCount)]
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]

        # Call function to populate setting tags
        self.initialize()

        # Call function to generate window using obtained settings
        self.build()




    def initialize(self):
        self.Window.section = "main window"
        self.Window.iniFile = self.iniFile
        self.Window = tkinterWindow.Window.read_settings(self.Window)

        for i in range(0, self.frameCount):
            self.Frame[i].iniFile = self.FramePlace[i].iniFile = self.iniFile
            self.Frame[i].section = self.FramePlace[i].section = str("frame" + str(i+1))
            self.Frame[i] = tkinterFrame.Frame.read_settings(self.Frame[i])
            self.FramePlace[i] = tkinterPlace.Place.read_settings(self.FramePlace[i])

        for i in range(0, self.messageCount):
            self.Message[i].iniFile = self.MessagePlace[i].iniFile = self.iniFile
            self.Message[i].section = self.MessagePlace[i].section = "message" + str(i+1)
            self.Message[i] = tkinterMessage.Message.read_settings(self.Message[i])
            self.MessagePlace[i] = tkinterPlace.Place.read_settings(self.MessagePlace[i])
            
        for i in range(0, self.textCount):
            self.Text[i].iniFile = self.TextPlace[i].iniFile = self.iniFile
            self.Text[i].section = self.TextPlace[i].section = str("text" + str(i+1))
            self.Text[i] = tkinterText.Text.read_settings(self.Text[i])
            self.TextPlace[i] = tkinterPlace.Place.read_settings(self.TextPlace[i])

        for i in range(0, self.buttonCount):
            self.Button[i].iniFile = self.ButtonPlace[i].iniFile = self.iniFile
            self.Button[i].section = self.ButtonPlace[i].section = "button" + str(i+1)
            self.Button[i] = tkinterButton.Button.read_settings(self.Button[i])
            self.ButtonPlace[i] = tkinterPlace.Place.read_settings(self.ButtonPlace[i])    


    def build(self):
        self.parent.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height),
                                              int(self.Window.posX), int(self.Window.posY)))
        for i in range(0, self.frameCount):
            self.tkFrame[i] = tk.Frame()
            if self.Frame[i].backgroundColor != '':
                self.tkFrame[i].config(background=self.Frame[i].backgroundColor)
            if self.Frame[i].borderwidth != '':
                self.tkFrame[i].config(borderwidth=int(self.Frame[i].borderwidth))
            if self.Frame[i].colormap != '':
                self.tkFrame[i].config(colormap=self.Frame[i].colormap)
            if self.Frame[i].container != '':
                self.tkFrame[i].config(container=self.Frame[i].container)
            if self.Frame[i].cursor != '':
                self.tkFrame[i].config(cursor=self.Frame[i].cursor)
            if self.Frame[i].height != '':
                self.tkFrame[i].config(height=int(self.Frame[i].height))
            if self.Frame[i].highlightBackgroundColor != '':
                self.tkFrame[i].config(highlightbackground=self.Frame[i].highlightBackgroundColor)
            if self.Frame[i].highlightColor != '':
                self.tkFrame[i].config(highlightcolor=self.Frame[i].highlightColor)
            if self.Frame[i].highlightThickness != '':
                self.tkFrame[i].config(highlightthickness=int(self.Frame[i].highlightThickness))
            if self.Frame[i].padX != '':
                self.tkFrame[i].config(padx=int(self.Frame[i].padX))
            if self.Frame[i].padY != '':
                self.tkFrame[i].config(pady=int(self.Frame[i].padY))
            if self.Frame[i].relief != '':
                self.tkFrame[i].config(relief=self.Frame[i].relief)
            if self.Frame[i].takeFocus != '':
                self.tkFrame[i].config(takefocus=self.Frame[i].takeFocus)
            if self.Frame[i].visual != '':
                self.tkFrame[i].config(visual=self.Frame[i].visual)
            if self.Frame[i].width != '':
                self.tkFrame[i].config(width=int(self.Frame[i].width))

            self.tkFrame[i].place()
            if self.FramePlace[i].anchor != '':
                self.tkFrame[i].place_configure(anchor=self.FramePlace[i].anchor)
            if self.FramePlace[i].borderMode != '':
                self.tkFrame[i].place_configure(bordermode=self.FramePlace[i].borderMode)
            if self.FramePlace[i].height != '':
                self.tkFrame[i].place_configure(height=int(self.FramePlace[i].height))
            if self.FramePlace[i].width != '':
                self.tkFrame[i].place_configure(width=int(self.FramePlace[i].width))
            if self.FramePlace[i].relHeight != '':
                self.tkFrame[i].place_configure(relheight=float(self.FramePlace[i].relHeight))
            if self.FramePlace[i].relWidth != '':
                self.tkFrame[i].place_configure(relwidth=float(self.FramePlace[i].relWidth))
            if self.FramePlace[i].relX != '':
                self.tkFrame[i].place_configure(relx=float(self.FramePlace[i].relX))
            if self.FramePlace[i].relY != '':
                self.tkFrame[i].place_configure(rely=float(self.FramePlace[i].relY))
            if self.FramePlace[i].offsetX != '':
                self.tkFrame[i].place_configure(x=int(self.FramePlace[i].offsetX))
            if self.FramePlace[i].offsetY != '':
                self.tkFrame[i].place_configure(y=int(self.FramePlace[i].offsetY))


        for i in range(0, self.messageCount):
            self.tkMessage[i] = tk.Message()    
            if self.Message[i].anchor != "":
                self.tkMessage[i].config(anchor=self.Message[i].anchor)
            if self.Message[i].aspect != "":
                self.tkMessage[i].config(aspect=self.Message[i].aspect)
            if self.Message[i].backgroundColor != "":
                self.tkMessage[i].config(background=self.Message[i].backgroundColor)
            if self.Message[i].borderwidth != "":
                self.tkMessage[i].config(borderwidth=self.Message[i].borderwidth)
            if self.Message[i].cursor != "":
                self.tkMessage[i].config(cursor=self.Message[i].cursor)
            if self.Message[i].font != "" and self.Message[i].fontSize != "":
                self.tkMessage[i].config(font=(self.Message[i].font, int(self.Message[i].fontSize)))
            if self.Message[i].foregroundColor != "":
                self.tkMessage[i].config(foreground=self.Message[i].foregroundColor)
            if self.Message[i].highlightBackground != "":
                self.tkMessage[i].config(highlightbackground=self.Message[i].highlightBackground)
            if self.Message[i].highlightBackgroundColor != "":
                self.tkMessage[i].config(highlightcolor=self.Message[i].highlightBackgroundColor)
            if self.Message[i].highlightThickness != "":
                self.tkMessage[i].config(highlightthickness=int(self.Message[i].highlightThickness))
            if self.Message[i].justify != "":
                self.tkMessage[i].config(justify=self.Message[i].justify)
            if self.Message[i].padX != "":
                self.tkMessage[i].config(padx=int(self.Message[i].padX))
            if self.Message[i].padY != "":
                self.tkMessage[i].config(pady=int(self.Message[i].padY))
            if self.Message[i].relief != "":
                self.tkMessage[i].config(relief=self.Message[i].relief)
            if self.Message[i].takeFocus != "":
                self.tkMessage[i].config(takefocus=self.Message[i].takeFocus)
            if self.Message[i].text != "":
                self.tkMessage[i].config(text=self.Message[i].text)
            if self.Message[i].textVariable != "":
                self.tkMessage[i].config(textvariable=self.Message[i].textVariable)
            if self.Message[i].width != "":
                self.tkMessage[i].config(width=int(self.Message[i].width))

            self.tkMessage[i].place()
            if self.MessagePlace[i].anchor != '':
                self.tkMessage[i].place_configure(anchor=self.MessagePlace[i].anchor)
            if self.MessagePlace[i].borderMode != '':
                self.tkMessage[i].place_configure(bordermode=self.MessagePlace[i].borderMode)
            if self.MessagePlace[i].height != '':
                self.tkMessage[i].place_configure(height=int(self.MessagePlace[i].height))
            if self.MessagePlace[i].relHeight != '':
                self.tkMessage[i].place_configure(relheight=int(self.MessagePlace[i].relHeight))
            if self.MessagePlace[i].width != '':
                self.tkMessage[i].place_configure(width=int(self.MessagePlace[i].width))
            if self.MessagePlace[i].relWidth != '':
                self.tkMessage[i].place_configure(relwidth=int(self.MessagePlace[i].relWidth))
            if self.MessagePlace[i].relX != '':
                self.tkMessage[i].place_configure(relx=int(self.MessagePlace[i].relX))
            if self.MessagePlace[i].relY != '':
                self.tkMessage[i].place_configure(rely=int(self.MessagePlace[i].relY))
            if self.MessagePlace[i].offsetX != '':
                self.tkMessage[i].place_configure(x=int(self.MessagePlace[i].offsetX))
            if self.MessagePlace[i].offsetY != '':
                self.tkMessage[i].place_configure(y=int(self.MessagePlace[i].offsetY))


        for i in range(0, self.textCount):
            self.tkText[i] = tk.Text()    
            if self.Text[i].autoSeparators != "":
                self.tkText[i].config(autoseparators=self.Text[i].autoSeparators)
            if self.Text[i].backgroundColor != "":
                self.tkText[i].config(bg=self.Text[i].backgroundColor)
            if self.Text[i].backgroundStipple != "":
                self.tkText[i].config(bgstipple=self.Text[i].backgroundStipple)
            if self.Text[i].borderwidth != "":
                self.tkText[i].config(bd=int(self.Text[i].borderwidth))
            if self.Text[i].foregroundStipple != "":
                self.tkText[i].config(fgstipple=self.Text[i].foregroundStipple)
            if self.Text[i].cursor != "":
                self.tkText[i].config(cursor=self.Text[i].cursor)
            if self.Text[i].exportSelection != "":
                self.tkText[i].config(exportselection=self.Text[i].exportSelection)
            if self.Text[i].font != "" and self.Text[i].fontSize != "":
                self.tkText[i].config(font=(self.Text[i].font, int(self.Text[i].fontSize)))
            if self.Text[i].foregroundColor != "":
                self.tkText[i].config(foreground=self.Text[i].foregroundColor)
            if self.Text[i].foregroundStipple != "":
                self.tkText[i].config(fgstipple=self.Text[i].foregroundStipple)
            if self.Text[i].height != "":
                self.tkText[i].config(height=int(self.Text[i].height))
            if self.Text[i].highlightBackgroundColor != "":
                self.tkText[i].config(highlightbackground=self.Text[i].highlightBackgroundColor)
            if self.Text[i].highlightColor != "":
                self.tkText[i].config(highlightcolor=self.Text[i].highlightColor)
            if self.Text[i].highlightThickness != "":
                self.tkText[i].config(highlightthickness=int(self.Text[i].highlightThickness))
            if self.Text[i].insertBackground != "":
                self.tkText[i].config(insertbackground=self.Text[i].insertBackground)
            if self.Text[i].insertBorderwidth != "":
                self.tkText[i].config(insertBorderwidth=int(self.Text[i].insertBorderwidth))
            if self.Text[i].insertOffTime != "":
                self.tkText[i].config(insertOffTime=int(self.Text[i].insertOffTime))
            if self.Text[i].insertOnTime != "":
                self.tkText[i].config(insertOnTime=int(self.Text[i].insertOnTime))
            if self.Text[i].insertWidth != "":
                self.tkText[i].config(insertWidth=int(self.Text[i].insertWidth))
            if self.Text[i].justify != "":
                self.tkText[i].config(justify=self.Text[i].justify)
            if self.Text[i].lmargin1 != "":
                self.tkText[i].config(lmargin1=int(self.Text[i].lmargin1))
            if self.Text[i].tlmargin2 != "":
                self.tkText[i].config(lmargin2=int(self.Text[i].lmargin2))
            if self.Text[i].maxUndo != "":
                self.tkText[i].config(maxundo=int(self.Text[i].maxUndo))
            if self.Text[i].padX != "":
                self.tkText[i].config(padx=int(self.Text[i].padX))
            if self.Text[i].padY != "":
                self.tkText[i].config(PadY=int(self.Text[i].padY))
            if self.Text[i].offset != "":
                self.tkText[i].config(offset=int(self.Text[i].offset))
            if self.Text[i].overstrike != "":
                self.tkText[i].config(overstrike=self.Text[i].overstrike)
            if self.Text[i].relief != "":
                self.tkText[i].config(offset=self.Text[i].relief)
            if self.Text[i].rmargin != "":
                self.tkText[i].config(overstrike=int(self.Text[i].rmargin))
            if self.Text[i].selectBackgroundColor != "":
                self.tkText[i].config(selectbackground=self.Text[i].selectBackgroundColor)
            if self.Text[i].tselectForegroundColor != "":
                self.tkText[i].config(selectforeground=self.Text[i].selectForegroundColor)
            if self.Text[i].selectBorderwidth != "":
                self.tkText[i].config(selectborderwidth=int(self.Text[i].selectBorderwidth))
            if self.Text[i].setGrid != "":
                self.tkText[i].config(setgrid=self.Text[i].SetGrid)
            if self.Text[i].spacing1 != "":
                self.tkText[i].config(spacing1=int(self.Text[i].spacing1))
            if self.Text[i].spacing2 != "":
                self.tkText[i].config(spacing2=int(self.Text[i].spacing2))
            if self.Text[i].spacing3 != "":
                self.tkText[i].config(spacing3=int(self.Text[i].spacing3))
            if self.Text[i].state != "":
                self.tkText[i].config(state=self.Text[i].state)
            if self.Text[i].tabs != "":
                self.tkText[i].config(tabs=self.Text[i].tabs)
            if self.Text[i].takeFocus != "":
                self.tkText[i].config(takefocus=self.Text[i].takeFocus)
            if self.Text[i].text != "":
                self.Text[i].insert(tk.INSERT, self.Text[i].text)
            if self.Text[i].underline != "":
                self.tkText[i].config(underline=self.Text[i].underline)
            if self.Text[i].undo != "":
                self.tkText[i].config(undo=int(self.Text[i].undo))
            if self.Text[i].width != "":
                self.tkText[i].config(width=int(self.Text[i].width))
            if self.Text[i].wrap != "":
                self.tkText[i].config(wrap=self.Text[i].wrap)
            if self.Text[i].xScrollCommand != "":
                self.tkText[i].config(xscrollcommand=int(self.Text[i].xScrollCommand))
            if self.Text[i].yScrollCommand != "":
                self.tkText[i].config(yscrollcommand=int(self.Text[i].yScrollCommand))

            self.tkText[i].place()
            if self.TextPlace[i].anchor != '':
                self.tkText[i].place_configure(anchor=self.TextPlace[i].anchor)
            if self.TextPlace[i].borderMode != '':
                self.tkText[i].place_configure(bordermode=self.TextPlace[i].borderMode)
            if self.TextPlace[i].height != '':
                self.tkText[i].place_configure(height=int(self.TextPlace[i].height))
            if self.TextPlace[i].relHeight != '':
                self.tkText[i].place_configure(relheight=int(self.TextPlace[i].relHeight))
            if self.TextPlace[i].width != '':
                self.tkText[i].place_configure(width=int(self.TextPlace[i].width))
            if self.TextPlace[i].relWidth != '':
                self.tkText[i].place_configure(relwidth=int(self.TextPlace[i].relWidth))
            if self.TextPlace[i].relX != '':
                self.tkText[i].place_configure(relx=int(self.TextPlace[i].relX))
            if self.TextPlace[i].relY != '':
                self.tkText[i].place_configure(rely=int(self.TextPlace[i].relY))
            if self.TextPlace[i].offsetX != '':
                self.tkText[i].place_configure(x=int(self.TextPlace[i].offsetX))
            if self.TextPlace[i].offsetY != '':
                self.tkText[i].place_configure(y=int(self.TextPlace[i].offsetY))
  
        
        for i in range(0, self.buttonCount):
            self.tkButton[i] = tk.Button()             
            if self.Button[i].backgroundColor != '':
                self.tkButton[i].config(background=self.Button[i].backgroundColor)
            if self.Button[i].bitmap != '':
                self.tkButton[i].config(bitmap=self.Button[i].bitmap)
            if self.Button[i].borderwidth != '':
                self.tkButton[i].config(borderwidth=int(self.Button[i].borderwidth))
            if self.Button[i].command != '':
                self.tkButton[i].config(command=lambda instance=int(self.Button[i].command): gui_controls.callback(self.parent, instance))
            if self.Button[i].compound != '':
                self.tkButton[i].config(compound=self.Button[i].compound)
            if self.Button[i].cursor != '':
                self.tkButton[i].config(cursor=self.Button[i].cursor)
            if self.Button[i].default != '':
                self.tkButton[i].config(default=self.Button[i].default)
            if self.Button[i].disableForeground != '':
                self.tkButton[i].config(disableforeground=self.Button[i].disableForeground)
            if self.Button[i].font != '' and self.Button[i].fontSize != '':
                self.tkButton[i].config(font=(self.Button[i].font, int(self.Button[i].fontSize)))
            if self.Button[i].foregroundColor != '':
                self.tkButton[i].config(foreground=self.Button[i].foregroundColor)
            if self.Button[i].height != '':
                self.tkButton[i].config(height=int(self.Button[i].height))
            if self.Button[i].highlightBackgroundColor != '':
                self.tkButton[i].config(highlightbackground=self.Button[i].highlightBackgroundColor)
            if self.Button[i].highlightColor != '':
                self.tkButton[i].config(highlightcolor=self.Button[i].highlightColor)
            if self.Button[i].highlightThickness != '':
                self.tkButton[i].config(highlightthickness=int(self.Button[i].highlightThickness))
            if self.Button[i].image != '':
                self.tkButton[i].config(image=self.Button[i].image)
            if self.Button[i].justify != '':
                self.tkButton[i].config(justify=self.Button[i].justify)
            if self.Button[i].overRelief != '':
                self.tkButton[i].config(overrelief=self.Button[i].overRelief)
            if self.Button[i].padX != '':
                self.tkButton[i].config(padx=int(self.Button[i].padX))
            if self.Button[i].padY != '':
                self.tkButton[i].config(pady=int(self.Button[i].padY))
            if self.Button[i].relief != '':
                self.tkButton[i].config(relief=self.Button[i].relief)
            if self.Button[i].repeatDelay != '':
                self.tkButton[i].config(repeatdelay=int(self.Button[i].repeatDelay))
            if self.Button[i].repeatInterval != '':
                self.tkButton[i].config(repeatinterval=int(self.Button[i].repeatInterval))
            if self.Button[i].state != '':
                self.tkButton[i].config(state=self.Button[i].state)
            if self.Button[i].takeFocus != '':
                self.tkButton[i].config(takefocus=self.Button[i].takeFocus)
            if self.Button[i].text != '':
                self.tkButton[i].config(text=self.Button[i].text)
            if self.Button[i].textVariable != '':
                self.tkButton[i].config(textvariable=self.Button[i].textVariable)
            if self.Button[i].underline != '':
                self.tkButton[i].config(underline=self.Button[i].underline)
            if self.Button[i].width != '':
                self.tkButton[i].config(width=int(self.Button[i].width))
            if self.Button[i].wrapLength != '':
                self.tkButton[i].config(wraplength=int(self.Button[i].wrapLength))
            
            self.tkButton[i].place()            
            if self.ButtonPlace[i].anchor != '':
                self.tkButton[i].place_configure(anchor=self.ButtonPlace[i].anchor)
            if self.ButtonPlace[i].borderMode != '':
                self.tkButton[i].place_configure(bordermode=self.ButtonPlace[i].borderMode)
            if self.ButtonPlace[i].height != '':
                self.tkButton[i].place_configure(height=int(self.ButtonPlace[i].height))
            if self.ButtonPlace[i].width != '':
                self.tkButton[i].place_configure(width=int(self.ButtonPlace[i].width))
            if self.ButtonPlace[i].relHeight != '':
                self.tkButton[i].place_configure(relheight=int(self.ButtonPlace[i].relHeight))
            if self.ButtonPlace[i].relWidth != '':
                self.tkButton[i].place_configure(relwidth=int(self.ButtonPlace[i].relWidth))
            if self.ButtonPlace[i].relX != '':
                self.tkButton[i].place_configure(relx=int(self.ButtonPlace[i].relX))
            if self.ButtonPlace[i].relY != '':
                self.tkButton[i].place_configure(rely=int(self.ButtonPlace[i].relY))
            if self.ButtonPlace[i].offsetX != '':
                self.tkButton[i].place_configure(x=int(self.ButtonPlace[i].offsetX))
            if self.ButtonPlace[i].offsetY != '':
                self.tkButton[i].place_configure(y=int(self.ButtonPlace[i].offsetY))
        
        
        
if __name__ == "__main__":
    root=tk.Tk()
    app = SpawnAppWindow(root, 'gui.ini')
    root.title('My App Window')
    root.mainloop()