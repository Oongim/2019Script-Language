from CustomTkClass import*
from DataClass import formattedOptionToType
import random
MONTHLYRENT, DEPOSIT,AREASIZE =range(3)

class GraphFrame(Frame):
    def __init__(self, mainframe, window,viewport):
        super(GraphFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
        self.width = viewport.width
        self.height = viewport.height
        self.count=0
        self.sampleNumList=[[x for x in range(20)],random.sample([x for x in range(1,100)],24),[x for x in range(30)]]
        optionheight=self.height/5
        self.optionvalue=tkinter.IntVar()
        TempFont = tkinter.font.Font(self, size=20, weight='bold', family='Consolas')

        tkinter.Label(self, font=TempFont, text="그래프 옵션").place(x=viewport.width/2,y=20,anchor="center")
        self.radiobutton=[]
        self.radiobutton.append(tkinter.Radiobutton(self,text="월세",variable=self.optionvalue,value=MONTHLYRENT,command=self.update,state='normal'))
        self.radiobutton.append(tkinter.Radiobutton(self,text="보증금",variable=self.optionvalue,value=DEPOSIT,command=self.update))
        self.radiobutton.append(tkinter.Radiobutton(self,text="건물면적",variable=self.optionvalue,value=AREASIZE,command=self.update))

        self.radiobutton[0].place(x=self.width / 2 - self.width / 4, y=optionheight, anchor='center')
        self.radiobutton[1].place(x=self.width / 2, y=optionheight, anchor='center')
        self.radiobutton[2].place(x=self.width / 2 + self.width / 4, y=optionheight, anchor='center')

        self.canvasHeight=self.height/4*3
        self.canvas=tkinter.Canvas(self, bg="white", width=self.width, height=self.height/4*3)
        self.canvas.place(x=0,y=self.height/4)


    def drawGraph(self):
        self.canvas.delete("grim")
        dataNum = len(self.sampleNumList[self.optionvalue.get()])
        maxHeight=max(self.sampleNumList[self.optionvalue.get()])
        minHeight=min(self.sampleNumList[self.optionvalue.get()])

        if maxHeight is 0:
            maxHeight=1
            self.count=102
        for i in range(dataNum):
            if maxHeight is self.sampleNumList[self.optionvalue.get()][i]:
                color="red"
            elif minHeight is self.sampleNumList[self.optionvalue.get()][i]:
                color='blue'
            else:
                color="black"
            minHeightRate=min(int(self.sampleNumList[self.optionvalue.get()][i]/100*(self.count)),self.sampleNumList[self.optionvalue.get()][i])
            self.canvas.create_rectangle(i * (self.width - 10) / dataNum + 7,
                                         (maxHeight - minHeightRate) * (self.canvasHeight - 36) / maxHeight+15,
                                         (i + 1) * (self.width - 10) / dataNum + 5, self.canvasHeight - 20,
                                         fill=color, tag="grim",activefill='yellow')

            self.canvas.create_text(i * (self.width - 10) / dataNum + (self.width - 10) / dataNum / 2 + 6,
                                    (maxHeight - minHeightRate) * (self.canvasHeight - 36) / maxHeight + 7,
                                    text=minHeightRate, tags="grim")
            self.canvas.create_text(i * (self.width - 10) / dataNum + (self.width - 10) / dataNum / 2 + 6,
                                    (self.canvasHeight - 10),
                                    text=i, tags="grim")


    def updateGragh(self, dataes):
        # 선택목록의 데이터들에서 삭제 혹은 추가가 일어날 때, 호출된다.
        # 이 함수에서는 그래프를 새로 그려야 한다.
        # 업데이트된 새로운 데이터 리스트는 인자로 받는 dates 이다.
        self.findstr=['월세금액','보증금액','전용면적']
        for i in range(3):
            self.sampleNumList[i].clear()
        for data in dataes:
            for i in range(3):
                value = data.find(self.findstr[i])
                if self.findstr[i] == "보증금액":
                    value = formattedOptionToType(value, str, ",")
                elif value is None:
                    value = formattedOptionToType(data.find("계약면적"), str, ",")
                self.sampleNumList[i].append(eval(value))

    def update(self):
        if self.count>101:
            for radio in self.radiobutton:
                radio['state']='active'
            self.count=0
            return
        if self.count==0:
            for radio in self.radiobutton:
                radio['state']='disabled'

        self.count+=1
        self.drawGraph()
        self.window.after(10, self.update)
