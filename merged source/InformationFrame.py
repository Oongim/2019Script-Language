from CustomTkClass import*
from DataClass import formattedOptionToType
from GoogleMap import Parsing_KAKAOMAP_Address
from GoogleMap import make_googlemap_url
import urllib.request
import PIL.Image
import PIL.ImageTk
import io

class InformationFrame(Frame):
    listboxHeightRatio = 0.4
    infoSectionHeightRatio = 0.5
    infoWidthRatio = 0.5
    # sb : selectButton
    sbWidthRatio = 0.1
    sbHeightRatio = 0.2

    def __init__(self, mainframe, window, viewport):
        super(InformationFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
        self.dataList = []
        self.dataSelected = None
        self.mapImage = None

        # UI 생성
        self.createListbox()
        self.createInfoSection()
        self.createMap()
        self.dictDataFromListboxIndex = {}



    def createListbox(self):
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
        self.listbox.bind('<Double-Button-1>', self.selectSectionOfListbox)
        #self.listbox.bind('<<ListboxSelect>>', self.selectSectionOfListbox)


    def createInfoSection(self):
        vpInfoFrame = Viewport(
            0,
            0 + self.viewport.height * InformationFrame.listboxHeightRatio,
            self.viewport.width * InformationFrame.infoWidthRatio,
            self.viewport.height * InformationFrame.infoSectionHeightRatio
        )
        vpInfoFrame.makeElementToInt()

        self.InfoLabels = InfoLabels(self, vpInfoFrame)


    def createMap(self):
        vpMapFrame = Viewport(
            0 + self.viewport.width * InformationFrame.infoWidthRatio,
            0 + self.viewport.height * InformationFrame.listboxHeightRatio,
            self.viewport.width * (1 - InformationFrame.infoWidthRatio),
            self.viewport.height * (1 - InformationFrame.listboxHeightRatio)
        )
        vpMapFrame.makeElementToInt()

        self.map = tkinter.Label(self,  width=vpMapFrame.width, height=vpMapFrame.height, bg="white", image=self.mapImage)
        self.map.place(x=vpMapFrame.left, y=vpMapFrame.top, anchor="nw")



    def procSetData(self, dataList):
        self.setDataList(dataList)
        self.updateListbox()
        self.dataSelected = None
        self.initSelectedInfo()
        self.updateSelectedMap()

    def setDataList(self, dataList):
        self.dataList = dataList


    def updateListbox(self):
        vpListbox = Viewport(
            0,
            0,
            self.viewport.width,
            self.viewport.height * InformationFrame.listboxHeightRatio
        )
        vpListbox.makeElementToInt()
        self.listbox.delete(0, tkinter.END)
        index = 0
        for data in self.dataList:
            self.dictDataFromListboxIndex[index] = data
            index += 1
            dataString = "동 : {동}   월세 : {월세}만원   보증금 : {보증금}만원   면적 : {면적}m2".format(
                   동=data.find("법정동"), 월세=data.find("월세금액"), 보증금=data.find("보증금액"), 면적=data.find("면적"))
            self.listbox.insert(index, dataString)



    def selectSectionOfListbox(self, eventInfo):
        if len(self.listbox.curselection()) > 0:
            index = int(self.listbox.curselection()[0])
            self.dataSelected = self.dictDataFromListboxIndex[index]
            self.updateSelectedInfo(self.dataSelected)
            self.updateSelectedMap()


    def initSelectedInfo(self):
        self.InfoLabels.buildYear.setTextDataLabel("")
        self.InfoLabels.tradeDate.setTextDataLabel("")
        self.InfoLabels.dong.setTextDataLabel("")
        self.InfoLabels.deposit.setTextDataLabel("")
        self.InfoLabels.monthlyRent.setTextDataLabel("")
        self.InfoLabels.areaSize.setTextDataLabel("")


    def updateSelectedInfo(self, data):
        strDong = formattedOptionToType(data.find("법정동"), str, " ")
        strMonthlyRent = formattedOptionToType(data.find("월세금액"), str, ",", " ")
        strDeposit = formattedOptionToType(data.find("보증금액"), str, ",", " ")
        strAreaSize = formattedOptionToType(data.find("면적"), str, ",", " ")

        self.InfoLabels.buildYear.setTextDataLabel(data.find("건축년도"))
        self.InfoLabels.tradeDate.setTextDataLabel(data.find("년")+"/"+data.find("월")+"/"+data.find("일"))
        self.InfoLabels.dong.setTextDataLabel(strDong)
        self.InfoLabels.deposit.setTextDataLabel(strDeposit)
        self.InfoLabels.monthlyRent.setTextDataLabel(strMonthlyRent)
        self.InfoLabels.areaSize.setTextDataLabel(strAreaSize)


    def updateSelectedMap(self):
        try:
            strAdress = self.dataSelected.data["법정동"] + self.dataSelected.data["지번"]
            map_url = make_googlemap_url(Parsing_KAKAOMAP_Address(strAdress)[0])
            with urllib.request.urlopen(map_url) as uFile:
                rawData = uFile.read()
            rawImage = PIL.Image.open(io.BytesIO(rawData))
            self.mapImage = PIL.ImageTk.PhotoImage(rawImage)
            self.map["image"] = self.mapImage
        except:
            self.mapImage = None
            self.map["image"] = self.mapImage




class SearchResultInfoFrame(InformationFrame):
    def __init__(self, mainframe, window, viewport):
        super(SearchResultInfoFrame, self).__init__(mainframe, window, viewport)
        self.createSelectButton()


    def createSelectButton(self):
        vpSectionButton = Viewport(0, 0, 0, 0)
        vpSectionButton.right = 0 + self.viewport.width * InformationFrame.infoWidthRatio
        vpSectionButton.bottom = 0 + self.viewport.height

        self.selectButton = tkinter.Button(self, text="찜 하기",
                                           command=lambda: self.addDataToSelectedList())
        self.selectButton.place(x=vpSectionButton.right, y=vpSectionButton.bottom, anchor="se")
        self.updateSelectButtonState()


    def procSetData(self, dataList):
        super().procSetData(dataList)
        self.updateSelectButtonState()


    def selectSectionOfListbox(self, eventInfo):
        super().selectSectionOfListbox(eventInfo)
        self.updateSelectButtonState()


    def updateSelectButtonState(self):
        if self.dataSelected is not None:
            if not self.mainframe.reciveEvent(isDataInSelectedList=self.dataSelected):
                self.selectButton['state'] = "normal"
                return
        self.selectButton['state'] = 'disabled'


    def addDataToSelectedList(self):
        self.mainframe.reciveEvent(addDataSelected=self.dataSelected)
        self.updateSelectButtonState()



class SelectionInfoFrame(InformationFrame):
    def __init__(self, mainframe, window, viewport):
        super(SelectionInfoFrame, self).__init__(mainframe, window, viewport)
        self.createSelectButton()


    def createSelectButton(self):
        vpSectionButton = Viewport(0, 0, 0, 0)
        vpSectionButton.right = 0 + self.viewport.width * InformationFrame.infoWidthRatio
        vpSectionButton.bottom = 0 + self.viewport.height

        self.selectButton = tkinter.Button(self, text="목록에서 삭제",
                                           command=lambda: self.deleteDataFromSelectedList())
        self.selectButton.place(x=vpSectionButton.right, y=vpSectionButton.bottom, anchor="se")
        self.updateSelectButtonState()


    def procSetData(self, dataList):
        super().procSetData(dataList)
        self.updateSelectButtonState()


    def selectSectionOfListbox(self, eventInfo):
        super().selectSectionOfListbox(eventInfo)
        self.updateSelectButtonState()


    def updateSelectButtonState(self):
        if self.dataSelected is not None:
            self.selectButton['state'] = "normal"
            return
        self.selectButton['state'] = 'disabled'


    def deleteDataFromSelectedList(self):
        self.dataList.remove(self.dataSelected)
        self.procSetData(self.dataList)
        # self.dataSelected는 procSetData()에서 None으로 처리된다.


    def isDataInSelectedList(self, data):
        return data in self.dataList






class InfoLabels:
    def __init__(self, window, viewport,
                 padRatiosBetweenEachLabel = 0.03, kindLabelWidth=12, dataLabelWidth=16):
        self.window = window
        self.viewport = viewport
        self.numAttribute = 6

        heightEachLabelWithPad = viewport.height // 6
        heightEachLabel = int(heightEachLabelWithPad - viewport.height * padRatiosBetweenEachLabel)
        vpLabel = Viewport(viewport.left, viewport.top, viewport.width, heightEachLabel)

        vpBuildYear = Viewport(vpLabel.left, vpLabel.top, vpLabel.width, vpLabel.height)
        self.buildYear = DescLabel(window, vpBuildYear, "건축년도", "", kindLabelWidth, dataLabelWidth)

        vpTradeDate = Viewport(vpBuildYear.left, vpBuildYear.top + heightEachLabelWithPad, vpBuildYear.width, vpBuildYear.height)
        self.tradeDate = DescLabel(window, vpTradeDate, "거래일자", "", kindLabelWidth, dataLabelWidth)

        vpDongDate = Viewport(vpTradeDate.left, vpTradeDate.top + heightEachLabelWithPad, vpTradeDate.width, vpTradeDate.height)
        self.dong = DescLabel(window, vpDongDate, "법정동", "", kindLabelWidth, dataLabelWidth)

        vpDeposit = Viewport(vpDongDate.left, vpDongDate.top + heightEachLabelWithPad, vpDongDate.width, vpDongDate.height)
        self.deposit = DescLabel(window, vpDeposit, "보증금액", "", kindLabelWidth, dataLabelWidth)

        vpMonthlyRent = Viewport(vpDeposit.left, vpDeposit.top + heightEachLabelWithPad, vpDeposit.width, vpDeposit.height)
        self.monthlyRent = DescLabel(window, vpMonthlyRent, "월세금액", "", kindLabelWidth, dataLabelWidth)

        vpAreaSize = Viewport(vpMonthlyRent.left, vpMonthlyRent.top + heightEachLabelWithPad, vpMonthlyRent.width, vpMonthlyRent.height)
        self.areaSize = DescLabel(window, vpAreaSize, "면적", "", kindLabelWidth, dataLabelWidth)


# 건축년도, 년, 법정동, 보증금액, 월, 월세금액, 일, 지역코드

# 연립 다세대 only  :  연립다세대, 전용면적, 지번, 층


















