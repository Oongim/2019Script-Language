import tkinter
import tkinter.ttk
import tkinter.font
from Error import *



class Viewport:
    def __init__(self, left=0, top=0, width=0, height=0):
        self.left = left
        self.top = top
        self.right = left+width
        self.bottom = top+height
        self.width = width
        self.height = height

    def makeElementToInt(self):
        self.left = int(self.left)
        self.top = int(self.top)
        self.right = int(self.right)
        self.bottom = int(self.bottom)
        self.width = int(self.width)
        self.height = int(self.height)


class Window(tkinter.Tk):
    def __init__(self, left=200, top=200, width=1280, height=720):
        super(Window, self).__init__()
        self.resizable(False, False)
        self.viewport = Viewport(left, top, width, height)
        self.resize(width=width, height=height, left=left, top=top)


    def resize(self, width, height, left=None, top=None):
        if not left == None:
            self.viewport.left = left
        if not top == None:
            self.viewport.top = top
        self.viewport.width = width
        self.viewport.height = height
        self.geometry \
            ("{width}x{height}+{left}+{top}".format(width=self.viewport.width, height=self.viewport.height,
                                                    left=self.viewport.left, top=self.viewport.top))


class Notebook(tkinter.ttk.Notebook):
    upperGab = 15
    tabHeight = 35
    def __init__(self, window):
        self.window = window
        super(Notebook, self).__init__(window)
        self.pack()
        self.bind("<<NotebookTabChanged>>", Notebook.funcOnTabChanged)
        self.tabStackCount = 0
        self.dictTabFrame = {}
        self.dictTabIndex = {}
        self.dictTabFrameFromIndex = {}


    @staticmethod
    def setTabSytle():
        style = tkinter.ttk.Style()
        style.theme_create("tabStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
            "TNotebook.Tab": {"configure": {"padding": [10, 4]}}})
        style.theme_use("tabStyle")


    def addTab(self, window, viewport, tabName=""):
        if tabName in self.dictTabIndex.keys():
            raise AlreadyInKeysOfDict("{str} is already in keys of dictTabID".format(str=tabName))
        tabFrame = TabFrame(window, viewport)
        self.add(tabFrame, text=tabName)
        self.dictTabFrame[tabName] = tabFrame
        self.dictTabIndex[tabName] = str(self.tabStackCount)
        self.dictTabFrameFromIndex[str(self.tabStackCount)] = tabFrame
        self.tabStackCount = self.tabStackCount + 1

    def resize(self, width, height):
        self.configure(width=width, height=height)

    def getFrame(self, strKey):
        return self.dictTabFrame[strKey]

    def getFrameFromID(self, tabID):
        for frame in self.dictTabFrame.values():
            if frame._w == tabID:
                return frame
        return None

    def selectTab(self, strKey):
        self.select(self.dictTabIndex[strKey])

    @staticmethod
    def funcOnTabChanged(tab):
        tab.widget.getFrameFromID(tab.widget.select()).onVisibility()



class Frame(tkinter.Frame):
    def __init__(self, window, viewport):
        self.window = window
        self.viewport = viewport
        super(Frame, self).__init__(window, width=viewport.width, height=viewport.height)

class TabFrame(Frame):
    def __init__(self, window, viewport):
        super(TabFrame, self).__init__(window, viewport)

    def onVisibility(self):
        # 노트북의 크기 전환은 할 필요없음. 자동으로 되는 듯
        self.window.resize(width=self.viewport.width, height=self.viewport.height+Notebook.tabHeight)


class DescLabel:
    def __init__(self, window, viewport, kindText, dataText, kindLabelWidth, dataLabelWidth):
        self.window = window
        self.viewport = viewport
        self.labelFont = tkinter.font.Font(window, size=10, weight='bold', family='Consolas')

        self.kindLabel = tkinter.Label(window, font=self.labelFont, text=kindText, width=kindLabelWidth, height=1, anchor="e")
        self.dataLabel = tkinter.Label(window, font=self.labelFont, text=dataText, width=dataLabelWidth, height=1, anchor="w")

        self.kindLabel.place(x=viewport.left, y=viewport.top, anchor="nw")
        self.dataLabel.place(x=viewport.right, y=viewport.top, anchor="ne")

        #디버그용 코드
        # self.kindLabel.configure(bg="blue")
        # self.dataLabel.configure(bg="red")

    def setTextDataLabel(self, text):
        self.dataLabel.configure(text=text)


