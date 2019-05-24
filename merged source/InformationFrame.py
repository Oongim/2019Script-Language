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

    def setDataList(self, dataList):
        self.dataList = dataList


    def update(self):
        vpListbox = Viewport(
            0,
            0,
            self.viewport.width,
            self.viewport.height * InformationFrame.listboxHeightRatio
        )
        vpListbox.makeElementToInt()
        self.listbox.delete(0, tkinter.END)
        i = 0
        for data in self.dataList:
            dataString = "동 : {동}   월세 : {월세}만원   보증금 : {보증금}만원   면적 : {면적}m2".format(
                   동=data.find("법정동"), 월세=data.find("월세금액"), 보증금=data.find("보증금액"), 면적=data.find("면적"))
            self.listbox.insert(i, dataString)
        # self.listbox.place(x=vpListbox.left, y=vpListbox.top,
        #                    width=vpListbox.width, height=vpListbox.height)

