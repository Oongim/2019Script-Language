from CustomTkClass import*
from SearchFrame import *
from InformationFrame import *
from ReadingDataFromXML import *
from GmailAndXMLSaveLoadFrame import GmailAndXMLSaveLoadFrame
from GraphFrame import GraphFrame
from SettingFrame import SettingFrmae
from logoLoading import logoLoading
from ReadingDataFromXML import XML_SAVE_DIR_NAME
import os

mfViewport = Viewport(100, 100, 800, 500)       # mainframeViewport
tab1Viewport = Viewport(0, 0, mfViewport.width, mfViewport.height)
tab2Viewport = Viewport(0, 0, mfViewport.width, mfViewport.height + 60)  # 메일 보내는 프레임의 height가 약 60
tab3Viewport = Viewport(0, 0, mfViewport.width, mfViewport.height)

tab1_name = "test_1"
tab2_name = "test_2"
tab3_name = "test_3"

class MainFrame:
    def __init__(self):
        self.window = Window()
        self.window.resize(mfViewport.width, mfViewport.height, mfViewport.left, mfViewport.top)

        self.window.title("산기대방구하기")
        self.window.iconbitmap(os.getcwd() + '\Image\logo_icon.ico')

        self.buildNotebook()
        self.dataSelectedList = []
   
        self.initTab1()
        self.initTab2()
        self.initTab3()




    def mainloop(self):
        self.window.mainloop()

    def buildNotebook(self):
        Notebook.setTabSytle()
        self.notebook = Notebook(self.window)
        self.notebook.addTab(self.window, tab1Viewport, tab1_name)
        self.notebook.addTab(self.window, tab2Viewport, tab2_name)
        self.notebook.addTab(self.window, tab3Viewport, tab3_name)

    def initTab1(self):
        optionFrame = OptionFrame(self, self.notebook.getFrame(tab1_name),
                                  Viewport(
                                      0,
                                      0,
                                      self.notebook.getFrame(tab1_name).viewport.right - 500,
                                      self.notebook.getFrame(tab1_name).viewport.height))
        optionFrame.place(x=optionFrame.viewport.left, y=optionFrame.viewport.top)

        self.infoFrame = SearchResultInfoFrame(self, self.notebook.getFrame(tab1_name),
                                               Viewport(
                                                   self.notebook.getFrame(tab1_name).viewport.right - 500,
                                                   0,
                                                   500,
                                                   self.notebook.getFrame(tab1_name).viewport.height))
        self.infoFrame.place(x=self.infoFrame.viewport.left, y=self.infoFrame.viewport.top)


    def initTab2(self):
        self.selectionInfoFrame = SelectionInfoFrame(self, self.notebook.getFrame(tab2_name),
                                                     Viewport(
                                                         0,
                                                         0,
                                                         500,
                                                         500))
        self.selectionInfoFrame.place(x=self.selectionInfoFrame.viewport.left, y=self.selectionInfoFrame.viewport.top)

        self.graphFrame = GraphFrame(self, self.notebook.getFrame(tab2_name),
                                     Viewport(
                                         500,
                                         0,
                                         300,
                                         500))
        self.graphFrame.place(x=self.graphFrame.viewport.left, y=self.graphFrame.viewport.top)

        self.gmailFrame = GmailAndXMLSaveLoadFrame(self, self.notebook.getFrame(tab2_name),
                                                   Viewport(
                                                       0,
                                                       500,
                                                       self.notebook.getFrame(tab2_name).viewport.width,
                                                       self.notebook.getFrame(tab2_name).viewport.height - 500
                                                   ))
        self.gmailFrame.place(x=self.gmailFrame.viewport.left, y=self.gmailFrame.viewport.top)


    def initTab3(self):
        self.settingFrmae = SettingFrmae(self, self.notebook.getFrame(tab3_name),
                                         Viewport(
                                         0,
                                         0,
                                         self.notebook.getFrame(tab3_name).viewport.width,
                                         self.notebook.getFrame(tab3_name).viewport.height
                                         ))
        self.settingFrmae.place(x=self.settingFrmae.viewport.left, y=self.settingFrmae.viewport.top)



    def reciveEvent(self, **events):
        # 미완
        for (event, eventData) in events.items():
            if event == "search":
                DOMReadingManager.initSearchOption()
                DOMReadingManager.setWithFormattedOptionList(eventData)
                dataes = DOMReadingManager.searchDataes()
                self.infoFrame.procSetData(dataes)

            elif event =="addDataSelected":
                self.selectionInfoFrame.procSetData(self.selectionInfoFrame.dataList + [eventData])
                self.graphFrame.updateGragh(self.selectionInfoFrame.dataList)

            elif event == "delDataFromSection":
                self.graphFrame.updateGragh(self.selectionInfoFrame.dataList)                         

            elif event =="isDataInSelectedList":
                return self.selectionInfoFrame.isDataInSelectedList(eventData)
            
            elif event =="getSelectionDataes":
                return self.selectionInfoFrame.dataList

            elif event == "setSelectionDataes":
                self.selectionInfoFrame.procSetData(eventData)
                self.graphFrame.updateGragh(self.selectionInfoFrame.dataList)

            elif event == "LogIn":
                return self.gmailFrame.logIn(*eventData)

            elif event == "getDataSelectedinSelection":
                return self.selectionInfoFrame.dataSelected, self.selectionInfoFrame.imgReadData


    def isDataInSelectedList(self, tag):
        for data in self.dataSelectedList:
            if data.tag == tag:
                return True
        return False
    
  
 #xml 저장 폴더가 존재하는 지 확인한다. 없으면 만든다.
if not os.path.isdir(XML_SAVE_DIR_NAME):
   os.mkdir(XML_SAVE_DIR_NAME)

logoLoading()
mainframe = MainFrame()
mainframe.mainloop()
