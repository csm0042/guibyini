import logging, time, sys
sys.path.insert(0, 'c:/python34/MyProjects/pic-rename/pic-rename')
import gui_callbacks
import tkinter as tk
import widget_count
import tkinterPlace
import tkinterWindow
import tkinterFrame
import tkinterMessage
import tkinterText
import tkinterButton


#######################################################################################################################
# Define class
#######################################################################################################################
class SpawnAppwindow:
    def __init__(self, inifile, logfile, iotable):
        self.root = tk.Tk()
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        self.section = str()
        self.startime = time.time()

        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=self.logfile,
                    filemode='w')
        logging.info('[SpawnGuiFromIni.init] Program Logger for SpawnAppWindow Started at t = +%f' %
                     float(self.startime-self.startime))



        self.Window = tkinterWindow.Window()


        logging.info('[SpawnGuiFromIni.init] Searching INI file for "frame" widgets at t = +%f' %
                     float(time.time()-self.startime))
        self.frameCount = widget_count.CountWidgetByType(self.inifile, "frame")
        logging.info('[SpawnGuiFromIni.init] Found configuration data for %d "frame" widgets at t = +%f' %
                     (self.frameCount, float(time.time()-self.startime)))
        self.frameDataRead = 0
        self.framesCreated = 0
        self.Frame = tkinterFrame.Frame()
        self.FramePlace = tkinterPlace.Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]


        # Create tag lists for message settings
        logging.info('[SpawnGuiFromIni.init] Searching INI file for "message" widgets at t = +%f' %
                     float(time.time()-self.startime))
        self.messageCount = widget_count.CountWidgetByType(self.inifile, "message")
        logging.info('[SpawnGuiFromIni.init] Found configuration data for %d "message" widgets at t = +%f' %
                     (self.messageCount, float(time.time()-self.startime)))
        self.messageDataRead = 0
        self.messagesCreated = 0
        self.Message = tkinterMessage.Message()
        self.MessagePlace = tkinterPlace.Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]

        # Create tag list for text settings
        logging.info('[SpawnGuiFromIni.init] Searching INI file for "text" widgets at t = +%f' %
                     float(time.time()-self.startime))
        self.textCount = widget_count.CountWidgetByType(self.inifile, "text")
        logging.info('[SpawnGuiFromIni.init] Found configuration data for %d "text" widgets at t = +%f' %
                     (self.textCount, float(time.time()-self.startime)))
        self.textDataRead = 0
        self.textsCreated = 0
        self.Text = tkinterText.Text()
        self.TextPlace = tkinterPlace.Place()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        self.tkTextHandshake = [str() for i in range(self.textCount)]

        # Create tag lists for button settings
        logging.info('[SpawnGuiFromIni.init] Searching INI file for "button" widgets at t = +%f' %
                     float(time.time()-self.startime))
        self.buttonCount = widget_count.CountWidgetByType(self.inifile, "button")
        logging.info('[SpawnGuiFromIni.init] Found configuration data for %d "button" widgets at t = +%f' %
                     (self.buttonCount, float(time.time()-self.startime)))
        self.buttonDataRead = 0
        self.buttonsCreated = 0
        self.Button = tkinterButton.Button()
        self.ButtonInput = [bool() for i in range(self.buttonCount)]
        self.ButtonPlace = tkinterPlace.Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]

        # Call function to populate setting tags
        logging.info('[SpawnGuiFromIni.init] Call "initialize" function at t = +%f' % float(time.time()-self.startime))
        self.SpawnAppWindow()
        logging.info('[SpawnGuiFromIni.init] Initialization complete at t = +%f' % float(time.time()-self.startime))




    def SpawnAppWindow(self):
        self.Window.section = "main window"
        self.Window.iniFile = self.inifile

       
        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window = tkinterWindow.Window.read_settings(self.Window)
        logging.info('[SpawnGuiFromIni.SpawnAppwindow] Adjusting window geometry')
        self.root.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height),
                                              int(self.Window.posX), int(self.Window.posY)))
        logging.info('[SpawnGuiFromIni.SpawnAppwindow] Adjusting window background color')
        if self.Window.backgroundColor != "":
            self.parent.config(background=self.Window.backgroundColor)


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        logging.info('[SpawnGuiFromIni.SpawnAppWindow] Starting "frame" widget loop')
        for i in range(0, self.frameCount):
            self.Frame.iniFile = self.FramePlace.iniFile = self.inifile
            self.Frame.section = self.FramePlace.section = str("frame" + str(i+1))
            
            self.Frame = tkinterFrame.Frame.read_settings(self.Frame)
            self.tkFrame[i] = tk.Frame()
            if self.Frame.backgroundColor != '':
                self.tkFrame[i].config(background=self.Frame.backgroundColor)
            if self.Frame.borderwidth != '':
                self.tkFrame[i].config(borderwidth=int(self.Frame.borderwidth))
            if self.Frame.colormap != '':
                self.tkFrame[i].config(colormap=self.Frame.colormap)
            if self.Frame.container != '':
                self.tkFrame[i].config(container=self.Frame.container)
            if self.Frame.cursor != '':
                self.tkFrame[i].config(cursor=self.Frame.cursor)
            if self.Frame.height != '':
                self.tkFrame[i].config(height=int(self.Frame.height))
            if self.Frame.highlightBackgroundColor != '':
                self.tkFrame[i].config(highlightbackground=self.Frame.highlightBackgroundColor)
            if self.Frame.highlightColor != '':
                self.tkFrame[i].config(highlightcolor=self.Frame.highlightColor)
            if self.Frame.highlightThickness != '':
                self.tkFrame[i].config(highlightthickness=int(self.Frame.highlightThickness))
            if self.Frame.padX != '':
                self.tkFrame[i].config(padx=int(self.Frame.padX))
            if self.Frame.padY != '':
                self.tkFrame[i].config(pady=int(self.Frame.padY))
            if self.Frame.relief != '':
                self.tkFrame[i].config(relief=self.Frame.relief)
            if self.Frame.takeFocus != '':
                self.tkFrame[i].config(takefocus=self.Frame.takeFocus)
            if self.Frame.visual != '':
                self.tkFrame[i].config(visual=self.Frame.visual)
            if self.Frame.width != '':
                self.tkFrame[i].config(width=int(self.Frame.width))
                
            self.FramePlace = tkinterPlace.Place.read_settings(self.FramePlace)
            self.tkFrame[i].place()
            if self.FramePlace.anchor != '':
                self.tkFrame[i].place_configure(anchor=self.FramePlace.anchor)
            if self.FramePlace.borderMode != '':
                self.tkFrame[i].place_configure(bordermode=self.FramePlace.borderMode)
            if self.FramePlace.height != '':
                self.tkFrame[i].place_configure(height=int(self.FramePlace.height))
            if self.FramePlace.width != '':
                self.tkFrame[i].place_configure(width=int(self.FramePlace.width))
            if self.FramePlace.relHeight != '':
                self.tkFrame[i].place_configure(relheight=float(self.FramePlace.relHeight))
            if self.FramePlace.relWidth != '':
                self.tkFrame[i].place_configure(relwidth=float(self.FramePlace.relWidth))
            if self.FramePlace.relX != '':
                self.tkFrame[i].place_configure(relx=float(self.FramePlace.relX))
            if self.FramePlace.relY != '':
                self.tkFrame[i].place_configure(rely=float(self.FramePlace.relY))
            if self.FramePlace.offsetX != '':
                self.tkFrame[i].place_configure(x=int(self.FramePlace.offsetX))
            if self.FramePlace.offsetY != '':
                self.tkFrame[i].place_configure(y=int(self.FramePlace.offsetY))
        
        
        ################################################################################################################
        # CALL LOOP TO CREATE MESSAGE WIDGETS
        ################################################################################################################
        logging.info('[SpawnGuiFromIni.SpawnAppwindow] Starting "message" widget loop')
        for i in range(0, self.messageCount):
            self.Message.iniFile = self.MessagePlace.iniFile = self.inifile
            self.Message.section = self.MessagePlace.section = "message" + str(i+1)
            
            self.Message = tkinterMessage.Message.read_settings(self.Message)
            self.tkMessage[i] = tk.Message()    
            if self.Message.anchor != "":
                self.tkMessage[i].config(anchor=self.Message.anchor)
            if self.Message.aspect != "":
                self.tkMessage[i].config(aspect=self.Message.aspect)
            if self.Message.backgroundColor != "":
                self.tkMessage[i].config(background=self.Message.backgroundColor)
            if self.Message.borderwidth != "":
                self.tkMessage[i].config(borderwidth=self.Message.borderwidth)
            if self.Message.cursor != "":
                self.tkMessage[i].config(cursor=self.Message.cursor)
            if self.Message.font != "" and self.Message.fontSize != "":
                self.tkMessage[i].config(font=(self.Message.font, int(self.Message.fontSize)))
            if self.Message.foregroundColor != "":
                self.tkMessage[i].config(foreground=self.Message.foregroundColor)
            if self.Message.highlightBackground != "":
                self.tkMessage[i].config(highlightbackground=self.Message.highlightBackground)
            if self.Message.highlightBackgroundColor != "":
                self.tkMessage[i].config(highlightcolor=self.Message.highlightBackgroundColor)
            if self.Message.highlightThickness != "":
                self.tkMessage[i].config(highlightthickness=int(self.Message.highlightThickness))
            if self.Message.justify != "":
                self.tkMessage[i].config(justify=self.Message.justify)
            if self.Message.padX != "":
                self.tkMessage[i].config(padx=int(self.Message.padX))
            if self.Message.padY != "":
                self.tkMessage[i].config(pady=int(self.Message.padY))
            if self.Message.relief != "":
                self.tkMessage[i].config(relief=self.Message.relief)
            if self.Message.takeFocus != "":
                self.tkMessage[i].config(takefocus=self.Message.takeFocus)
            if self.Message.text != "":
                self.tkMessage[i].config(text=self.Message.text)
            if self.Message.textVariable != "":
                self.tkMessage[i].config(textvariable=self.Message.textVariable)
            if self.Message.width != "":
                self.tkMessage[i].config(width=int(self.Message.width))
            
            self.MessagePlace = tkinterPlace.Place.read_settings(self.MessagePlace)
            self.tkMessage[i].place()
            if self.MessagePlace.anchor != '':
                self.tkMessage[i].place_configure(anchor=self.MessagePlace.anchor)
            if self.MessagePlace.borderMode != '':
                self.tkMessage[i].place_configure(bordermode=self.MessagePlace.borderMode)
            if self.MessagePlace.height != '':
                self.tkMessage[i].place_configure(height=int(self.MessagePlace.height))
            if self.MessagePlace.relHeight != '':
                self.tkMessage[i].place_configure(relheight=int(self.MessagePlace.relHeight))
            if self.MessagePlace.width != '':
                self.tkMessage[i].place_configure(width=int(self.MessagePlace.width))
            if self.MessagePlace.relWidth != '':
                self.tkMessage[i].place_configure(relwidth=int(self.MessagePlace.relWidth))
            if self.MessagePlace.relX != '':
                self.tkMessage[i].place_configure(relx=int(self.MessagePlace.relX))
            if self.MessagePlace.relY != '':
                self.tkMessage[i].place_configure(rely=int(self.MessagePlace.relY))
            if self.MessagePlace.offsetX != '':
                self.tkMessage[i].place_configure(x=int(self.MessagePlace.offsetX))
            if self.MessagePlace.offsetY != '':
                self.tkMessage[i].place_configure(y=int(self.MessagePlace.offsetY))
        
        
        ################################################################################################################
        # CALL LOOP TO CREATE TEXT WIDGETS
        ################################################################################################################
        logging.info('[SpawnGuiFromIni.SpawnAppWindow] Starting "text" widget loop at t = +%f' % float(time.time()-self.startime))
        for i in range(0, self.textCount):
            self.Text.iniFile = self.TextPlace.iniFile = self.inifile
            self.Text.section = self.TextPlace.section = str("text" + str(i+1))

            self.Text = tkinterText.Text.read_settings(self.Text)
            self.tkText[i] = tk.Text()
            if self.Text.autoSeparators != "":
                self.tkText[i].config(autoseparators=self.Text.autoSeparators)
            if self.Text.backgroundColor != "":
                self.tkText[i].config(bg=self.Text.backgroundColor)
            if self.Text.backgroundStipple != "":
                self.tkText[i].config(bgstipple=self.Text.backgroundStipple)
            if self.Text.borderwidth != "":
                self.tkText[i].config(bd=int(self.Text.borderwidth))
            if self.Text.foregroundStipple != "":
                self.tkText[i].config(fgstipple=self.Text.foregroundStipple)
            if self.Text.cursor != "":
                self.tkText[i].config(cursor=self.Text.cursor)
            if self.Text.exportSelection != "":
                self.tkText[i].config(exportselection=self.Text.exportSelection)
            if self.Text.font != "" and self.Text.fontSize != "":
                self.tkText[i].config(font=(self.Text.font, int(self.Text.fontSize)))
            if self.Text.foregroundColor != "":
                self.tkText[i].config(foreground=self.Text.foregroundColor)
            if self.Text.foregroundStipple != "":
                self.tkText[i].config(fgstipple=self.Text.foregroundStipple)
            if self.Text.height != "":
                self.tkText[i].config(height=int(self.Text.height))
            if self.Text.highlightBackgroundColor != "":
                self.tkText[i].config(highlightbackground=self.Text.highlightBackgroundColor)
            if self.Text.highlightColor != "":
                self.tkText[i].config(highlightcolor=self.Text.highlightColor)
            if self.Text.highlightThickness != "":
                self.tkText[i].config(highlightthickness=int(self.Text.highlightThickness))
            if self.Text.insertBackground != "":
                self.tkText[i].config(insertbackground=self.Text.insertBackground)
            if self.Text.insertBorderwidth != "":
                self.tkText[i].config(insertBorderwidth=int(self.Text.insertBorderwidth))
            if self.Text.insertOffTime != "":
                self.tkText[i].config(insertOffTime=int(self.Text.insertOffTime))
            if self.Text.insertOnTime != "":
                self.tkText[i].config(insertOnTime=int(self.Text.insertOnTime))
            if self.Text.insertWidth != "":
                self.tkText[i].config(insertWidth=int(self.Text.insertWidth))
            #if self.Text.justify != "":
            #    self.tkText[i].config(justify=self.Text.justify)
            if self.Text.lmargin1 != "":
                self.tkText[i].config(lmargin1=int(self.Text.lmargin1))
            if self.Text.lmargin2 != "":
                self.tkText[i].config(lmargin2=int(self.Text.lmargin2))
            if self.Text.maxUndo != "":
                self.tkText[i].config(maxundo=int(self.Text.maxUndo))
            if self.Text.padX != "":
                self.tkText[i].config(padx=int(self.Text.padX))
            if self.Text.padY != "":
                self.tkText[i].config(pady=int(self.Text.padY))
            if self.Text.offset != "":
                self.tkText[i].config(offset=int(self.Text.offset))
            if self.Text.overstrike != "":
                self.tkText[i].config(overstrike=self.Text.overstrike)
            if self.Text.relief != "":
                self.tkText[i].config(offset=self.Text.relief)
            if self.Text.rmargin != "":
                self.tkText[i].config(overstrike=int(self.Text.rmargin))
            if self.Text.selectBackgroundColor != "":
                self.tkText[i].config(selectbackground=self.Text.selectBackgroundColor)
            if self.Text.selectForegroundColor != "":
                self.tkText[i].config(selectforeground=self.Text.selectForegroundColor)
            if self.Text.selectBorderwidth != "":
                self.tkText[i].config(selectborderwidth=int(self.Text.selectBorderwidth))
            if self.Text.setGrid != "":
                self.tkText[i].config(setgrid=self.Text.SetGrid)
            if self.Text.spacing1 != "":
                self.tkText[i].config(spacing1=int(self.Text.spacing1))
            if self.Text.spacing2 != "":
                self.tkText[i].config(spacing2=int(self.Text.spacing2))
            if self.Text.spacing3 != "":
                self.tkText[i].config(spacing3=int(self.Text.spacing3))
            if self.Text.state != "":
                self.tkText[i].config(state=self.Text.state)
            if self.Text.tabs != "":
                self.tkText[i].config(tabs=self.Text.tabs)
            if self.Text.takeFocus != "":
                self.tkText[i].config(takefocus=self.Text.takeFocus)
            if self.Text.text != "":
                self.tkText[i].insert(tk.END, self.Text.text)
            if self.Text.underline != "":
                self.tkText[i].config(underline=self.Text.underline)
            if self.Text.undo != "":
                self.tkText[i].config(undo=int(self.Text.undo))
            if self.Text.width != "":
                self.tkText[i].config(width=int(self.Text.width))
            if self.Text.wrap != "":
                self.tkText[i].config(wrap=self.Text.wrap)
            if self.Text.xScrollCommand != "":
                self.tkText[i].config(xscrollcommand=int(self.Text.xScrollCommand))
            if self.Text.yScrollCommand != "":
                self.tkText[i].config(yscrollcommand=int(self.Text.yScrollCommand))

            self.TextPlace = tkinterPlace.Place.read_settings(self.TextPlace)
            self.tkText[i].place()
            if self.TextPlace.anchor != '':
                self.tkText[i].place_configure(anchor=self.TextPlace.anchor)
            if self.TextPlace.borderMode != '':
                self.tkText[i].place_configure(bordermode=self.TextPlace.borderMode)
            if self.TextPlace.height != '':
                self.tkText[i].place_configure(height=int(self.TextPlace.height))
            if self.TextPlace.relHeight != '':
                self.tkText[i].place_configure(relheight=int(self.TextPlace.relHeight))
            if self.TextPlace.width != '':
                self.tkText[i].place_configure(width=int(self.TextPlace.width))
            if self.TextPlace.relWidth != '':
                self.tkText[i].place_configure(relwidth=int(self.TextPlace.relWidth))
            if self.TextPlace.relX != '':
                self.tkText[i].place_configure(relx=int(self.TextPlace.relX))
            if self.TextPlace.relY != '':
                self.tkText[i].place_configure(rely=int(self.TextPlace.relY))
            if self.TextPlace.offsetX != '':
                self.tkText[i].place_configure(x=int(self.TextPlace.offsetX))
            if self.TextPlace.offsetY != '':
                self.tkText[i].place_configure(y=int(self.TextPlace.offsetY))
        
        
        ################################################################################################################
        # CALL LOOP TO CREATE BUTTON WIDGETS
        ################################################################################################################
        logging.info('[SpawnGuiFromIni.SpawnAppWindow] Starting "button" widget loop at t = +%f' %
                     float(time.time()-self.startime))
        for i in range(0, self.buttonCount):
            self.Button.iniFile = self.ButtonPlace.iniFile = self.inifile
            self.Button.section = self.ButtonPlace.section = "button" + str(i+1)

            self.Button = tkinterButton.Button.read_settings(self.Button)
            self.tkButton[i] = tk.Button()
            if self.Button.backgroundColor != '':
                self.tkButton[i].config(background=self.Button.backgroundColor)
            if self.Button.bitmap != '':
                self.tkButton[i].config(bitmap=self.Button.bitmap)
            if self.Button.borderwidth != '':
                self.tkButton[i].config(borderwidth=int(self.Button.borderwidth))
            if self.Button.command != '':
                self.tkButton[i].config(command=lambda instance=int(self.Button.command): gui_callbacks.callback(self, instance))
            if self.Button.compound != '':
                self.tkButton[i].config(compound=self.Button.compound)
            if self.Button.cursor != '':
                self.tkButton[i].config(cursor=self.Button.cursor)
            if self.Button.default != '':
                self.tkButton[i].config(default=self.Button.default)
            if self.Button.disableForeground != '':
                self.tkButton[i].config(disableforeground=self.Button.disableForeground)
            if self.Button.font != '' and self.Button.fontSize != '':
                self.tkButton[i].config(font=(self.Button.font, int(self.Button.fontSize)))
            if self.Button.foregroundColor != '':
                self.tkButton[i].config(foreground=self.Button.foregroundColor)
            if self.Button.height != '':
                self.tkButton[i].config(height=int(self.Button.height))
            if self.Button.highlightBackgroundColor != '':
                self.tkButton[i].config(highlightbackground=self.Button.highlightBackgroundColor)
            if self.Button.highlightColor != '':
                self.tkButton[i].config(highlightcolor=self.Button.highlightColor)
            if self.Button.highlightThickness != '':
                self.tkButton[i].config(highlightthickness=int(self.Button.highlightThickness))
            if self.Button.image != '':
                self.tkButton[i].config(image=self.Button.image)
            if self.Button.justify != '':
                self.tkButton[i].config(justify=self.Button.justify)
            if self.Button.overRelief != '':
                self.tkButton[i].config(overrelief=self.Button.overRelief)
            if self.Button.padX != '':
                self.tkButton[i].config(padx=int(self.Button.padX))
            if self.Button.padY != '':
                self.tkButton[i].config(pady=int(self.Button.padY))
            if self.Button.relief != '':
                self.tkButton[i].config(relief=self.Button.relief)
            if self.Button.repeatDelay != '':
                self.tkButton[i].config(repeatdelay=int(self.Button.repeatDelay))
            if self.Button.repeatInterval != '':
                self.tkButton[i].config(repeatinterval=int(self.Button.repeatInterval))
            if self.Button.state != '':
                self.tkButton[i].config(state=self.Button.state)
            if self.Button.takeFocus != '':
                self.tkButton[i].config(takefocus=self.Button.takeFocus)
            if self.Button.text != '':
                self.tkButton[i].config(text=self.Button.text)
            if self.Button.textVariable != '':
                self.tkButton[i].config(textvariable=self.Button.textVariable)
            if self.Button.underline != '':
                self.tkButton[i].config(underline=self.Button.underline)
            if self.Button.width != '':
                self.tkButton[i].config(width=int(self.Button.width))
            if self.Button.wrapLength != '':
                self.tkButton[i].config(wraplength=int(self.Button.wrapLength))

            self.ButtonPlace = tkinterPlace.Place.read_settings(self.ButtonPlace)
            self.tkButton[i].place()            
            if self.ButtonPlace.anchor != '':
                self.tkButton[i].place_configure(anchor=self.ButtonPlace.anchor)
            if self.ButtonPlace.borderMode != '':
                self.tkButton[i].place_configure(bordermode=self.ButtonPlace.borderMode)
            if self.ButtonPlace.height != '':
                self.tkButton[i].place_configure(height=int(self.ButtonPlace.height))
            if self.ButtonPlace.width != '':
                self.tkButton[i].place_configure(width=int(self.ButtonPlace.width))
            if self.ButtonPlace.relHeight != '':
                self.tkButton[i].place_configure(relheight=int(self.ButtonPlace.relHeight))
            if self.ButtonPlace.relWidth != '':
                self.tkButton[i].place_configure(relwidth=int(self.ButtonPlace.relWidth))
            if self.ButtonPlace.relX != '':
                self.tkButton[i].place_configure(relx=int(self.ButtonPlace.relX))
            if self.ButtonPlace.relY != '':
                self.tkButton[i].place_configure(rely=int(self.ButtonPlace.relY))
            if self.ButtonPlace.offsetX != '':
                self.tkButton[i].place_configure(x=int(self.ButtonPlace.offsetX))
            if self.ButtonPlace.offsetY != '':
                self.tkButton[i].place_configure(y=int(self.ButtonPlace.offsetY))

        self.root.mainloop()



    ####################################################################################################################
    # Define interface methods
    ####################################################################################################################
    def return_root(self):
        return self.root

    def kill_root(self):
        self.root.destroy()
        return

    def return_text(self, field):
        self.field = field - 1
        self.tkTextHandshake[self.field] = self.tkText[self.field].get("1.0", tk.END)
        return self.tkTextHandshake[self.field]

    def write_text(self, field, text):
        self.field = field - 1
        self.text = text
        self.tkText[self.field].insert(tk.END, self.text)
        return

    def clear_text(self, field):
        self.field = field - 1
        self.tkText[self.field].delete(1.0, tk.END)
        return




########################################################################################################################
#  Run if script is called manually
########################################################################################################################
        
if __name__ == "__main__":
    ioTable = int()
    app = SpawnAppwindow('gui.ini', 'debug.log', ioTable)