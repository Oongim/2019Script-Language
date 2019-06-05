import UtilityDOM
from DataClass import DataSmallApartment
from DataClass import DataSingleDetachedHouse
from DataClass import formattedOptionToType

import os.path
import Error

import urllib.request
from xml.dom.minidom import parse

XML_SAVE_DIR_NAME = "XML_SAVE"
XML_SAVE_DIR_PATH = XML_SAVE_DIR_NAME+"\\"
SEP_DataesSmallApartment = "SA"
SEP_SingleDetachedHouse = "SDH"


def readNodesFromURL(url):
    s = urllib.request.urlopen(url)
    return parse(file=s)
    #return parse(file=urllib.request.urlopen(url))

def readNodesFromFile(filePath):
    return parse(filePath)

def getDictDataes(path, sep, LAWD_CD, DEAL_YMD, makeURL):
    filePath = path+sep+"_"+str(LAWD_CD)+"_"+str(DEAL_YMD)+".xml"

    if os.path.exists(filePath):
        XML_Dataes = readNodesFromFile(filePath)              
    else:
        XML_Dataes = readNodesFromURL(makeURL(LAWD_CD, DEAL_YMD))
        
        #XML에 저장
        file_handle = open(filePath, "w+", encoding='utf8')
        XML_Dataes.writexml(file_handle)
        file_handle.close()

    itemGroup = UtilityDOM.findNode(XML_Dataes, "response", "body", "items")
    return UtilityDOM.getListDataFromBaseNode(itemGroup, "item")


def getXMLDataesFromURLOpenAPI(LAWD_CD, DEAL_YMD, makeURL):
    url = makeURL(LAWD_CD, DEAL_YMD)
    return readNodesFromURL(url)


def getDataesSmallApartment(LAWD_CD, DEAL_YMD):
    makeSmallApartmentURL = lambda LAWD_CD, DEAL_YMD: "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?" + \
                          "serviceKey=e07l%2FJKjgBmbsW47T0yZchUXcgD2K7v9znyVX8WBKIPUkCpdHgMpxIk1nRksfUDBvFCtRk7A%2BH6KKbwYxVXfOQ%3D%3D" + \
                          "&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}".format(LAWD_CD=LAWD_CD, DEAL_YMD=DEAL_YMD)

    dataes = getDictDataes(XML_SAVE_DIR_PATH, SEP_DataesSmallApartment, LAWD_CD, DEAL_YMD, makeSmallApartmentURL)
    return [DataSmallApartment(data) for data in dataes]



def getDataesSingleDetachedHouse(LAWD_CD, DEAL_YMD):
    makeSingleDetachedHouseURL = lambda LAWD_CD, DEAL_YMD: "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?" + \
                             "serviceKey=IZ9s8c2tjO0gB4qkVdINj%2Bx0uW5AoM%2FmphJ42H4qz5Djt82Kdt45%2BUiVe9nP2XQCCBcKvvvS4XZo3%2BqIh6DJKg%3D%3D" + \
                             "&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}".format(LAWD_CD=LAWD_CD, DEAL_YMD=DEAL_YMD)

    dataes = getDictDataes(XML_SAVE_DIR_PATH, SEP_SingleDetachedHouse, LAWD_CD, DEAL_YMD, makeSingleDetachedHouseURL)
    return [DataSingleDetachedHouse(data) for data in dataes]



class ActivableValue:
    def __init__(self, bActivation, value):
        self.set(bActivation, value)

    def set(self, bActivation, value):
        self.activeSelf = bActivation
        self.value = value




CONST_HOUSE_TYPE_ALL = ""
CONST_HOUSE_TYPE_SMALL_APARTMENT = "연립 다세대"
CONST_HOUSE_TYPE_SINGLE_DETACHED_HOUSE = "단독 다가구"

class DOMReadingManager:
    LAWD_CD = 41390
    strYearsList = ["2018"]
    strMonthsList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]


    # strMonthsList = ["12"]
    houseType = ActivableValue(False, CONST_HOUSE_TYPE_ALL)
    addressDong = ActivableValue(False, "")
    minMonthlyRent = ActivableValue(False, 0)
    maxMonthlyRent = ActivableValue(False, 0)
    minDeposit = ActivableValue(False, 0)
    maxDeposit = ActivableValue(False, 0)
    minAreaSize = ActivableValue(False, 0)
    maxAreaSize = ActivableValue(False, 0)

    dataesSmallApartment = []
    dataesSingleDetachedHouse = []


    @staticmethod
    def initSearchOption():
        DOMReadingManager.houseType.set(False, CONST_HOUSE_TYPE_ALL)
        DOMReadingManager.addressDong.set(False, "")
        DOMReadingManager.minMonthlyRent.set(False, 0)
        DOMReadingManager.maxMonthlyRent.set(False, 0)
        DOMReadingManager.minDeposit.set(False, 0)
        DOMReadingManager.maxDeposit.set(False, 0)
        DOMReadingManager.minAreaSize.set(False, 0)
        DOMReadingManager.maxAreaSize.set(False, 0)


    @staticmethod
    def getDateList():
        return [int(year + strMonth) for year in DOMReadingManager.strYearsList for strMonth in
                     DOMReadingManager.strMonthsList]

    @staticmethod
    def getKeyPairForReading():
        for DEAL_YMD in DOMReadingManager.getDateList():
            yield [DOMReadingManager.LAWD_CD, DEAL_YMD]

    @staticmethod
    def readXML():
        # 법정동string으로부터 지번코드로 변경하는 처리를 추가해야한다.
        # 일단은 임시로 고정값을 설정해 둠.
        DOMReadingManager.dataesSmallApartment.clear()
        DOMReadingManager.dataesSingleDetachedHouse.clear()
       
        for keyPair in DOMReadingManager.getKeyPairForReading():
            DOMReadingManager.dataesSmallApartment \
                += getDataesSmallApartment(*keyPair)
            DOMReadingManager.dataesSingleDetachedHouse \
                += getDataesSingleDetachedHouse(*keyPair)
            print("LAWD_CD: {LAWD_CD}     DEAL_YMD: {DEAL_YMD}".format(LAWD_CD=keyPair[0], DEAL_YMD=keyPair[1]))
            yield keyPair[1]    # DEAL_YMDs


    @staticmethod
    def searchDataes():
        # 검색 함수 설정
        if DOMReadingManager.houseType.activeSelf:
            if DOMReadingManager.houseType.value == CONST_HOUSE_TYPE_ALL:
                readDstDataes = DOMReadingManager.dataesSmallApartment + DOMReadingManager.dataesSingleDetachedHouse
            elif DOMReadingManager.houseType.value == CONST_HOUSE_TYPE_SMALL_APARTMENT:
                readDstDataes = DOMReadingManager.dataesSmallApartment
            elif DOMReadingManager.houseType.value == CONST_HOUSE_TYPE_SINGLE_DETACHED_HOUSE:
                readDstDataes = DOMReadingManager.dataesSingleDetachedHouse
            else:
                raise Error.NotUsableValue()    #houseType should be usable value
        else:
            readDstDataes = DOMReadingManager.dataesSmallApartment + DOMReadingManager.dataesSingleDetachedHouse

        return [data for data in readDstDataes if DOMReadingManager.checkDataWithOption(data)]




    @staticmethod
    def checkDataWithOption(data):

        dong = formattedOptionToType(data.find("법정동"), str, " ")
        monthlyRent = formattedOptionToType(data.find("월세금액"), eval, ",", " ")
        deposit = formattedOptionToType(data.find("보증금액"), eval, ",", " ")
        areaSize = formattedOptionToType(data.find("면적"), eval, ",", " ")


        if DOMReadingManager.addressDong.activeSelf:
            if DOMReadingManager.addressDong.value != "":
                if dong != DOMReadingManager.addressDong.value:
                    return False

        if DOMReadingManager.minMonthlyRent.activeSelf:
            if monthlyRent < DOMReadingManager.minMonthlyRent.value:
                return False

        if DOMReadingManager.maxMonthlyRent.activeSelf:
            if monthlyRent > DOMReadingManager.maxMonthlyRent.value:
                return False

        if DOMReadingManager.minDeposit.activeSelf:
            if deposit < DOMReadingManager.minDeposit.value:
                return False

        if DOMReadingManager.maxDeposit.activeSelf:
            if deposit > DOMReadingManager.maxDeposit.value:
                return False

        if DOMReadingManager.minAreaSize.activeSelf:
            if areaSize < DOMReadingManager.minAreaSize.value:
                return False

        if DOMReadingManager.maxAreaSize.activeSelf:
            if areaSize > DOMReadingManager.maxAreaSize.value:
                return False

        return True


    @staticmethod
    def setWithFormattedOptionList(optionList):
        DOMReadingManager.setHouseType(*optionList[0])
        DOMReadingManager.setAddressDong(*optionList[1])
        DOMReadingManager.setMinMonthlyRent(*optionList[2])
        DOMReadingManager.setMaxMonthlyRent(*optionList[3])
        DOMReadingManager.setMinDeposit(*optionList[4])
        DOMReadingManager.setMaxDeposit(*optionList[5])
        DOMReadingManager.setMinAreaSize(*optionList[6])
        DOMReadingManager.setMaxAreaSize(*optionList[7])


    @staticmethod
    def setHouseType(bActivation, houseType = CONST_HOUSE_TYPE_ALL):
        if bActivation:
            if not (houseType == CONST_HOUSE_TYPE_SMALL_APARTMENT
                    or houseType == CONST_HOUSE_TYPE_SINGLE_DETACHED_HOUSE
                    or houseType == CONST_HOUSE_TYPE_ALL):
                raise Error.NotUsableValue()
        DOMReadingManager.houseType.set(bActivation, houseType)


    @staticmethod
    def setAddressDong(bActivation, dong=""):
        DOMReadingManager.addressDong.set(bActivation, dong)


    @staticmethod
    def setMinMonthlyRent(bActivation, rent='0'):
        DOMReadingManager.minMonthlyRent.set(bActivation, int(rent))


    @staticmethod
    def setMaxMonthlyRent(bActivation, rent='0'):
        DOMReadingManager.maxMonthlyRent.set(bActivation, int(rent))


    @staticmethod
    def setMinDeposit(bActivation, deposit='0'):
        DOMReadingManager.minDeposit.set(bActivation, int(deposit))


    @staticmethod
    def setMaxDeposit(bActivation, deposit='0'):
        DOMReadingManager.maxDeposit.set(bActivation, int(deposit))


    @staticmethod
    def setMinAreaSize(bActivation, areaSize='0'):
        DOMReadingManager.minAreaSize.set(bActivation, int(areaSize))


    @staticmethod
    def setMaxAreaSize(bActivation, areaSize='0'):
        DOMReadingManager.maxAreaSize.set(bActivation, int(areaSize))























