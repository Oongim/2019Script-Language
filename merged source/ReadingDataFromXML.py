import UtilityDOM
from DataClass import DataSmallApartment
from DataClass import DataSingleDetachedHouse

import Error

import urllib.request
from xml.dom.minidom import parse


def readNodesFromURL(url):
    return parse(file=urllib.request.urlopen(url))

def getDictDataesFromURLOpenAPI(url):
    rootNode = readNodesFromURL(url)
    itemGroup = UtilityDOM.findNode(rootNode, "response", "body", "items")
    return UtilityDOM.getListDataFromBaseNode(itemGroup, "item")


def getDataesSmallApartment(LAWD_CD, DEAL_YMD):
    smallApartmentURL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?" + \
                          "serviceKey=e07l%2FJKjgBmbsW47T0yZchUXcgD2K7v9znyVX8WBKIPUkCpdHgMpxIk1nRksfUDBvFCtRk7A%2BH6KKbwYxVXfOQ%3D%3D" + \
                          "&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}".format(LAWD_CD=LAWD_CD, DEAL_YMD=DEAL_YMD)

    dataes = getDictDataesFromURLOpenAPI(smallApartmentURL)
    return [DataSmallApartment(**data) for data in dataes]


def getDataesSingleDetachedHouse(LAWD_CD, DEAL_YMD):
    singleDetachedHouseURL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?" + \
                          "serviceKey=e07l%2FJKjgBmbsW47T0yZchUXcgD2K7v9znyVX8WBKIPUkCpdHgMpxIk1nRksfUDBvFCtRk7A%2BH6KKbwYxVXfOQ%3D%3D" + \
                          "&LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}".format(LAWD_CD=LAWD_CD, DEAL_YMD=DEAL_YMD)

    dataes = getDictDataesFromURLOpenAPI(singleDetachedHouseURL)
    return [DataSingleDetachedHouse(**data) for data in dataes]



class ActivableValue:
    def __init__(self, bActivation, value):
        self.set(bActivation, value)

    def set(self, bActivation, value):
        self.activeSelf = bActivation
        self.value = value




CONST_HOUSE_TYPE_ALL = ""
CONST_HOUSE_TYPE_SMALL_APARTMENT = "단독 다가구"
CONST_HOUSE_TYPE_SINGLE_DETACHED_HOUSE = "연립 다세대"

class DOMReadingManager:
    houseType = ActivableValue(False, CONST_HOUSE_TYPE_ALL)
    addressDong = ActivableValue(False, "")
    minMonthlyRent = ActivableValue(False, 0)
    maxMonthlyRent = ActivableValue(False, 0)
    minDeposit = ActivableValue(False, 0)
    maxDeposit = ActivableValue(False, 0)
    minAreaSize = ActivableValue(False, 0)
    maxAreaSize = ActivableValue(False, 0)


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
    def readXML():
        
        # 검색 함수 설정
        if DOMReadingManager.houseType.activeSelf:
            if DOMReadingManager.houseType == CONST_HOUSE_TYPE_ALL:
                readFunctions = [getDataesSmallApartment, getDataesSingleDetachedHouse]
            elif DOMReadingManager.houseType == CONST_HOUSE_TYPE_SMALL_APARTMENT:
                readFunctions = [getDataesSmallApartment]
            elif DOMReadingManager.houseType == CONST_HOUSE_TYPE_SINGLE_DETACHED_HOUSE:
                readFunctions = [getDataesSingleDetachedHouse]
            else:
                raise Error.NotUsableValue()    #houseType should be usable value
        else:
            readFunctions = [getDataesSmallApartment, getDataesSingleDetachedHouse]

        # 법정동string으로부터 지번코드로 변경하는 처리를 추가해야한다.
        # 일단은 임시로 고정값을 설정해 둠.
        strMonths = ["01", "02", "03", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        LAWD_CD = 41390     # 시흥시
        DEAL_YMDs = [int(str(year)+strMonth) for year in range(2018, 2018+1) for strMonth in strMonths]

        notRemoveDataes = []
        resultDataes = []
        for readFunc in readFunctions:
            for DEAL_YMD in DEAL_YMDs:
                dataes = readFunc(LAWD_CD, DEAL_YMD)
                notRemoveDataes += dataes
                #조건에 맞지 않는 data는 삭제
                index = 0
                while index < len(dataes):
                    if not DOMReadingManager.checkDataWithOption(dataes[index]):
                        dataes.remove(dataes[index])
                    else:
                        index += 1
                resultDataes += dataes

        resultDataes.sort(key=lambda data:data.find("월세금액"))
        return resultDataes



    @staticmethod
    def checkDataWithOption(data):
        if DOMReadingManager.addressDong.activeSelf:
            if DOMReadingManager.addressDong.value != "":
                if data.find("법정동") != DOMReadingManager.addressDong.value:
                    return False

        if DOMReadingManager.minMonthlyRent.activeSelf:
            if int(data.find("월세금액")) < DOMReadingManager.minMonthlyRent.value:
                return False

        if DOMReadingManager.maxMonthlyRent.activeSelf:
            if int(data.find("월세금액")) > DOMReadingManager.maxMonthlyRent.value:
                return False

        if DOMReadingManager.minDeposit.activeSelf:
            if int(data.find("보증금")) < DOMReadingManager.minDeposit.value:
                return False

        if DOMReadingManager.maxDeposit.activeSelf:
            if int(data.find("보증금")) > DOMReadingManager.maxDeposit.value:
                return False

        if DOMReadingManager.minAreaSize.activeSelf:
            if int(data.find("면적")) < DOMReadingManager.minAreaSize.value:
                return False

        if DOMReadingManager.maxAreaSize.activeSelf:
            if int(data.find("면적")) > DOMReadingManager.maxAreaSize.value:
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
        DOMReadingManager.minAreaSize.set(bActivation, int(areaSize))























