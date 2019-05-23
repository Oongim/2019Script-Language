import UtilityDOM

import urllib.request
from xml.dom.minidom import parse, parseString
url="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?" +\
    "serviceKey=e07l%2FJKjgBmbsW47T0yZchUXcgD2K7v9znyVX8WBKIPUkCpdHgMpxIk1nRksfUDBvFCtRk7A%2BH6KKbwYxVXfOQ%3D%3D" +\
    "&LAWD_CD=11110&DEAL_YMD=201812"

data=urllib.request.urlopen(url).read()

list=parse(file=urllib.request.urlopen(url))

itemGroup = UtilityDOM.findNode(list, "response", "body", "items")

dataList = UtilityDOM.getListDataFromBaseNode(itemGroup, "item")
chosenDataLsit = UtilityDOM.getListDataFromBaseNode(itemGroup, "item", "건축년도", "NotFound")
print(1)


#네이버 도서검색에서 find 참고할것?