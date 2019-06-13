import tkinter
from CustomTkClass import Viewport
from CustomTkClass import Window
from CustomTkClass import Frame


class SettingFrmae(Frame):
    def __init__(self, mainframe, window, viewport):
        super(SettingFrmae, self).__init__(window, viewport)
        self.mainframe = mainframe

        self.createSettingEmailSenderButton()


    def createSettingEmailSenderButton(self):
        self.settingEmailSenderButton = tkinter.Button(self, text="Email Sender Setting",
                                                       command=self.setSettingEmailSender)
        self.vpSettingEmailSenderButton = Viewport(100, 50, 0, 0)
        self.settingEmailSenderButton.place(
            x=self.vpSettingEmailSenderButton.left, y=self.vpSettingEmailSenderButton.top, anchor="center")


    def setSettingEmailSender(self):
        emailSenderWindow = SettingEmailSenderWindow(self,
                                                     self.mainframe.window.viewport.left+100,
                                                     self.mainframe.window.viewport.top+100)
        emailSenderWindow.mainloop()


    def setID_PW(self, id, pw):
        self.mainframe.reciveEvent(setID_PW=(id, pw))
        
  



class SettingEmailSenderWindow(Window):
    def __init__(self, mainframe, left=200, top=200, width=400, height=200):
        super(SettingEmailSenderWindow, self).__init__(left, top, width, height)
        self.mainframe = mainframe
        self.id = ""
        self.pw = ""

        entryLeft = width//10

        self.idLabel = tkinter.Label(self, text="ID")
        self.idLabel.place(x=entryLeft-5, y=height//5, anchor="ne")
        self.idEntry = tkinter.Entry(self, bg='white', width=width//9, textvariable=str)
        self.idEntry.place(x=entryLeft, y=height//5, anchor="nw")


        self.pwLabel = tkinter.Label(self, text="PW")
        self.pwLabel.place(x=entryLeft-5, y=height//2, anchor="ne")
        self.pwEntry = tkinter.Entry(self, bg='white', width=width//9, textvariable=str)
        self.pwEntry.place(x=entryLeft, y=height//2, anchor="nw")
        self.pwEntry.bind('<KeyRelease>', self.modifyPW)
        self.pwEntry.bind("<KeyPress>", self.modifyPW)

        self.confirmButton = tkinter.Button(self, text="확인", command=self.confirm)
        self.confirmButton.place(x= width//4, y=height*4//5, anchor="center")
        self.cancelButton = tkinter.Button(self, text="취소", command=lambda: self.destroy())
        self.cancelButton.place(x=width*3//4, y=height*4//5, anchor="center")

        self.mainframe.settingEmailSenderButton["state"] = "disable"


    def confirm(self):
        self.id = self.idEntry.get()
        self.mainframe.mainframe.reciveEvent(LogIn=(self.id, self.pw))
        self.destroy()
    
    def destroy(self):
        self.mainframe.settingEmailSenderButton["state"] = "normal"
        super().destroy()


    def modifyPW(self, event):
        pwString = self.pwEntry.get()
        if len(self.pw) > len(pwString):
            self.pw = self.pw[0:len(pwString)]
        elif len(self.pw) < len(pwString):
            self.pw += pwString[len(self.pw):]

        pwString = "*" * len(pwString)
        self.pwEntry.delete(0, tkinter.END)
        self.pwEntry.insert(0, pwString)





