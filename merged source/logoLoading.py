import tkinter
import ReadingDataFromXML

class logoLoading:

    def __init__(self,loadingData=True):

        self.opacity = 1
        self.window = tkinter.Tk()
        self.isLoading = False
        self.canvas = 0
        self.count = 0
        self.generator = ReadingDataFromXML.DOMReadingManager.readXML()

        self.isLoading=loadingData
        self.window.attributes('-alpha',self.opacity)
        self.window.image=tkinter.PhotoImage(file='Image/logo.png')
        tkinter.Label(self.window, image=self.window.image, bg='white').pack()
        self.canvas = tkinter.Canvas(self.window, bg="black", width=self.window.image.width(), height=20)
        self.canvas.pack()
        self.window.overrideredirect(True)
        self.window.geometry("+100+100")
        self.window.lift()
        self.window.wm_attributes("-topmost", True)
        self.window.wm_attributes("-transparentcolor", "white")
        self.opacity -= 0.01
        self.window.attributes('-alpha', self.opacity)
        self.myupdate()
        self.window.mainloop()

    def myupdate(self):
        if self.isLoading and self.opacity <= 0.98:
            date=str(next(self.generator))
            if date=="201812":
                self.isLoading=False
            self.IncreaseLoadingBar(date)

        elif self.opacity <= 0:
            self.window.destroy()
            return
        else:
            self.opacity -= 0.01
            self.window.attributes('-alpha', self.opacity)
        self.window.after(20, self.myupdate)


    def IncreaseLoadingBar(self,DataDate):
        self.count += 1
        self.canvas.delete("grim")
        self.canvas.create_rectangle(0,0,self.window.image.width()/12*self.count,20,fill='red',tag="grim")
        TempFont = tkinter.font.Font(self.window, size=15, weight='bold', family='Consolas')
        text=DataDate[:4]+"."+DataDate[4:]+". Data Complete"
        self.canvas.create_text(self.window.image.width()/2,10,font=TempFont,text=text,tag="grim",fill='yellow')
