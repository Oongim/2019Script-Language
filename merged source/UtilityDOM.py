

def findNode(domNode, *nodeNames):
    if len(nodeNames) == 0:
        return domNode

    for childNode in domNode.childNodes:
        if childNode.nodeName == nodeNames[0]:
            return findNode(childNode, *nodeNames[1:])

    return None


def getDataFromNode(domNode, *dataNames):
    if len(dataNames) == 0:
        condition = lambda nodeName: True
    else:
        condition = lambda nodeName: nodeName in dataNames

    data = {}
    for dataNode in domNode.childNodes:
        if condition(dataNode.nodeName):
            data[dataNode.nodeName] = dataNode.childNodes[0].nodeValue

    for dataName in dataNames:
        if dataName not in data.keys():
            data[dataName] = None

    return data


def getListDataFromBaseNode(domNode, childNodesName, *dataNames):
    dataList = []
    for elementNode in domNode.childNodes:
        if elementNode.nodeName == childNodesName:
            dataList.append(getDataFromNode(elementNode, *dataNames))

    return dataList
