from CustomTkClass import*


#Search프레임 관리
class Search:
    def __init__(self,window, width=300, height=300):
        self.width=width
        self.height=height
        window.geometry(str(self.width)+"x"+str(self.height))
        frame=OptionFrame(window,Viewport(0,0,width, height))
        window.mainloop()

#옵션의 프레임
class OptionFrame(Frame):
    def __init__(self,window,viewport):
        super(OptionFrame, self).__init__(window, viewport)
        width = viewport.width
        height = viewport.height
        heightRate=height/10
        minHeight=20
        minWidth=40

        self.optionList=[["검색 옵션"],
                         ["주택 종류",      "",      '',      tkinter.BooleanVar()  ,("test","test","test")],
                         ["동",            "",      '',      tkinter.BooleanVar()  ,("test","test","test")],
                         ["월세",         "최소",   '',       tkinter.BooleanVar()],
                         ["",            "최대",   '',       tkinter.BooleanVar()],
                         ["보증금",       "최소",   '',       tkinter.BooleanVar()],
                         ["",            "최대",   '',       tkinter.BooleanVar()],
                         ["건물 면적",    "최소",   '',       tkinter.BooleanVar()],
                         ["",            "최대",   '',       tkinter.BooleanVar()]
                         ]

        #처음 검색옵션만 예외로 위치 설정
        TempFont = tkinter.font.Font(window, size=20, weight='bold', family='Consolas')
        tkinter.Label(window, font=TempFont, text=self.optionList[0][0]).place(x=width/4/2 + 30, y=heightRate + minHeight, anchor="s")
        tkinter.Button(window, text="검색", command=self.Search).place(x=width-20, y=heightRate+13 ,anchor="se")
        for i in range(1,len(self.optionList)):
            #0번 인덱스가 있을 경우 옵션 이름 세팅
            if self.optionList[i][0]:
                tkinter.Label(window, text=self.optionList[i][0]).place(x=width/4/2, y=heightRate * (i + 1) + minHeight, anchor="s")
            # 1번 인덱스에 최소 최대 가 있을 경우 이름 세팅과 2번에 Entry세팅
            if self.optionList[i][1]:
                tkinter.Label(window, text=self.optionList[i][1]).place(x=width / 3, y=heightRate * (i + 1) + minHeight, anchor="s")
                self.optionList[i][2]=tkinter.Entry(window, width=int((width + 35 - width / 3 * 2) / 10), state='disabled')
            #1번 인덱스가 빌 경우 2번에 콤보박스 세팅
            else:
                self.optionList[i][2]=(tkinter.ttk.Combobox(window, width=int((width + 15 - width / 3 * 2) / 10), textvariable=str,state='disabled'))
                self.optionList[i][2]['value']=self.optionList[i][4]
            self.optionList[i][2].place(x=width-20, y=heightRate * (i + 1) + minHeight, anchor="se")
            #체크 박스 세팅
            self.optionList[i].append(tkinter.ttk.Checkbutton(window,variable= self.optionList[i][3], command=self.activeEntry).place(x=width / 2 ,
                                                                        y=heightRate * (i+1) + minHeight, anchor="s"))
    def Search(self):
        for i in range(1, len(self.optionList)):
            print(self.optionList[i][2].get())

    def activeEntry(self):
        for i in range(1, len(self.optionList)):
                if self.optionList[i][3].get()==True:
                    #콤보박스
                    if self.optionList[i][4]:
                        self.optionList[i][2]['state'] = 'readonly'
                    #엔트리
                    else:
                        self.optionList[i][2]['state'] = 'normal'
                else:
                    self.optionList[i][2]['state'] = 'disabled'





