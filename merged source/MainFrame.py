
from CustomTkClass import*
from SearchFrame import *



class MainFrame:
    def __init__(self):
        self.window = Window()
        self.buildNotebook()

        self.test_frame = OptionFrame(self.notebook.getFrame("test_1"), 800, 500)
        self.window.mainloop()

    def buildNotebook(self):
        Notebook.setTabSytle()
        self.notebook = Notebook(self.window)
        # self.tabs.addTab(self.window, self.window.viewport, "test_1")
        # self.tabs.addTab(self.window, self.window.viewport, "test_2")
        self.tab1Viewport = Viewport(0, 0, 800, 500)
        tab2Viewport = Viewport(0, 0, 500, 300)


        self.notebook.addTab(self.window, self.tab1Viewport, "test_1")
        self.notebook.addTab(self.window, tab2Viewport, "test_2")


MainFrame()