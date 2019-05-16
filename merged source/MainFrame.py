
from TkinterManager import*
from SearchFrame import *



class MainFrame:
    def __init__(self):
        self.windowManager = WindowManager()

        TabManager.setTabSytle()
        self.tabs = TabManager(self.windowManager.self, self.windowManager.viewport)
        self.tabs.addTab(self.windowManager.self, "test_1")
        self.tabs.addTab(self.windowManager.self, "test_2")
        # self.test_frame = OptionFrame(self.tabs.getFrame("test_1"), 800, 600)
        self.windowManager.mainloop()




MainFrame()