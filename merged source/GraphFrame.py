from CustomTkClass import*
import random
MONTHLYRENT, DEPOSIT,AREASIZE =range(3)

class GraphFrame(Frame):
    def __init__(self, mainframe, window,viewport):
        super(GraphFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
        self.width = viewport.width
        self.height = viewport.height

        self.sampleNumList=[[x for x in range(20)],random.sample([x for x in range(1,25)],24),[x for x in range(30)]]
        optionheight=self.height/5
        self.optionvalue=tkinter.IntVar()
        TempFont = tkinter.font.Font(self, size=20, weight='bold', family='Consolas')

        tkinter.Label(self, font=TempFont, text="그래프 옵션").place(x=viewport.width/2,y=20,anchor="center")
        tkinter.Radiobutton(self,text="월세",variable=self.optionvalue,value=MONTHLYRENT,command=self.drawGraph,state='normal').place(x=self.width/2-self.width/4,y=optionheight,anchor='center')
        tkinter.Radiobutton(self,text="보증금",variable=self.optionvalue,value=DEPOSIT,command=self.drawGraph).place(x=self.width/2,y=optionheight,anchor='center')
        tkinter.Radiobutton(self,text="건물면적",variable=self.optionvalue,value=AREASIZE,command=self.drawGraph).place(x=self.width/2+self.width/4,y=optionheight,anchor='center')
        self.canvasHeight=self.height/4*3
        self.canvas=tkinter.Canvas(self, bg="white", width=self.width, height=self.height/4*3)
        self.canvas.place(x=0,y=self.height/4)

    def drawGraph(self):
        self.canvas.delete("grim")
        dataNum=len(self.sampleNumList[self.optionvalue.get()])
        for i in range(dataNum):
            self.canvas.create_rectangle(i * (self.width - 10) / dataNum + 5,
                                        (dataNum - self.sampleNumList[self.optionvalue.get()][i]) * (self.canvasHeight - 10) / dataNum + 10,
                                        (i + 1) * (self.width - 10) / dataNum + 5, self.canvasHeight, fill='black',tag="grim")

            self.canvas.create_text(i * (self.width - 10) / dataNum + (self.width - 10) / dataNum / 2 + 5,
                                    (dataNum - self.sampleNumList[self.optionvalue.get()][i]) * (self.canvasHeight - 10) / dataNum - (
                                            self.canvasHeight - 10) / dataNum / 2 + 10, text=(self.sampleNumList[self.optionvalue.get()][i]),tags="grim")



    def updateGragh(self, dataes):
        # 선택목록의 데이터들에서 삭제 혹은 추가가 일어날 때, 호출된다.
        # 이 함수에서는 그래프를 새로 그려야 한다.
        # 업데이트된 새로운 데이터 리스트는 인자로 받는 dates 이다.
        pass


