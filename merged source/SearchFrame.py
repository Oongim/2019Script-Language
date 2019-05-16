import tkinter
from tkinter import ttk
from tkinter import font

class OptionFrame(tkinter.Frame):
    def __init__(self,window,width,height):
        super(OptionFrame, self).__init__(window)
        heightRate=height/10
        minHeight=20
        minWidth=40
        i = 1
        TempFont = tkinter.font.Font(window, size=20, weight='bold', family='Consolas')
        tkinter.Label(window,font=TempFont ,text="검색 옵션").place(x=minWidth+30, y=heightRate*i+minHeight, anchor="s")
        tkinter.Button(window,text="검색",command=self.Search).place(x=width/4,y=heightRate-13)
        i += 1
        tkinter.Label(window,  text="주택 종류").place(x=minWidth, y=heightRate*i+minHeight, anchor="s")
        self.isKindCheck = tkinter.BooleanVar()
        tkinter.ttk.Checkbutton(window, command=self.activeEntry,variable=self.isKindCheck).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.kindCombo=ttk.Combobox(window,width=int((width/4+15-width/4/3*2)/10),textvariable=str)
        self.kindCombo['value']=('test','test','test')
        self.kindCombo.place(x=width/4+35, y=heightRate*i+minHeight, anchor="se")
        i += 1
        tkinter.Label(window,  text="동").place(x=minWidth, y=heightRate*i+minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.positionCombo = ttk.Combobox(window, width=int((width / 4 + 15 - width / 4 / 3 * 2) / 10), textvariable=str,state='disabled')
        self.positionCombo['value'] = ('test', 'test', 'test')
        self.positionCombo.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")
        i += 1
        tkinter.Label(window,  text="월세").place(x=minWidth, y=heightRate*i+minHeight, anchor="s")
        tkinter.Label(window,  text="최소").place(x=width/4/2, y=heightRate*i+minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.monthPayMinE=tkinter.Entry(window,width=int((width/4+35-width/4/3*2)/10),state='disabled')
        self.monthPayMinE.place(x=width/4+35, y=heightRate*i+minHeight, anchor="se")
        i += 1
        tkinter.Label(window, text="최대").place(x=width / 4 / 2, y=heightRate * i + minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.monthPayMaxE = tkinter.Entry(window, width=int((width / 4 + 35 - width / 4 / 3 * 2) / 10),state='disabled')
        self.monthPayMaxE.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")
        i += 1
        tkinter.Label(window,  text="보증금").place(x=minWidth, y=heightRate*i+minHeight, anchor="s")
        tkinter.Label(window, text="최소").place(x=width / 4 / 2, y=heightRate * i + minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.depositMinE = tkinter.Entry(window, width=int((width / 4 + 35 - width / 4 / 3 * 2) / 10),state='disabled')
        self.depositMinE.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")
        i += 1
        tkinter.Label(window, text="최대").place(x=width / 4 / 2, y=heightRate * i + minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.depositMaxE = tkinter.Entry(window, width=int((width / 4 + 35 - width / 4 / 3 * 2) / 10),state='disabled')
        self.depositMaxE.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")
        i += 1
        tkinter.Label(window,  text="건물 면적").place(x=minWidth, y=heightRate*i+minHeight, anchor="s")
        tkinter.Label(window, text="최소").place(x=width / 4 / 2, y=heightRate * i + minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.areaMinE = tkinter.Entry(window, width=int((width / 4 + 35 - width / 4 / 3 * 2) / 10),state='disabled')
        self.areaMinE.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")
        i += 1
        tkinter.Label(window, text="최대").place(x=width / 4 / 2, y=heightRate * i + minHeight, anchor="s")
        tkinter.ttk.Checkbutton(window, command=self.activeEntry).place(x=width / 4 / 3 * 2,
                                                                        y=heightRate * i + minHeight, anchor="s")
        self.areaMaxE = tkinter.Entry(window, width=int((width / 4 + 35 - width / 4 / 3 * 2) / 10),state='disabled')
        self.areaMaxE.place(x=width / 4 + 35, y=heightRate * i + minHeight, anchor="se")


    def Search(self):
        pass
    def activeEntry(self):
        if self.isKindCheck.get()==1:
            self.kindCombo['state']='active'
        else:
            self.kindCombo['state'] = 'active'


class Search:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        window = tkinter.Tk()
        window.geometry(str(self.width)+"x"+str(self.height))
        frame=OptionFrame(window,width,height)

        window.mainloop()




