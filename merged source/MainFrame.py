from CustomTkClass import*
from SearchFrame import *
from InformationFrame import *
from ReadingDataFromXML import *
from GmailAndXMLSaveLoadFrame import GmailAndXMLSaveLoadFrame
from GraphFrame import *


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
        optionFrame.place(x=optionFrame.viewport.left, y = optionFrame.viewport.top)

        self.infoFrame = InformationFrame(self, self.notebook.getFrame("test_1"),
                                            Viewport(
                                                self.notebook.getFrame("test_1").viewport.right-500,
                                                0,
                                                500,
                                                self.notebook.getFrame("test_1").viewport.height))
        self.infoFrame.place(x= self.infoFrame.viewport.left, y =  self.infoFrame.viewport.top)



        self.selectionInfoFrame= InformationFrame(self, self.notebook.getFrame("test_2"),
                                            Viewport(
                                                0,
                                                0,
                                                500,
                                                500))
        self.selectionInfoFrame.place(x= self.selectionInfoFrame.viewport.left, y =  self.selectionInfoFrame.viewport.top)

        self.graphFrame = GraphFrame(self, self.notebook.getFrame("test_2"),
                                Viewport(
                                    500,
                                    0,
                                    300,
                                    500))
        self.graphFrame.place(x= self.graphFrame.viewport.left, y= self.graphFrame.viewport.top)
        self.gmailFrame = GmailAndXMLSaveLoadFrame(self, self.notebook.getFrame("test_2"),
                                              Viewport(
                                                  0,
                                                  500,
                                                  self.notebook.getFrame("test_2").viewport.width,
                                                  self.notebook.getFrame("test_2").viewport.height - 500
                                              ))
        self.gmailFrame.place(x= self.gmailFrame.viewport.left, y= self.gmailFrame.viewport.top)


    def mainloop(self):
        self.window.mainloop()

    def buildNotebook(self):
        Notebook.setTabSytle()
        self.notebook = Notebook(self.window)
        # self.tabs.addTab(self.window, self.window.viewport, "test_1")
        # self.tabs.addTab(self.window, self.window.viewport, "test_2")
        tab1Viewport = Viewport(0, 0, 800, 500)
        tab2Viewport = Viewport(0, 0, 800, 600)


        self.notebook.addTab(self.window, tab1Viewport, "test_1")
        self.notebook.addTab(self.window, tab2Viewport, "test_2")

    def reciveEvent(self, **events):
        # 미완
        for (event, eventData) in events.items():
            if event == "search":
                DOMReadingManager.initSearchOption()
                DOMReadingManager.setWithFormattedOptionList(eventData)
                dataes = DOMReadingManager.searchDataes()
                self.infoFrame.setDataList(dataes)
                self.infoFrame.updateListbox()









mainframe = MainFrame()
DOMReadingManager.readXML()
mainframe.mainloop()