from CustomTkClass import*
from SearchFrame import *
from InformationFrame import *
from ReadingDataFromXML import *



class MainFrame:
    def __init__(self):
        self.window = Window()
        self.buildNotebook()


        optionFrame = OptionFrame(self, self.notebook.getFrame("test_1"),
                                  Viewport(
                                      0,
                                      0,
                                      self.notebook.getFrame("test_1").viewport.right-500,
                                      self.notebook.getFrame("test_1").viewport.height))
        optionFrame.pack(side=tkinter.LEFT)

        infoFrame = InformationFrame(self, self.notebook.getFrame("test_1"),
                                            Viewport(
                                                self.notebook.getFrame("test_1").viewport.right-500,
                                                0,
                                                500,
                                                self.notebook.getFrame("test_1").viewport.height))
        infoFrame.pack(side=tkinter.RIGHT)

        selectionInfoFrame= InformationFrame(self, self.notebook.getFrame("test_2"),
                                            Viewport(
                                                0,
                                                0,
                                                200,
                                                self.notebook.getFrame("test_2").viewport.height))
        selectionInfoFrame.pack(side=tkinter.LEFT)

        self.window.mainloop()

    def buildNotebook(self):
        Notebook.setTabSytle()
        self.notebook = Notebook(self.window)
        # self.tabs.addTab(self.window, self.window.viewport, "test_1")
        # self.tabs.addTab(self.window, self.window.viewport, "test_2")
        tab1Viewport = Viewport(0, 0, 800, 500)
        tab2Viewport = Viewport(0, 0, 500, 300)


        self.notebook.addTab(self.window, tab1Viewport, "test_1")
        self.notebook.addTab(self.window, tab2Viewport, "test_2")

    def reciveEvent(self, **events):
        # 미완
        for (event, eventData) in events.items():
            if event == "search":
                DOMReadingManager.initSearchOption()
                DOMReadingManager.setWithFormattedOptionList(eventData)
                dataes = DOMReadingManager.readXML()









MainFrame()