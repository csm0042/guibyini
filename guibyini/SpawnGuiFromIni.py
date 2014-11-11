import tkinter as tk
import widget_count
import tkinterWindow
import tkinterFrame
import tkinterMessage


class SpawnAppWindow:
    def __init__(self, parent, iniFile):
        self.parent = parent
        self.iniFile = iniFile
        self.section_to_read = str()

        self.window = tkinterWindow.Window()

        # Create tag list for frame settings
        self.frameCount = widget_count.CountWidgetByType(self.iniFile, "frame")
        self.frameDataRead = 0
        self.framesCreated = 0
        self.Frame = [tkinterFrame.Frame()]*self.frameCount
        #self.Frame = tkinterFrame.Frame()
        #for i in range(self.frameCount-1):
        #    self.Frame.append(tkinterFrame.Frame())

        # Create tag lists for message settings
        self.messageCount = widget_count.CountWidgetByType(self.iniFile, "message")
        self.messageDataRead = 0
        self.messagesCreated = 0
        self.Messages = [tkinterMessage.Message()]*self.messageCount
        #self.Message = tkinterMessage.Message()
        #for i in range(self.messageCount-1):
        #    self.Message.append(tkinterMessage.Message())

        # Call function to populate setting tags
        self.initialize()

        # Call function to generate window using obtained settings
        self.build()




    def initialize(self):

        self.section_to_read = "window"
        self.Window = tkinterWindow.read_settings(self.iniFile, self.section_to_read)

        for i in range(self.frameCount):
            self.section_to_read = "frame" + str(self.i+1)
            self.Frame[i] = tkinterFrame.read_settings(self.iniFile, self.section_to_read)

        for i in range(self.messageCount):
            self.section_to_read = "message" + str(self.i+1)
            self.Frame[i] = tkinterMessage.read_settings(self.iniFile, self.section_to_read)




    def build(self):

        tkinterWindow.apply_settings(self.window)

        for i in range(self.frameCount):
            tk.Frame().place()
            tkinterFrame.apply_settings(self.Frame[i])

        for i in range(self.messageCount):
            tk.Message().place()
            tkinterMessage.apply_settings(self.Message[i])










if __name__ == "__main__":
    root=tk.Tk()
    app = SpawnAppWindow(root, 'gui.ini')
    root.title('My App Window')
    root.mainloop()