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
        #self.Frame = [tkinterFrame.Frame() for i in range(self.frameCount)]
        self.Frame = tkinterFrame.Frame()
        #self.FramePlace = [tkinterPlace.Place() for i in range(self.frameCount)]
        self.FramePlace = tkinterPlace.Place()
        #self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
        self.tkFrame = tk.Frame()

        # Create tag lists for message settings
        self.messageCount = widget_count.CountWidgetByType(self.iniFile, "message")
        self.messageDataRead = 0
        self.messagesCreated = 0
        #self.Message = [tkinterMessage.Message() for i in range(self.messageCount)]
        self.Message = tkinterMessage.Message()
        #self.MessagePlace = [tkinterPlace.Place() for i in range(self.messageCount)]
        self.MessagePlace = tkinterPlace.Place()
        #self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        self.tkMessage = tk.Message()
        
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
        #self.Button = [tkinterButton.Button() for i in range(self.buttonCount)]
        self.Button = tkinterButton.Button()
        #self.ButtonPlace = [tkinterPlace.Place() for i in range(self.buttonCount)]
        self.ButtonPlace = tkinterPlace.Place()
        #self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        self.tkButton = tk.Button()

        # Call function to populate setting tags
        self.initialize()

        # Call function to generate window using obtained settings
        # self.build()




    def initialize(self):
        self.Window.section = "main window"
        self.Window.iniFile = self.iniFile
        self.Window = tkinterWindow.Window.read_settings(self.Window)
        self.parent.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height),
                                              int(self.Window.posX), int(self.Window.posY)))
        if self.Window.backgroundColor != "":
            self.parent.config(background=self.Window.backgroundColor)

        for i in range(0, self.frameCount):
            self.Frame.iniFile = self.FramePlace.iniFile = self.iniFile
            self.Frame.section = self.FramePlace.section = str("frame" + str(i+1))
            
            self.Frame = tkinterFrame.Frame.read_settings(self.Frame)
            self.tkFrame = tk.Frame()
            if self.Frame.backgroundColor != '':
                self.tkFrame.config(background=self.Frame.backgroundColor)
            if self.Frame.borderwidth != '':
                self.tkFrame.config(borderwidth=int(self.Frame.borderwidth))
            if self.Frame.colormap != '':
                self.tkFrame.config(colormap=self.Frame.colormap)
            if self.Frame.container != '':
                self.tkFrame.config(container=self.Frame.container)
            if self.Frame.cursor != '':
                self.tkFrame.config(cursor=self.Frame.cursor)
            if self.Frame.height != '':
                self.tkFrame.config(height=int(self.Frame.height))
            if self.Frame.highlightBackgroundColor != '':
                self.tkFrame.config(highlightbackground=self.Frame.highlightBackgroundColor)
            if self.Frame.highlightColor != '':
                self.tkFrame.config(highlightcolor=self.Frame.highlightColor)
            if self.Frame.highlightThickness != '':
                self.tkFrame.config(highlightthickness=int(self.Frame.highlightThickness))
            if self.Frame.padX != '':
                self.tkFrame.config(padx=int(self.Frame.padX))
            if self.Frame.padY != '':
                self.tkFrame.config(pady=int(self.Frame.padY))
            if self.Frame.relief != '':
                self.tkFrame.config(relief=self.Frame.relief)
            if self.Frame.takeFocus != '':
                self.tkFrame.config(takefocus=self.Frame.takeFocus)
            if self.Frame.visual != '':
                self.tkFrame.config(visual=self.Frame.visual)
            if self.Frame.width != '':
                self.tkFrame.config(width=int(self.Frame.width))
                
            self.FramePlace = tkinterPlace.Place.read_settings(self.FramePlace)
            self.tkFrame.place()
            if self.FramePlace.anchor != '':
                self.tkFrame.place_configure(anchor=self.FramePlace.anchor)
            if self.FramePlace.borderMode != '':
                self.tkFrame.place_configure(bordermode=self.FramePlace.borderMode)
            if self.FramePlace.height != '':
                self.tkFrame.place_configure(height=int(self.FramePlace.height))
            if self.FramePlace.width != '':
                self.tkFrame.place_configure(width=int(self.FramePlace.width))
            if self.FramePlace.relHeight != '':
                self.tkFrame.place_configure(relheight=float(self.FramePlace.relHeight))
            if self.FramePlace.relWidth != '':
                self.tkFrame.place_configure(relwidth=float(self.FramePlace.relWidth))
            if self.FramePlace.relX != '':
                self.tkFrame.place_configure(relx=float(self.FramePlace.relX))
            if self.FramePlace.relY != '':
                self.tkFrame.place_configure(rely=float(self.FramePlace.relY))
            if self.FramePlace.offsetX != '':
                self.tkFrame.place_configure(x=int(self.FramePlace.offsetX))
            if self.FramePlace.offsetY != '':
                self.tkFrame.place_configure(y=int(self.FramePlace.offsetY))


        for i in range(0, self.messageCount):
            self.Message.iniFile = self.MessagePlace.iniFile = self.iniFile
            self.Message.section = self.MessagePlace.section = "message" + str(i+1)
            
            self.Message = tkinterMessage.Message.read_settings(self.Message)
            self.tkMessage = tk.Message()    
            if self.Message.anchor != "":
                self.tkMessage.config(anchor=self.Message.anchor)
            if self.Message.aspect != "":
                self.tkMessage.config(aspect=self.Message.aspect)
            if self.Message.backgroundColor != "":
                self.tkMessage.config(background=self.Message.backgroundColor)
            if self.Message.borderwidth != "":
                self.tkMessage.config(borderwidth=self.Message.borderwidth)
            if self.Message.cursor != "":
                self.tkMessage.config(cursor=self.Message.cursor)
            if self.Message.font != "" and self.Message.fontSize != "":
                self.tkMessage.config(font=(self.Message.font, int(self.Message.fontSize)))
            if self.Message.foregroundColor != "":
                self.tkMessage.config(foreground=self.Message.foregroundColor)
            if self.Message.highlightBackground != "":
                self.tkMessage.config(highlightbackground=self.Message.highlightBackground)
            if self.Message.highlightBackgroundColor != "":
                self.tkMessage.config(highlightcolor=self.Message.highlightBackgroundColor)
            if self.Message.highlightThickness != "":
                self.tkMessage.config(highlightthickness=int(self.Message.highlightThickness))
            if self.Message.justify != "":
                self.tkMessage.config(justify=self.Message.justify)
            if self.Message.padX != "":
                self.tkMessage.config(padx=int(self.Message.padX))
            if self.Message.padY != "":
                self.tkMessage.config(pady=int(self.Message.padY))
            if self.Message.relief != "":
                self.tkMessage.config(relief=self.Message.relief)
            if self.Message.takeFocus != "":
                self.tkMessage.config(takefocus=self.Message.takeFocus)
            if self.Message.text != "":
                self.tkMessage.config(text=self.Message.text)
            if self.Message.textVariable != "":
                self.tkMessage.config(textvariable=self.Message.textVariable)
            if self.Message.width != "":
                self.tkMessage.config(width=int(self.Message.width))
            
            self.MessagePlace = tkinterPlace.Place.read_settings(self.MessagePlace)
            self.tkMessage.place()
            if self.MessagePlace.anchor != '':
                self.tkMessage.place_configure(anchor=self.MessagePlace.anchor)
            if self.MessagePlace.borderMode != '':
                self.tkMessage.place_configure(bordermode=self.MessagePlace.borderMode)
            if self.MessagePlace.height != '':
                self.tkMessage.place_configure(height=int(self.MessagePlace.height))
            if self.MessagePlace.relHeight != '':
                self.tkMessage.place_configure(relheight=int(self.MessagePlace.relHeight))
            if self.MessagePlace.width != '':
                self.tkMessage.place_configure(width=int(self.MessagePlace.width))
            if self.MessagePlace.relWidth != '':
                self.tkMessage.place_configure(relwidth=int(self.MessagePlace.relWidth))
            if self.MessagePlace.relX != '':
                self.tkMessage.place_configure(relx=int(self.MessagePlace.relX))
            if self.MessagePlace.relY != '':
                self.tkMessage.place_configure(rely=int(self.MessagePlace.relY))
            if self.MessagePlace.offsetX != '':
                self.tkMessage.place_configure(x=int(self.MessagePlace.offsetX))
            if self.MessagePlace.offsetY != '':
                self.tkMessage.place_configure(y=int(self.MessagePlace.offsetY))

            
        for i in range(0, self.textCount):
            self.Text.iniFile = self.TextPlace.iniFile = self.iniFile
            self.Text.section = self.TextPlace.section = str("text" + str(i+1))

            self.Text = tkinterText.Text.read_settings(self.Text)
            self.tkText = tk.Text()
            if self.Text.autoSeparators != "":
                self.tkText.config(autoseparators=self.Text.autoSeparators)
            if self.Text.backgroundColor != "":
                self.tkText.config(bg=self.Text.backgroundColor)
            if self.Text.backgroundStipple != "":
                self.tkText.config(bgstipple=self.Text.backgroundStipple)
            if self.Text.borderwidth != "":
                self.tkText.config(bd=int(self.Text.borderwidth))
            if self.Text.foregroundStipple != "":
                self.tkText.config(fgstipple=self.Text.foregroundStipple)
            if self.Text.cursor != "":
                self.tkText.config(cursor=self.Text.cursor)
            if self.Text.exportSelection != "":
                self.tkText.config(exportselection=self.Text.exportSelection)
            if self.Text.font != "" and self.Text.fontSize != "":
                self.tkText.config(font=(self.Text.font, int(self.Text.fontSize)))
            if self.Text.foregroundColor != "":
                self.tkText.config(foreground=self.Text.foregroundColor)
            if self.Text.foregroundStipple != "":
                self.tkText.config(fgstipple=self.Text.foregroundStipple)
            if self.Text.height != "":
                self.tkText.config(height=int(self.Text.height))
            if self.Text.highlightBackgroundColor != "":
                self.tkText.config(highlightbackground=self.Text.highlightBackgroundColor)
            if self.Text.highlightColor != "":
                self.tkText.config(highlightcolor=self.Text.highlightColor)
            if self.Text.highlightThickness != "":
                self.tkText.config(highlightthickness=int(self.Text.highlightThickness))
            if self.Text.insertBackground != "":
                self.tkText.config(insertbackground=self.Text.insertBackground)
            if self.Text.insertBorderwidth != "":
                self.tkText.config(insertBorderwidth=int(self.Text.insertBorderwidth))
            if self.Text.insertOffTime != "":
                self.tkText.config(insertOffTime=int(self.Text.insertOffTime))
            if self.Text.insertOnTime != "":
                self.tkText.config(insertOnTime=int(self.Text.insertOnTime))
            if self.Text.insertWidth != "":
                self.tkText.config(insertWidth=int(self.Text.insertWidth))
            if self.Text.justify != "":
                self.tkText.config(justify=self.Text.justify)
            if self.Text.lmargin1 != "":
                self.tkText.config(lmargin1=int(self.Text.lmargin1))
            if self.Text.tlmargin2 != "":
                self.tkText.config(lmargin2=int(self.Text.lmargin2))
            if self.Text.maxUndo != "":
                self.tkText.config(maxundo=int(self.Text.maxUndo))
            if self.Text.padX != "":
                self.tkText.config(padx=int(self.Text.padX))
            if self.Text.padY != "":
                self.tkText.config(PadY=int(self.Text.padY))
            if self.Text.offset != "":
                self.tkText.config(offset=int(self.Text.offset))
            if self.Text.overstrike != "":
                self.tkText.config(overstrike=self.Text.overstrike)
            if self.Text.relief != "":
                self.tkText.config(offset=self.Text.relief)
            if self.Text.rmargin != "":
                self.tkText.config(overstrike=int(self.Text.rmargin))
            if self.Text.selectBackgroundColor != "":
                self.tkText.config(selectbackground=self.Text.selectBackgroundColor)
            if self.Text.tselectForegroundColor != "":
                self.tkText.config(selectforeground=self.Text.selectForegroundColor)
            if self.Text.selectBorderwidth != "":
                self.tkText.config(selectborderwidth=int(self.Text.selectBorderwidth))
            if self.Text.setGrid != "":
                self.tkText.config(setgrid=self.Text.SetGrid)
            if self.Text.spacing1 != "":
                self.tkText.config(spacing1=int(self.Text.spacing1))
            if self.Text.spacing2 != "":
                self.tkText.config(spacing2=int(self.Text.spacing2))
            if self.Text.spacing3 != "":
                self.tkText.config(spacing3=int(self.Text.spacing3))
            if self.Text.state != "":
                self.tkText.config(state=self.Text.state)
            if self.Text.tabs != "":
                self.tkText.config(tabs=self.Text.tabs)
            if self.Text.takeFocus != "":
                self.tkText.config(takefocus=self.Text.takeFocus)
            if self.Text.text != "":
                #self.Text.insert(tk.INSERT, self.Text.text)
                self.Text.config(text=self.Text.text)
            if self.Text.underline != "":
                self.tkText.config(underline=self.Text.underline)
            if self.Text.undo != "":
                self.tkText.config(undo=int(self.Text.undo))
            if self.Text.width != "":
                self.tkText.config(width=int(self.Text.width))
            if self.Text.wrap != "":
                self.tkText.config(wrap=self.Text.wrap)
            if self.Text.xScrollCommand != "":
                self.tkText.config(xscrollcommand=int(self.Text.xScrollCommand))
            if self.Text.yScrollCommand != "":
                self.tkText.config(yscrollcommand=int(self.Text.yScrollCommand))

            self.TextPlace = tkinterPlace.Place.read_settings(self.TextPlace)
            self.tkText.place()
            if self.TextPlace.anchor != '':
                self.tkText.place_configure(anchor=self.TextPlace.anchor)
            if self.TextPlace.borderMode != '':
                self.tkText.place_configure(bordermode=self.TextPlace.borderMode)
            if self.TextPlace.height != '':
                self.tkText.place_configure(height=int(self.TextPlace.height))
            if self.TextPlace.relHeight != '':
                self.tkText.place_configure(relheight=int(self.TextPlace.relHeight))
            if self.TextPlace.width != '':
                self.tkText.place_configure(width=int(self.TextPlace.width))
            if self.TextPlace.relWidth != '':
                self.tkText.place_configure(relwidth=int(self.TextPlace.relWidth))
            if self.TextPlace.relX != '':
                self.tkText.place_configure(relx=int(self.TextPlace.relX))
            if self.TextPlace.relY != '':
                self.tkText.place_configure(rely=int(self.TextPlace.relY))
            if self.TextPlace.offsetX != '':
                self.tkText.place_configure(x=int(self.TextPlace.offsetX))
            if self.TextPlace.offsetY != '':
                self.tkText.place_configure(y=int(self.TextPlace.offsetY))

        for i in range(0, self.buttonCount):
            self.Button.iniFile = self.ButtonPlace.iniFile = self.iniFile
            self.Button.section = self.ButtonPlace.section = "button" + str(i+1)

            self.Button = tkinterButton.Button.read_settings(self.Button)
            self.tkButton = tk.Button()
            if self.Button.backgroundColor != '':
                self.tkButton.config(background=self.Button.backgroundColor)
            if self.Button.bitmap != '':
                self.tkButton.config(bitmap=self.Button.bitmap)
            if self.Button.borderwidth != '':
                self.tkButton.config(borderwidth=int(self.Button.borderwidth))
            if self.Button.command != '':
                self.tkButton.config(command=lambda instance=int(self.Button.command): callback(self.parent, instance))
            if self.Button.compound != '':
                self.tkButton.config(compound=self.Button.compound)
            if self.Button.cursor != '':
                self.tkButton.config(cursor=self.Button.cursor)
            if self.Button.default != '':
                self.tkButton.config(default=self.Button.default)
            if self.Button.disableForeground != '':
                self.tkButton.config(disableforeground=self.Button.disableForeground)
            if self.Button.font != '' and self.Button.fontSize != '':
                self.tkButton.config(font=(self.Button.font, int(self.Button.fontSize)))
            if self.Button.foregroundColor != '':
                self.tkButton.config(foreground=self.Button.foregroundColor)
            if self.Button.height != '':
                self.tkButton.config(height=int(self.Button.height))
            if self.Button.highlightBackgroundColor != '':
                self.tkButton.config(highlightbackground=self.Button.highlightBackgroundColor)
            if self.Button.highlightColor != '':
                self.tkButton.config(highlightcolor=self.Button.highlightColor)
            if self.Button.highlightThickness != '':
                self.tkButton.config(highlightthickness=int(self.Button.highlightThickness))
            if self.Button.image != '':
                self.tkButton.config(image=self.Button.image)
            if self.Button.justify != '':
                self.tkButton.config(justify=self.Button.justify)
            if self.Button.overRelief != '':
                self.tkButton.config(overrelief=self.Button.overRelief)
            if self.Button.padX != '':
                self.tkButton.config(padx=int(self.Button.padX))
            if self.Button.padY != '':
                self.tkButton.config(pady=int(self.Button.padY))
            if self.Button.relief != '':
                self.tkButton.config(relief=self.Button.relief)
            if self.Button.repeatDelay != '':
                self.tkButton.config(repeatdelay=int(self.Button.repeatDelay))
            if self.Button.repeatInterval != '':
                self.tkButton.config(repeatinterval=int(self.Button.repeatInterval))
            if self.Button.state != '':
                self.tkButton.config(state=self.Button.state)
            if self.Button.takeFocus != '':
                self.tkButton.config(takefocus=self.Button.takeFocus)
            if self.Button.text != '':
                self.tkButton.config(text=self.Button.text)
            if self.Button.textVariable != '':
                self.tkButton.config(textvariable=self.Button.textVariable)
            if self.Button.underline != '':
                self.tkButton.config(underline=self.Button.underline)
            if self.Button.width != '':
                self.tkButton.config(width=int(self.Button.width))
            if self.Button.wrapLength != '':
                self.tkButton.config(wraplength=int(self.Button.wrapLength))

            self.ButtonPlace = tkinterPlace.Place.read_settings(self.ButtonPlace)
            self.tkButton.place()            
            if self.ButtonPlace.anchor != '':
                self.tkButton.place_configure(anchor=self.ButtonPlace.anchor)
            if self.ButtonPlace.borderMode != '':
                self.tkButton.place_configure(bordermode=self.ButtonPlace.borderMode)
            if self.ButtonPlace.height != '':
                self.tkButton.place_configure(height=int(self.ButtonPlace.height))
            if self.ButtonPlace.width != '':
                self.tkButton.place_configure(width=int(self.ButtonPlace.width))
            if self.ButtonPlace.relHeight != '':
                self.tkButton.place_configure(relheight=int(self.ButtonPlace.relHeight))
            if self.ButtonPlace.relWidth != '':
                self.tkButton.place_configure(relwidth=int(self.ButtonPlace.relWidth))
            if self.ButtonPlace.relX != '':
                self.tkButton.place_configure(relx=int(self.ButtonPlace.relX))
            if self.ButtonPlace.relY != '':
                self.tkButton.place_configure(rely=int(self.ButtonPlace.relY))
            if self.ButtonPlace.offsetX != '':
                self.tkButton.place_configure(x=int(self.ButtonPlace.offsetX))
            if self.ButtonPlace.offsetY != '':
                self.tkButton.place_configure(y=int(self.ButtonPlace.offsetY))

        

def callback(parent, num):
    if num == 1:
        print('F1 pressed')
        pass
    if num == 2:
        print('F2 pressed')
        pass
    if num == 3:
        print('F3 pressed')
        pass
    if num == 4:
        print('F4 pressed')
        pass
    if num == 5:
        print('F5 pressed')
        pass
    if num == 6:
        print('F6 pressed')
        pass
    if num == 7:
        print('F7 pressed')
        pass
    if num == 8:
        print('F8 pressed')
        pass
    if num == 9:
        print('F9 pressed')
        pass
    if num == 10:
        print('F10 pressed')
        pass
    if num == 11:
        print('F11 pressed')
        pass
    if num == 12:
        print('F12 pressed')
        pass
    if num == 13:
        print('F13 pressed')
        print('Attempting to close application')
        try:
            parent.destroy()
            print('Application closed')
        except:
            print('Application already closed')
        finally:
            pass
    if num == 14:
        print('F14 pressed')
        pass
    if num == 15:
        print('F15 pressed')
        pass
    if num == 16:
        print('F16 pressed')
        pass
    if num == 17:
        print('F17 pressed')
        pass
    if num == 18:
        print('F18 pressed')
        pass
    if num == 19:
        print('F19 pressed')
        pass
    if num == 20:
        print('F20 pressed')
        pass
    if num == 21:
        print('F21 pressed')
        print('Attempting to close application')
        try:
            parent.destroy()
            print('Application closed')
        except:
            print('Application already closed')
            pass


        
if __name__ == "__main__":
    root=tk.Tk()
    app = SpawnAppWindow(root, 'gui.ini')
    root.title('My App Window')
    root.mainloop()