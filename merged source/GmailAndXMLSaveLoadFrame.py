from CustomTkClass import*
from tkinter.filedialog import askopenfilename,asksaveasfile
class GmailAndXMLSaveLoadFrame(Frame):
    def __init__(self, mainframe, window, viewport):
        super(GmailAndXMLSaveLoadFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
        width = viewport.width

        TempFont = tkinter.font.Font(self, size=20, weight='bold', family='Consolas')

        tkinter.Label(self, font=TempFont, text="목록 내보내기 ").pack(side=tkinter.LEFT)

        setframe = tkinter.Frame(self)
        setframe.pack(side=tkinter.LEFT)
        gmailframe=tkinter.Frame(setframe)
        gmailframe.pack()
        TempFont = tkinter.font.Font(self, size=15, weight='bold', family='Consolas')
        tkinter.Label(gmailframe,   font=TempFont,text="Gmail   ").pack(side=tkinter.LEFT,anchor="w")
        self.gamilentry = tkinter.Entry(gmailframe, width=int((width - 160) / 10), text="Gmail")
        self.gamilentry.pack(side=tkinter.LEFT)
        tkinter.Button(gmailframe, text="보내기",command=self.sendEmail).pack(side=tkinter.RIGHT)

        xmlframe = tkinter.Frame(setframe)
        xmlframe.pack(anchor="w",fill="x")
        TempFont = tkinter.font.Font(self, size=15, weight='bold', family='Consolas')
        tkinter.Label(xmlframe,font=TempFont, text="XML 파일").pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="불러오기",command=self.XMLopen).pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="내보내기",command=self.XMLsave).pack(side=tkinter.LEFT)

    def sendEmail(self):
        pass
    def XMLopen(self):
        filename=askopenfilename()
    def XMLsave(self):
        asksaveasfile()
