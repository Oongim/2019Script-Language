from CustomTkClass import*

class InformationFrame(Frame):
    listboxHeightRatio = 0.4
    infoWidthRatio = 0.5
    def __init__(self, mainframe, window, viewport):
        super(InformationFrame, self).__init__(window, viewport)
        self.mainframe = mainframe

        # UI 생성
        self.initListboxFrame()
        self.initInfomationFrame()
        self.initMapFrame()


    def initListboxFrame(self):
        vpListbox = Viewport(
            0,
            0,
            self.viewport.width,
            self.viewport.height * InformationFrame.listboxHeightRatio
        )
        vpListbox.makeElementToInt()

        self.listbox = tkinter.Listbox(self, width=vpListbox.width)
        self.listbox.place(x=vpListbox.left, y=vpListbox.top,
                           width=vpListbox.width, height=vpListbox.height)

    def initInfomationFrame(self):
        vpInfoFrame = Viewport(
            0,
            0 + self.viewport.height * InformationFrame.listboxHeightRatio,
            self.viewport.width * InformationFrame.infoWidthRatio,
            self.viewport.height * (1-InformationFrame.listboxHeightRatio)
        )
        vpInfoFrame.makeElementToInt()

        self.test1 = tkinter.Listbox(self, width=vpInfoFrame.width)
        self.test1.place(x=vpInfoFrame.left, y=vpInfoFrame.top,
                           width=vpInfoFrame.width, height=vpInfoFrame.height)

    def initMapFrame(self):
        vpMapFrame = Viewport(
            0 + self.viewport.width * InformationFrame.infoWidthRatio,
            0 + self.viewport.height * InformationFrame.listboxHeightRatio,
            self.viewport.width * (1 - InformationFrame.infoWidthRatio),
            self.viewport.height * (1 - InformationFrame.listboxHeightRatio)
        )
        vpMapFrame.makeElementToInt()

        self.test2 = tkinter.Listbox(self, width=vpMapFrame.width)
        self.test2.place(x=vpMapFrame.left, y=vpMapFrame.top,
                         width=vpMapFrame.width, height=vpMapFrame.height)
