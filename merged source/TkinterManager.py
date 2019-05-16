import tkinter
import tkinter.ttk
import tkinter.font
from Error import *



class Viewport:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.right = left+width
        self.bottom = top+height
        self.width = width
        self.height = height
        
        
class widget:
    def __init__(self, widget):
        self.self = widget


class WindowManager(widget):
    def __init__(self, left=200, top=200, width=1280, height=720):
        super(WindowManager, self).__init__(tkinter.Tk())
        self.viewport = Viewport(left, top, width, height)
        self.self.geometry \
            ("{width}x{height}+{left}+{top}".format(width=self.viewport.width, height=self.viewport.height,
                                                                  left=self.viewport.left, top=self.viewport.top))
        self.self.resizable(False, False)

    def mainloop(self):
        self.self.mainloop()


class TabManager(widget):
    def __init__(self, window, viewport, upperGab=0):
        self.viewport = Viewport(viewport.left, viewport.top,
                                 viewport.width, viewport.height-upperGab )

        super(TabManager, self).__init__(tkinter.ttk.Notebook(window, width=self.viewport.width, height=self.viewport.height))
        self.self.pack()
        self.dictFrame = {}


    @staticmethod
    def setTabSytle():
        style = tkinter.ttk.Style()
        style.theme_create("tabStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [10, 4]} }})
        style.theme_use("tabStyle")


    def addTab(self, window, tabString=""):
        if tabString in self.dictFrame.keys():
            raise AlreadyInKeysOfDict("{str} is already in keys of dictFrame".format(str=tabString))
        frame = tkinter.Frame(window, width=self.viewport.width, height=self.viewport.height)
        self.self.add(frame, text=tabString)
        self.dictFrame[tabString] = frame


    def getFrame(self, strKey):
        return self.dictFrame[strKey]


# 미완
class Frame(widget):
    def __init__(self, window, viewport):
        super(Frame, self).__init__(tkinter.Frame(window))
        pass