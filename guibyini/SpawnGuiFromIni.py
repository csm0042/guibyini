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
class AppWindow(object):
    def __init__(self, inifile, logfile, iotable):
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        self.root = tk.Tk()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[AppWindow.init] Appwindow object created')

        self.frameCount = widget_count.CountWidgetByType(self.inifile, "frame")
        self.messageCount = widget_count.CountWidgetByType(self.inifile, "message")
        self.textCount = widget_count.CountWidgetByType(self.inifile, "text")
        self.buttonCount = widget_count.CountWidgetByType(self.inifile, "button")
        logging.info('[AppWindow.init] Found configuration data for %d "frame" widgets' %self.frameCount)
        logging.info('[AppWindow.init] Found configuration data for %d "message" widgets' %self.messageCount)
        logging.info('[AppWindow.init] Found configuration data for %d "text" widgets' %self.textCount)
        logging.info('[AppWindow.init] Found configuration data for %d "button" widgets' %self.buttonCount)

        self.section = str()
        self.Window = tkinterWindow.Window()

        self.Frame = tkinterFrame.Frame()
        self.FramePlace = tkinterPlace.Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]

        self.Message = tkinterMessage.Message()
        self.MessagePlace = tkinterPlace.Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]

        self.Text = tkinterText.Text()
        self.TextPlace = tkinterPlace.Place()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        self.tkTextHandshake = [str() for i in range(self.textCount)]

        self.Button = tkinterButton.Button()
        self.ButtonPlace = tkinterPlace.Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        self.ButtonInput = [bool() for i in range(self.buttonCount)]



    def SpawnAppWindow(self):

        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window.section = "main window"
        self.Window.iniFile = self.inifile
        self.Window = tkinterWindow.Window.read_settings(self.Window)
        logging.info('[SpawnAppwindow] Adjusting window geometry')
        self.root.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height), int(self.Window.posX),
                                            int(self.Window.posY)))
        logging.info('[SpawnAppWindow] Adjusting window background color')
        if self.Window.backgroundColor != "":
            self.root.config(background=self.Window.backgroundColor)
        logging.info('[SpawnAppWindow] Setting window title')
        if self.Window.title != '':
            self.root.title(self.Window.title)


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        logging.info('[SpawnGuiFromIni.SpawnAppWindow] Starting "frame" widget loop')
        for i in range(0, self.frameCount):
            self.Frame.iniFile = self.FramePlace.iniFile = self.inifile
            self.Frame.section = self.FramePlace.section = str("frame" + str(i+1))
            self.Frame = tkinterFrame.Frame.read_settings(self.Frame)
            self.FramePlace = tkinterPlace.Place.read_settings(self.FramePlace)
            logging.info('[SpawnAppWindow] Creating frame widget #%d' % (i+1))
            self.tkFrame[i] = self.SpawnFrame(self.tkFrame[i], self.Frame, self.FramePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE MESSAGE WIDGETS
        ################################################################################################################
        logging.info('[SpawnAppWindow] Starting "message" widget loop')
        for i in range(0, self.messageCount):
            self.Message.iniFile = self.MessagePlace.iniFile = self.inifile
            self.Message.section = self.MessagePlace.section = "message" + str(i+1)
            self.Message = tkinterMessage.Message.read_settings(self.Message)
            self.MessagePlace = tkinterPlace.Place.read_settings(self.MessagePlace)
            logging.info('[SpawnAppWindow] Creating message widget #%d' % (i+1))
            self.tkMessage[i] = self.SpawnMessage(self.tkMessage[i], self.Message, self.MessagePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE TEXT WIDGETS
        ################################################################################################################
        logging.info('[SpawnAppWindow] Starting "text" widget loop')
        for i in range(0, self.textCount):
            self.Text.iniFile = self.TextPlace.iniFile = self.inifile
            self.Text.section = self.TextPlace.section = str("text" + str(i+1))
            self.Text = tkinterText.Text.read_settings(self.Text)
            self.TextPlace = tkinterPlace.Place.read_settings(self.TextPlace)
            logging.info('[SpawnAppWindow] Creating text widget #%d' % (i+1))
            self.tkText[i] = self.SpawnText(self.tkText[i], self.Text, self.TextPlace)


        ################################################################################################################
        # CALL LOOP TO CREATE BUTTON WIDGETS
        ################################################################################################################
        logging.info('[SpawnAppWindow] Starting "button" widget loop')
        for i in range(0, self.buttonCount):
            self.Button.iniFile = self.ButtonPlace.iniFile = self.inifile
            self.Button.section = self.ButtonPlace.section = "button" + str(i+1)
            self.Button = tkinterButton.Button.read_settings(self.Button)
            self.ButtonPlace = tkinterPlace.Place.read_settings(self.ButtonPlace)
            logging.info('[SpawnAppWindow] Creating button widget #%d' % (i+1))
            self.tkButton[i] = self.SpawnButton(self.tkButton[i], self.Button, self.ButtonPlace)

        logging.info('[SpawnAppWindow] Starting tkinter main loop')
        self.root.mainloop()
        return self



    def SpawnFrame(self, frame, settings, placesettings):
        self.frame = frame
        self.frame = tk.Frame()
        self.settings = settings
        self.placesettings = placesettings
        if self.settings.backgroundColor != '':
            self.frame.config(background=self.settings.backgroundColor)
        if self.settings.borderwidth != '':
            self.frame.config(borderwidth=int(self.settings.borderwidth))
        if self.settings.colormap != '':
            self.frame.config(colormap=self.settings.colormap)
        if self.settings.container != '':
            self.frame.config(container=self.settings.container)
        if self.settings.cursor != '':
            self.frame.config(cursor=self.settings.cursor)
        if self.settings.height != '':
            self.frame.config(height=int(self.settings.height))
        if self.settings.highlightBackgroundColor != '':
            self.frame.config(highlightbackground=self.settings.highlightBackgroundColor)
        if self.settings.highlightColor != '':
            self.frame.config(highlightcolor=self.settings.highlightColor)
        if self.settings.highlightThickness != '':
            self.frame.config(highlightthickness=int(self.settings.highlightThickness))
        if self.settings.padX != '':
            self.frame.config(padx=int(self.settings.padX))
        if self.settings.padY != '':
            self.frame.config(pady=int(self.settings.padY))
        if self.settings.relief != '':
            self.frame.config(relief=self.settings.relief)
        if self.settings.takeFocus != '':
            self.frame.config(takefocus=self.settings.takeFocus)
        if self.settings.visual != '':
            self.frame.config(visual=self.settings.visual)
        if self.settings.width != '':
            self.frame.config(width=int(self.settings.width))
        self.frame.place()
        if self.placesettings.anchor != '':
            self.frame.place_configure(anchor=self.placesettings.anchor)
        if self.placesettings.borderMode != '':
            self.frame.place_configure(bordermode=self.placesettings.borderMode)
        if self.placesettings.height != '':
            self.frame.place_configure(height=int(self.placesettings.height))
        if self.placesettings.width != '':
            self.frame.place_configure(width=int(self.placesettings.width))
        if self.placesettings.relHeight != '':
            self.frame.place_configure(relheight=float(self.placesettings.relHeight))
        if self.placesettings.relWidth != '':
            self.frame.place_configure(relwidth=float(self.placesettings.relWidth))
        if self.placesettings.relX != '':
            self.frame.place_configure(relx=float(self.placesettings.relX))
        if self.placesettings.relY != '':
            self.frame.place_configure(rely=float(self.placesettings.relY))
        if self.placesettings.offsetX != '':
            self.frame.place_configure(x=int(self.placesettings.offsetX))
        if self.placesettings.offsetY != '':
            self.frame.place_configure(y=int(self.placesettings.offsetY))
        return self.frame


    def SpawnMessage(self, message, settings, placesettings):
        self.message = message
        self.message = tk.Message()
        self.settings = settings
        self.placesettings = placesettings
        if self.settings.anchor != "":
            self.message.config(anchor=self.settings.anchor)
        if self.settings.aspect != "":
            self.message.config(aspect=self.settings.aspect)
        if self.settings.backgroundColor != "":
            self.message.config(background=self.settings.backgroundColor)
        if self.settings.borderwidth != "":
            self.message.config(borderwidth=self.settings.borderwidth)
        if self.settings.cursor != "":
            self.message.config(cursor=self.settings.cursor)
        if self.settings.font != "" and self.settings.fontSize != "":
            self.message.config(font=(self.settings.font, int(self.settings.fontSize)))
        if self.settings.foregroundColor != "":
            self.message.config(foreground=self.settings.foregroundColor)
        if self.settings.highlightBackground != "":
            self.message.config(highlightbackground=self.settings.highlightBackground)
        if self.settings.highlightBackgroundColor != "":
            self.message.config(highlightcolor=self.settings.highlightBackgroundColor)
        if self.settings.highlightThickness != "":
            self.message.config(highlightthickness=int(self.settings.highlightThickness))
        if self.settings.justify != "":
            self.message.config(justify=self.settings.justify)
        if self.settings.padX != "":
            self.message.config(padx=int(self.settings.padX))
        if self.settings.padY != "":
            self.message.config(pady=int(self.settings.padY))
        if self.settings.relief != "":
            self.message.config(relief=self.settings.relief)
        if self.settings.takeFocus != "":
            self.message.config(takefocus=self.settings.takeFocus)
        if self.settings.text != "":
            self.message.config(text=self.settings.text)
        if self.settings.textVariable != "":
            self.message.config(textvariable=self.settings.textVariable)
        if self.settings.width != "":
            self.message.config(width=int(self.settings.width))
        self.message.place()
        if self.placesettings.anchor != '':
            self.message.place_configure(anchor=self.placesettings.anchor)
        if self.placesettings.borderMode != '':
            self.message.place_configure(bordermode=self.placesettings.borderMode)
        if self.placesettings.height != '':
            self.message.place_configure(height=int(self.placesettings.height))
        if self.placesettings.relHeight != '':
            self.message.place_configure(relheight=int(self.placesettings.relHeight))
        if self.placesettings.width != '':
            self.message.place_configure(width=int(self.placesettings.width))
        if self.placesettings.relWidth != '':
            self.message.place_configure(relwidth=int(self.placesettings.relWidth))
        if self.placesettings.relX != '':
            self.message.place_configure(relx=int(self.placesettings.relX))
        if self.placesettings.relY != '':
            self.message.place_configure(rely=int(self.placesettings.relY))
        if self.placesettings.offsetX != '':
            self.message.place_configure(x=int(self.placesettings.offsetX))
        if self.placesettings.offsetY != '':
            self.message.place_configure(y=int(self.placesettings.offsetY))
        return self.message


    def SpawnText(self, text, settings, placesettings):
        self.text = text
        self.text = tk.Text()
        self.settings = settings
        self.placesettings = placesettings
        if self.settings.autoSeparators != "":
            self.text.config(autoseparators=self.settings.autoSeparators)
        if self.settings.backgroundColor != "":
            self.text.config(bg=self.settings.backgroundColor)
        if self.settings.backgroundStipple != "":
            self.text.config(bgstipple=self.settings.backgroundStipple)
        if self.settings.borderwidth != "":
            self.text.config(bd=int(self.settings.borderwidth))
        if self.settings.foregroundStipple != "":
            self.text.config(fgstipple=self.settings.foregroundStipple)
        if self.settings.cursor != "":
            self.text.config(cursor=self.settings.cursor)
        if self.settings.exportSelection != "":
            self.text.config(exportselection=self.settings.exportSelection)
        if self.settings.font != "" and self.settings.fontSize != "":
            self.text.config(font=(self.settings.font, int(self.settings.fontSize)))
        if self.settings.foregroundColor != "":
            self.text.config(foreground=self.settings.foregroundColor)
        if self.settings.foregroundStipple != "":
            self.text.config(fgstipple=self.settings.foregroundStipple)
        if self.settings.height != "":
            self.text.config(height=int(self.settings.height))
        if self.settings.highlightBackgroundColor != "":
            self.text.config(highlightbackground=self.settings.highlightBackgroundColor)
        if self.settings.highlightColor != "":
            self.text.config(highlightcolor=self.settings.highlightColor)
        if self.settings.highlightThickness != "":
            self.text.config(highlightthickness=int(self.settings.highlightThickness))
        if self.settings.insertBackground != "":
            self.text.config(insertbackground=self.settings.insertBackground)
        if self.settings.insertBorderwidth != "":
            self.text.config(insertBorderwidth=int(self.settings.insertBorderwidth))
        if self.settings.insertOffTime != "":
            self.text.config(insertOffTime=int(self.settings.insertOffTime))
        if self.settings.insertOnTime != "":
            self.text.config(insertOnTime=int(self.settings.insertOnTime))
        if self.settings.insertWidth != "":
            self.text.config(insertWidth=int(self.settings.insertWidth))
        if self.settings.lmargin1 != "":
            self.text.config(lmargin1=int(self.settings.lmargin1))
        if self.settings.lmargin2 != "":
            self.text.config(lmargin2=int(self.settings.lmargin2))
        if self.settings.maxUndo != "":
            self.text.config(maxundo=int(self.settings.maxUndo))
        if self.settings.padX != "":
            self.text.config(padx=int(self.settings.padX))
        if self.settings.padY != "":
            self.text.config(pady=int(self.settings.padY))
        if self.settings.offset != "":
            self.text.config(offset=int(self.settings.offset))
        if self.settings.overstrike != "":
            self.text.config(overstrike=self.settings.overstrike)
        if self.settings.relief != "":
            self.text.config(offset=self.settings.relief)
        if self.settings.rmargin != "":
            self.text.config(overstrike=int(self.settings.rmargin))
        if self.settings.selectBackgroundColor != "":
            self.text.config(selectbackground=self.settings.selectBackgroundColor)
        if self.settings.selectForegroundColor != "":
            self.text.config(selectforeground=self.settings.selectForegroundColor)
        if self.settings.selectBorderwidth != "":
            self.text.config(selectborderwidth=int(self.settings.selectBorderwidth))
        if self.settings.setGrid != "":
            self.text.config(setgrid=self.settings.SetGrid)
        if self.settings.spacing1 != "":
            self.text.config(spacing1=int(self.settings.spacing1))
        if self.settings.spacing2 != "":
            self.text.config(spacing2=int(self.settings.spacing2))
        if self.settings.spacing3 != "":
            self.text.config(spacing3=int(self.settings.spacing3))
        if self.settings.state != "":
            self.text.config(state=self.settings.state)
        if self.settings.tabs != "":
            self.text.config(tabs=self.settings.tabs)
        if self.settings.takeFocus != "":
            self.text.config(takefocus=self.settings.takeFocus)
        if self.settings.text != "":
            self.text.insert(tk.END, self.settings.text)
        if self.settings.underline != "":
            self.text.config(underline=self.settings.underline)
        if self.settings.undo != "":
            self.text.config(undo=int(self.settings.undo))
        if self.settings.width != "":
            self.text.config(width=int(self.settings.width))
        if self.settings.wrap != "":
            self.text.config(wrap=self.settings.wrap)
        if self.settings.xScrollCommand != "":
            self.text.config(xscrollcommand=int(self.settings.xScrollCommand))
        if self.settings.yScrollCommand != "":
            self.text.config(yscrollcommand=int(self.settings.yScrollCommand))
        self.text.place()
        if self.placesettings.anchor != '':
            self.text.place_configure(anchor=self.placesettings.anchor)
        if self.placesettings.borderMode != '':
            self.text.place_configure(bordermode=self.placesettings.borderMode)
        if self.placesettings.height != '':
            self.text.place_configure(height=int(self.placesettings.height))
        if self.placesettings.relHeight != '':
            self.text.place_configure(relheight=int(self.placesettings.relHeight))
        if self.placesettings.width != '':
            self.text.place_configure(width=int(self.placesettings.width))
        if self.placesettings.relWidth != '':
            self.text.place_configure(relwidth=int(self.placesettings.relWidth))
        if self.placesettings.relX != '':
            self.text.place_configure(relx=int(self.placesettings.relX))
        if self.placesettings.relY != '':
            self.text.place_configure(rely=int(self.placesettings.relY))
        if self.placesettings.offsetX != '':
            self.text.place_configure(x=int(self.placesettings.offsetX))
        if self.placesettings.offsetY != '':
            self.text.place_configure(y=int(self.placesettings.offsetY))
        return self.text
    

    def SpawnButton(self, button, settings, placesettings):
        self.button = button
        self.button = tk.Button()
        self.settings = settings
        self.placesettings = placesettings
        if self.settings.backgroundColor != '':
            self.button.config(background=self.settings.backgroundColor)
        if self.settings.bitmap != '':
            self.button.config(bitmap=self.settings.bitmap)
        if self.settings.borderwidth != '':
            self.button.config(borderwidth=int(self.settings.borderwidth))
        if self.settings.command != '':
            self.button.config(command=lambda instance=int(self.settings.command):
            gui_callbacks.callback(self, instance, self.logfile))
        if self.settings.compound != '':
            self.button.config(compound=self.settings.compound)
        if self.settings.cursor != '':
            self.button.config(cursor=self.settings.cursor)
        if self.settings.default != '':
            self.button.config(default=self.settings.default)
        if self.settings.disableForeground != '':
            self.button.config(disableforeground=self.settings.disableForeground)
        if self.settings.font != '' and self.settings.fontSize != '':
            self.button.config(font=(self.settings.font, int(self.settings.fontSize)))
        if self.settings.foregroundColor != '':
            self.button.config(foreground=self.settings.foregroundColor)
        if self.settings.height != '':
            self.button.config(height=int(self.settings.height))
        if self.settings.highlightBackgroundColor != '':
            self.button.config(highlightbackground=self.settings.highlightBackgroundColor)
        if self.settings.highlightColor != '':
            self.button.config(highlightcolor=self.settings.highlightColor)
        if self.settings.highlightThickness != '':
            self.button.config(highlightthickness=int(self.settings.highlightThickness))
        if self.settings.image != '':
            self.button.config(image=self.settings.image)
        if self.settings.justify != '':
            self.button.config(justify=self.settings.justify)
        if self.settings.overRelief != '':
            self.button.config(overrelief=self.settings.overRelief)
        if self.settings.padX != '':
            self.button.config(padx=int(self.settings.padX))
        if self.settings.padY != '':
            self.button.config(pady=int(self.settings.padY))
        if self.settings.relief != '':
            self.button.config(relief=self.settings.relief)
        if self.settings.repeatDelay != '':
            self.button.config(repeatdelay=int(self.settings.repeatDelay))
        if self.settings.repeatInterval != '':
            self.button.config(repeatinterval=int(self.settings.repeatInterval))
        if self.settings.state != '':
            self.button.config(state=self.settings.state)
        if self.settings.takeFocus != '':
            self.button.config(takefocus=self.settings.takeFocus)
        if self.settings.text != '':
            self.button.config(text=self.settings.text)
        if self.settings.textVariable != '':
            self.button.config(textvariable=self.settings.textVariable)
        if self.settings.underline != '':
            self.button.config(underline=self.settings.underline)
        if self.settings.width != '':
            self.button.config(width=int(self.settings.width))
        if self.settings.wrapLength != '':
            self.button.config(wraplength=int(self.settings.wrapLength))
        self.button.place()            
        if self.placesettings.anchor != '':
            self.button.place_configure(anchor=self.placesettings.anchor)
        if self.placesettings.borderMode != '':
            self.button.place_configure(bordermode=self.placesettings.borderMode)
        if self.placesettings.height != '':
            self.button.place_configure(height=int(self.placesettings.height))
        if self.placesettings.width != '':
            self.button.place_configure(width=int(self.placesettings.width))
        if self.placesettings.relHeight != '':
            self.button.place_configure(relheight=int(self.placesettings.relHeight))
        if self.placesettings.relWidth != '':
            self.button.place_configure(relwidth=int(self.placesettings.relWidth))
        if self.placesettings.relX != '':
            self.button.place_configure(relx=int(self.placesettings.relX))
        if self.placesettings.relY != '':
            self.button.place_configure(rely=int(self.placesettings.relY))
        if self.placesettings.offsetX != '':
            self.button.place_configure(x=int(self.placesettings.offsetX))
        if self.placesettings.offsetY != '':
            self.button.place_configure(y=int(self.placesettings.offsetY))
        return self.button




    ####################################################################################################################
    # Define interface methods
    ####################################################################################################################
    def return_root(self):
        logging.info('[return_root] Returning window object')
        return self.root

    def kill_root(self):
        logging.info('[kill_root] Killing root window process')
        self.root.destroy()
        return

    def return_text(self, field):
        self.field = field
        self.address = self.field - 1
        logging.info('[return_text] Returning text from text field #%d' % self.field)
        return self.tkText[self.address].get("1.0", tk.END)

    def write_text(self, field, text):
        self.field = field
        self.address = self.field - 2
        self.text = text
        self.tkText[self.address].insert(tk.END, self.text)
        return

    def clear_text(self, field):
        self.field = field
        self.address = self.field - 1
        self.tkText[self.address].delete(1.0, tk.END)
        return




########################################################################################################################
#  Run if script is called manually
########################################################################################################################
        
if __name__ == "__main__":
    ioTable = int()
    AppWindowObject = AppWindow('gui_setup.ini', 'debug.ini', ioTable)
    app = AppWindow.SpawnAppWindow(AppWindowObject)