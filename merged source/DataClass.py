
class DataInterface:
    initNumTag = 0
    def __init__(self, data):
        self.data = data
        self.tag = DataInterface.initNumTag
        DataInterface.initNumTag += 1

    def findWithOriginKey(self, originKey):
        if originKey in self.data.keys():
            return self.data[originKey]
        else:
            return None


# 연립 다세대
class DataSmallApartment(DataInterface):
    def __init__(self, data):
        super(DataSmallApartment, self).__init__(data)

    def find(self, key):
        if key == "면적":
            searchKey = "전용면적"
        else:
            searchKey = key

        return self.findWithOriginKey(searchKey)


# 단독 다가구
class DataSingleDetachedHouse(DataInterface):
    def __init__(self, data):
        super(DataSingleDetachedHouse, self).__init__(data)

    def find(self, key):
        if key == "면적":
            searchKey = "계약면적"
        else:
            searchKey = key

        return self.findWithOriginKey(searchKey)


def formattedOptionToType(strOption, type, *removeChars):
    for char in removeChars:
        strOption = strOption.replace(char, "")
    return type(strOption)


# 연립 다세대
# <건축년도>2002</건축년도>
# <년>2015</년>
# <법정동> 청운동</법정동>
# <보증금액> 45,000</보증금액>
# <연립다세대>아트빌</연립다세대>
# <월>12</월>
# <월세금액> 0</월세금액>
# <일>1~10</일>
# <전용면적>84.73</전용면적>
# <지번>89-5</지번>
# <지역코드>11110</지역코드>
# <층>1</층>
# 건축년도, 년, 법정동, 보증금액, 연립다세대, 월, 월세금액, 일, 전용면적, 지번, 지역코드, 층
#
# 단독 다가구
# <건축년도>1991</건축년도>
# <계약면적>53.76</계약면적>
# <년>2015</년>
# <법정동> 청운동</법정동>
# <보증금액> 25,000</보증금액>
# <월>12</월>
# <월세금액> 0</월세금액>
# <일>11~20</일>
# <지역코드>11110</지역코드>
# 건축년도, 계약면적, 년, 법정동, 보증금액, 월, 월세금액, 일, 지역코드

# 건축년도, 년, 법정동, 보증금액, 월, 월세금액, 일, 지역코드

# 연립 다세대 only  :  연립다세대, 전용면적, 지번, 층
# 단독 다가구 only  :  계약면적