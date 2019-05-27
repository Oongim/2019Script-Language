
##################################################################################################
#
# # 주소 한글로 검색해서 좌표 얻는 함수
import urllib
import http.client
from xml.etree import ElementTree

def Parsing_KAKAOMAP_Address(search_address):
    # 카카오 요청, 다른 예시는 https://developers.kakao.com/docs/restapi/local 참고
    server = "dapi.kakao.com"  # 서버
    headers = {'Authorization': 'KakaoAK cdb3b880191792500cb20af4a46a8edc'}  # 인증 키
    hangul_utf = urllib.parse.quote(search_address)
    url = "/v2/local/search/address.xml?query=%s" %hangul_utf # 좌표값 url str화
    conn = http.client.HTTPSConnection(server)  # 서버 연결
    conn.request("GET", url, None, headers)
    req = conn.getresponse()
    data = req.read()  # 데이터 저장
    tree = ElementTree.fromstring(data)  # ElementTree로 string화
    itemElements = tree.getiterator("documents")  # documents 이터레이터 생성

    result = []
    for item in itemElements:
        addr = []
        addr.append(item.find("y"))
        addr.append(item.find("x"))
        result.append((float(addr[1].text), float(addr[0].text)))
    return result


#################################################################################################

# #구글 지도 가져오기
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
from urllib.request import urlopen

def make_googlemap_url(center, zoom=16, maptype='roadmap'):
    key = 'AIzaSyA9gjC63ldBuHDwYM6flkFJDbTq6vQhFdg'
    point = str(center[1]) + ',' + str(center[0])
    size = (500, 500)

    url = "http://maps.google.com/maps/api/staticmap?"
    url += "center=%s&" % point
    url += "zoom=%i&" % zoom
    url += 'scale=1&'
    url += "size=" + str(size[0]) + 'x' + str(size[1]) + '&'
    url += 'maptype=' + maptype + '&'
    url += '&markers=color:red%7Clabel:C%7C' + point + '&'
    url += 'key=' + key

    return url

window=Tk()


print(Parsing_KAKAOMAP_Address("무악동63-9")[0])

map_url=make_googlemap_url(Parsing_KAKAOMAP_Address("무악동 63-9")[0])
with urlopen(map_url) as u:
    raw_data = u.read()
im = Image.open(BytesIO(raw_data))
map_image = ImageTk.PhotoImage(im)
Label(window, image=map_image, height=250, width=350, background='white').pack()

mainloop()

