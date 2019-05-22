from CustomTkClass import*
from SearchFrame import *


class MainFrame:
    def __init__(self):
        self.window = Window()
        self.buildNotebook()


        optionFrame = OptionFrame(self.notebook.getFrame("test_1"),
                                    Viewport(0, 0,
                                      self.notebook.getFrame("test_1").viewport.right-500,
                                      self.notebook.getFrame("test_1").viewport.height))
        optionFrame.grid(row=0, column=0)


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


MainFrame()