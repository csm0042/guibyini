import logging
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
class gui(object):
    def __init__(self, inifile, logfile, iotable):
        self.inifile = inifile
        self.logfile = logfile
        self.iotable = iotable
        self.field = int()
        self.address = int()
        self.text = str()
        self.place_settings = tkinterPlace.Place()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[gui.__init__] Appwindow object created')

        self.root = tk.Tk()
        self.section = str()
        self.Window = tkinterWindow.Window()

        self.frameCount = widget_count.CountWidgetByType(self.inifile, "frame")
        self.Frame = tkinterFrame.Frame()
        self.frame_settings = tkinterFrame.Frame()
        self.FramePlace = tkinterPlace.Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
        logging.info('[gui.__init__] Found configuration data for %d "frame" widgets' %self.frameCount)

        self.messageCount = widget_count.CountWidgetByType(self.inifile, "message")
        self.Message = tkinterMessage.Message()
        self.message_settings = tkinterMessage.Message()
        self.MessagePlace = tkinterPlace.Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        logging.info('[gui.__init__] Found configuration data for %d "message" widgets' %self.messageCount)

        self.textCount = widget_count.CountWidgetByType(self.inifile, "text")
        self.Text = tkinterText.Text()
        self.text_settings = tkinterText.Text()
        self.TextPlace = tkinterPlace.Place()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        self.tkTextHandshake = [str() for i in range(self.textCount)]
        logging.info('[gui.__init__] Found configuration data for %d "text" widgets' %self.textCount)

        self.buttonCount = widget_count.CountWidgetByType(self.inifile, "button")
        self.Button = tkinterButton.Button()
        self.button_settings = tkinterButton.Button()
        self.ButtonPlace = tkinterPlace.Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        self.ButtonInput = [bool() for i in range(self.buttonCount)]
        logging.info('[gui.__init__] Found configuration data for %d "button" widgets' %self.buttonCount)



    def create_window(self):

        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window.section = "main window"
        self.Window.iniFile = self.inifile
        self.Window = tkinterWindow.Window.read_settings(self.Window)
        logging.info('[gui.create_window] Adjusting window geometry')
        self.root.geometry("%sx%s+%s+%s" % (int(self.Window.width), int(self.Window.height), int(self.Window.posX),
                                            int(self.Window.posY)))
        logging.info('[gui.create_window] Adjusting window background color')
        if self.Window.backgroundColor != "":
            self.root.config(background=self.Window.backgroundColor)
        logging.info('[gui.create_window] Setting window title')
        if self.Window.title != '':
            self.root.title(self.Window.title)


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "frame" widget loop')
        for i in range(0, self.frameCount):
            self.Frame.iniFile = self.FramePlace.iniFile = self.inifile
            self.Frame.section = self.FramePlace.section = str("frame" + str(i+1))
            self.Frame.read_settings()
            self.FramePlace.read_settings()
            logging.info('[gui.create_window] Creating frame widget #%d' % (i+1))
            self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE MESSAGE WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "message" widget loop')
        for i in range(0, self.messageCount):
            self.Message.iniFile = self.MessagePlace.iniFile = self.inifile
            self.Message.section = self.MessagePlace.section = "message" + str(i+1)
            self.Message.read_settings()
            self.MessagePlace.read_settings()
            logging.info('[gui.create_window] Creating message widget #%d' % (i+1))
            self.tkMessage[i] = self.create_message_widget(self.tkMessage[i], self.Message, self.MessagePlace)


        ################################################################################################################
        # CALL LOOP TO CREATE TEXT WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "text" widget loop')
        for i in range(0, self.textCount):
            self.Text.iniFile = self.TextPlace.iniFile = self.inifile
            self.Text.section = self.TextPlace.section = str("text" + str(i+1))
            self.Text.read_settings()
            self.TextPlace.read_settings()
            logging.info('[gui.create_window] Creating text widget #%d' % (i+1))
            self.tkText[i] = self.create_text_widget(self.tkText[i], self.Text, self.TextPlace)


        ################################################################################################################
        # CALL LOOP TO CREATE BUTTON WIDGETS
        ################################################################################################################
        logging.info('[gui.create_window] Starting "button" widget loop')
        for i in range(0, self.buttonCount):
            self.Button.iniFile = self.ButtonPlace.iniFile = self.inifile
            self.Button.section = self.ButtonPlace.section = "button" + str(i+1)
            self.Button.read_settings()
            self.ButtonPlace.read_settings()
            logging.info('[gui.create_window] Creating button widget #%d' % (i+1))
            self.tkButton[i] = self.create_button_widget(self.tkButton[i], self.Button, self.ButtonPlace)

        logging.info('[gui.create_window] Starting tkinter main loop')
        self.root.mainloop()
        return self



    def create_frame_widget(self, frame, frame_settings, place_settings):
        self.frame = frame
        self.frame_settings = frame_settings
        self.place_settings = place_settings
        if self.frame_settings.backgroundColor != '':
            self.frame.config(background=self.frame_settings.backgroundColor)
        if self.frame_settings.borderwidth != '':
            self.frame.config(borderwidth=int(self.frame_settings.borderwidth))
        if self.frame_settings.colormap != '':
            self.frame.config(colormap=self.frame_settings.colormap)
        if self.frame_settings.container != '':
            self.frame.config(container=self.frame_settings.container)
        if self.frame_settings.cursor != '':
            self.frame.config(cursor=self.frame_settings.cursor)
        if self.frame_settings.height != '':
            self.frame.config(height=int(self.frame_settings.height))
        if self.frame_settings.highlightBackgroundColor != '':
            self.frame.config(highlightbackground=self.frame_settings.highlightBackgroundColor)
        if self.frame_settings.highlightColor != '':
            self.frame.config(highlightcolor=self.frame_settings.highlightColor)
        if self.frame_settings.highlightThickness != '':
            self.frame.config(highlightthickness=int(self.frame_settings.highlightThickness))
        if self.frame_settings.padX != '':
            self.frame.config(padx=int(self.frame_settings.padX))
        if self.frame_settings.padY != '':
            self.frame.config(pady=int(self.frame_settings.padY))
        if self.frame_settings.relief != '':
            self.frame.config(relief=self.frame_settings.relief)
        if self.frame_settings.takeFocus != '':
            self.frame.config(takefocus=self.frame_settings.takeFocus)
        if self.frame_settings.visual != '':
            self.frame.config(visual=self.frame_settings.visual)
        if self.frame_settings.width != '':
            self.frame.config(width=int(self.frame_settings.width))
        self.frame.place()
        if self.place_settings.anchor != '':
            self.frame.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.frame.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.frame.place_configure(height=int(self.place_settings.height))
        if self.place_settings.width != '':
            self.frame.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relHeight != '':
            self.frame.place_configure(relheight=float(self.place_settings.relHeight))
        if self.place_settings.relWidth != '':
            self.frame.place_configure(relwidth=float(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.frame.place_configure(relx=float(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.frame.place_configure(rely=float(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.frame.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.frame.place_configure(y=int(self.place_settings.offsetY))
        return self.frame


    def create_message_widget(self, message, message_settings, place_settings):
        self.message = message
        self.message_settings = message_settings
        self.place_settings = place_settings
        if self.message_settings.anchor != "":
            self.message.config(anchor=self.message_settings.anchor)
        if self.message_settings.aspect != "":
            self.message.config(aspect=self.message_settings.aspect)
        if self.message_settings.backgroundColor != "":
            self.message.config(background=self.message_settings.backgroundColor)
        if self.message_settings.borderwidth != "":
            self.message.config(borderwidth=self.message_settings.borderwidth)
        if self.message_settings.cursor != "":
            self.message.config(cursor=self.message_settings.cursor)
        if self.message_settings.font != "" and self.message_settings.fontSize != "":
            self.message.config(font=(self.message_settings.font, int(self.message_settings.fontSize)))
        if self.message_settings.foregroundColor != "":
            self.message.config(foreground=self.message_settings.foregroundColor)
        if self.message_settings.highlightBackground != "":
            self.message.config(highlightbackground=self.message_settings.highlightBackground)
        if self.message_settings.highlightBackgroundColor != "":
            self.message.config(highlightcolor=self.message_settings.highlightBackgroundColor)
        if self.message_settings.highlightThickness != "":
            self.message.config(highlightthickness=int(self.message_settings.highlightThickness))
        if self.message_settings.justify != "":
            self.message.config(justify=self.message_settings.justify)
        if self.message_settings.padX != "":
            self.message.config(padx=int(self.message_settings.padX))
        if self.message_settings.padY != "":
            self.message.config(pady=int(self.message_settings.padY))
        if self.message_settings.relief != "":
            self.message.config(relief=self.message_settings.relief)
        if self.message_settings.takeFocus != "":
            self.message.config(takefocus=self.message_settings.takeFocus)
        if self.message_settings.text != "":
            self.message.config(text=self.message_settings.text)
        if self.message_settings.textVariable != "":
            self.message.config(textvariable=self.message_settings.textVariable)
        if self.message_settings.width != "":
            self.message.config(width=int(self.message_settings.width))
        self.message.place()
        if self.place_settings.anchor != '':
            self.message.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.message.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.message.place_configure(height=int(self.place_settings.height))
        if self.place_settings.relHeight != '':
            self.message.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.width != '':
            self.message.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relWidth != '':
            self.message.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.message.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.message.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.message.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.message.place_configure(y=int(self.place_settings.offsetY))
        return self.message


    def create_text_widget(self, text, text_settings, place_settings):
        self.text = text
        self.text_settings = text_settings
        self.place_settings = place_settings
        if self.text_settings.autoSeparators != "":
            self.text.config(autoseparators=self.text_settings.autoSeparators)
        if self.text_settings.backgroundColor != "":
            self.text.config(bg=self.text_settings.backgroundColor)
        if self.text_settings.backgroundStipple != "":
            self.text.config(bgstipple=self.text_settings.backgroundStipple)
        if self.text_settings.borderwidth != "":
            self.text.config(bd=int(self.text_settings.borderwidth))
        if self.text_settings.foregroundStipple != "":
            self.text.config(fgstipple=self.text_settings.foregroundStipple)
        if self.text_settings.cursor != "":
            self.text.config(cursor=self.text_settings.cursor)
        if self.text_settings.exportSelection != "":
            self.text.config(exportselection=self.text_settings.exportSelection)
        if self.text_settings.font != "" and self.text_settings.fontSize != "":
            self.text.config(font=(self.text_settings.font, int(self.text_settings.fontSize)))
        if self.text_settings.foregroundColor != "":
            self.text.config(foreground=self.text_settings.foregroundColor)
        if self.text_settings.foregroundStipple != "":
            self.text.config(fgstipple=self.text_settings.foregroundStipple)
        if self.text_settings.height != "":
            self.text.config(height=int(self.text_settings.height))
        if self.text_settings.highlightBackgroundColor != "":
            self.text.config(highlightbackground=self.text_settings.highlightBackgroundColor)
        if self.text_settings.highlightColor != "":
            self.text.config(highlightcolor=self.text_settings.highlightColor)
        if self.text_settings.highlightThickness != "":
            self.text.config(highlightthickness=int(self.text_settings.highlightThickness))
        if self.text_settings.insertBackground != "":
            self.text.config(insertbackground=self.text_settings.insertBackground)
        if self.text_settings.insertBorderwidth != "":
            self.text.config(insertBorderwidth=int(self.text_settings.insertBorderwidth))
        if self.text_settings.insertOffTime != "":
            self.text.config(insertOffTime=int(self.text_settings.insertOffTime))
        if self.text_settings.insertOnTime != "":
            self.text.config(insertOnTime=int(self.text_settings.insertOnTime))
        if self.text_settings.insertWidth != "":
            self.text.config(insertWidth=int(self.text_settings.insertWidth))
        if self.text_settings.lmargin1 != "":
            self.text.config(lmargin1=int(self.text_settings.lmargin1))
        if self.text_settings.lmargin2 != "":
            self.text.config(lmargin2=int(self.text_settings.lmargin2))
        if self.text_settings.maxUndo != "":
            self.text.config(maxundo=int(self.text_settings.maxUndo))
        if self.text_settings.padX != "":
            self.text.config(padx=int(self.text_settings.padX))
        if self.text_settings.padY != "":
            self.text.config(pady=int(self.text_settings.padY))
        if self.text_settings.offset != "":
            self.text.config(offset=int(self.text_settings.offset))
        if self.text_settings.overstrike != "":
            self.text.config(overstrike=self.text_settings.overstrike)
        if self.text_settings.relief != "":
            self.text.config(offset=self.text_settings.relief)
        if self.text_settings.rmargin != "":
            self.text.config(overstrike=int(self.text_settings.rmargin))
        if self.text_settings.selectBackgroundColor != "":
            self.text.config(selectbackground=self.text_settings.selectBackgroundColor)
        if self.text_settings.selectForegroundColor != "":
            self.text.config(selectforeground=self.text_settings.selectForegroundColor)
        if self.text_settings.selectBorderwidth != "":
            self.text.config(selectborderwidth=int(self.text_settings.selectBorderwidth))
        if self.text_settings.setGrid != "":
            self.text.config(setgrid=self.text_settings.SetGrid)
        if self.text_settings.spacing1 != "":
            self.text.config(spacing1=int(self.text_settings.spacing1))
        if self.text_settings.spacing2 != "":
            self.text.config(spacing2=int(self.text_settings.spacing2))
        if self.text_settings.spacing3 != "":
            self.text.config(spacing3=int(self.text_settings.spacing3))
        if self.text_settings.state != "":
            self.text.config(state=self.text_settings.state)
        if self.text_settings.tabs != "":
            self.text.config(tabs=self.text_settings.tabs)
        if self.text_settings.takeFocus != "":
            self.text.config(takefocus=self.text_settings.takeFocus)
        if self.text_settings.text != "":
            self.text.insert(tk.END, self.text_settings.text)
        if self.text_settings.underline != "":
            self.text.config(underline=self.text_settings.underline)
        if self.text_settings.undo != "":
            self.text.config(undo=int(self.text_settings.undo))
        if self.text_settings.width != "":
            self.text.config(width=int(self.text_settings.width))
        if self.text_settings.wrap != "":
            self.text.config(wrap=self.text_settings.wrap)
        if self.text_settings.xScrollCommand != "":
            self.text.config(xscrollcommand=int(self.text_settings.xScrollCommand))
        if self.text_settings.yScrollCommand != "":
            self.text.config(yscrollcommand=int(self.text_settings.yScrollCommand))
        self.text.place()
        if self.place_settings.anchor != '':
            self.text.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.text.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.text.place_configure(height=int(self.place_settings.height))
        if self.place_settings.relHeight != '':
            self.text.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.width != '':
            self.text.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relWidth != '':
            self.text.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.text.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.text.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.text.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.text.place_configure(y=int(self.place_settings.offsetY))
        return self.text
    

    def create_button_widget(self, button, button_settings, place_settings):
        self.button = button
        self.button_settings = button_settings
        self.place_settings = place_settings
        if self.button_settings.backgroundColor != '':
            self.button.config(background=self.button_settings.backgroundColor)
        if self.button_settings.bitmap != '':
            self.button.config(bitmap=self.button_settings.bitmap)
        if self.button_settings.borderwidth != '':
            self.button.config(borderwidth=int(self.button_settings.borderwidth))
        if self.button_settings.command != '':
            self.button.config(command=lambda instance=int(self.button_settings.command):
            gui_callbacks.callback(self, instance, self.logfile))
        if self.button_settings.compound != '':
            self.button.config(compound=self.button_settings.compound)
        if self.button_settings.cursor != '':
            self.button.config(cursor=self.button_settings.cursor)
        if self.button_settings.default != '':
            self.button.config(default=self.button_settings.default)
        if self.button_settings.disableForeground != '':
            self.button.config(disableforeground=self.button_settings.disableForeground)
        if self.button_settings.font != '' and self.button_settings.fontSize != '':
            self.button.config(font=(self.button_settings.font, int(self.button_settings.fontSize)))
        if self.button_settings.foregroundColor != '':
            self.button.config(foreground=self.button_settings.foregroundColor)
        if self.button_settings.height != '':
            self.button.config(height=int(self.button_settings.height))
        if self.button_settings.highlightBackgroundColor != '':
            self.button.config(highlightbackground=self.button_settings.highlightBackgroundColor)
        if self.button_settings.highlightColor != '':
            self.button.config(highlightcolor=self.button_settings.highlightColor)
        if self.button_settings.highlightThickness != '':
            self.button.config(highlightthickness=int(self.button_settings.highlightThickness))
        if self.button_settings.image != '':
            self.button.config(image=self.button_settings.image)
        if self.button_settings.justify != '':
            self.button.config(justify=self.button_settings.justify)
        if self.button_settings.overRelief != '':
            self.button.config(overrelief=self.button_settings.overRelief)
        if self.button_settings.padX != '':
            self.button.config(padx=int(self.button_settings.padX))
        if self.button_settings.padY != '':
            self.button.config(pady=int(self.button_settings.padY))
        if self.button_settings.relief != '':
            self.button.config(relief=self.button_settings.relief)
        if self.button_settings.repeatDelay != '':
            self.button.config(repeatdelay=int(self.button_settings.repeatDelay))
        if self.button_settings.repeatInterval != '':
            self.button.config(repeatinterval=int(self.button_settings.repeatInterval))
        if self.button_settings.state != '':
            self.button.config(state=self.button_settings.state)
        if self.button_settings.takeFocus != '':
            self.button.config(takefocus=self.button_settings.takeFocus)
        if self.button_settings.text != '':
            self.button.config(text=self.button_settings.text)
        if self.button_settings.textVariable != '':
            self.button.config(textvariable=self.button_settings.textVariable)
        if self.button_settings.underline != '':
            self.button.config(underline=self.button_settings.underline)
        if self.button_settings.width != '':
            self.button.config(width=int(self.button_settings.width))
        if self.button_settings.wrapLength != '':
            self.button.config(wraplength=int(self.button_settings.wrapLength))
        self.button.place()            
        if self.place_settings.anchor != '':
            self.button.place_configure(anchor=self.place_settings.anchor)
        if self.place_settings.borderMode != '':
            self.button.place_configure(bordermode=self.place_settings.borderMode)
        if self.place_settings.height != '':
            self.button.place_configure(height=int(self.place_settings.height))
        if self.place_settings.width != '':
            self.button.place_configure(width=int(self.place_settings.width))
        if self.place_settings.relHeight != '':
            self.button.place_configure(relheight=int(self.place_settings.relHeight))
        if self.place_settings.relWidth != '':
            self.button.place_configure(relwidth=int(self.place_settings.relWidth))
        if self.place_settings.relX != '':
            self.button.place_configure(relx=int(self.place_settings.relX))
        if self.place_settings.relY != '':
            self.button.place_configure(rely=int(self.place_settings.relY))
        if self.place_settings.offsetX != '':
            self.button.place_configure(x=int(self.place_settings.offsetX))
        if self.place_settings.offsetY != '':
            self.button.place_configure(y=int(self.place_settings.offsetY))
        return self.button




    ####################################################################################################################
    # Define interface methods
    ####################################################################################################################
    def return_root(self):
        logging.info('[gui.return_root] Returning window object')
        return self.root

    def kill_root(self):
        logging.info('[gui.kill_root] Killing root window process')
        self.root.destroy()
        return

    def return_text(self, field):
        self.field = field
        self.address = self.field - 1
        logging.info('[gui.return_text] Returning text from text field #%d' % self.field)
        return self.tkText[self.address].get("1.0", tk.END)

    def write_text(self, field, text):
        self.field = field
        self.address = self.field - 2
        self.text = text
        self.tkText[self.address].insert(tk.END, self.text)
        logging.info('[gui.write_text] Writing text to text field #%d' % self.field)
        return

    def clear_text(self, field):
        self.field = field
        self.address = self.field - 2
        self.tkText[self.address].delete(1.0, tk.END)
        logging.info('[gui.clear_text] Clearing text to text field #%d' % self.field)
        return




########################################################################################################################
#  Run if script is called manually
########################################################################################################################
        
if __name__ == "__main__":
    ioTable = int()
    AppWindowObject = gui('gui_setup.ini', 'debug.log', ioTable)
    app = AppWindowObject.create_window()