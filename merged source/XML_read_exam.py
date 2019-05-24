import UtilityDOM
from DataClass import DataSmallApartment
from DataClass import DataSmallApartment

import urllib.request
from xml.dom.minidom import parse, parseString

#연립 다세대
exam_small_apartment_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?" +\
    "serviceKey=e07l%2FJKjgBmbsW47T0yZchUXcgD2K7v9znyVX8WBKIPUkCpdHgMpxIk1nRksfUDBvFCtRk7A%2BH6KKbwYxVXfOQ%3D%3D" +\
    "&LAWD_CD=11110&DEAL_YMD=201812"

#단독/다가구
exam_single_detached_house = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?"+\
                             "serviceKey=IZ9s8c2tjO0gB4qkVdINj%2Bx0uW5AoM%2FmphJ42H4qz5Djt82Kdt45%2BUiVe9nP2XQCCBcKvvvS4XZo3%2BqIh6DJKg%3D%3D&LAWD_CD=11110&DEAL_YMD=201512"

url=exam_single_detached_house

data=urllib.request.urlopen(url).read()

list=parse(file=urllib.request.urlopen(url))

itemGroup = UtilityDOM.findNode(list, "response", "body", "items")

dataList = UtilityDOM.getListDataFromBaseNode(itemGroup, "item")
chosenDataLsit = UtilityDOM.getListDataFromBaseNode(itemGroup, "item", "건축년도", "NotFound")
print(1)






#네이버 도서검색에서 find 참고할것?

