from CustomTkClass import*
from tkinter.filedialog import askopenfilename,asksaveasfile
import tkinter.messagebox
import imghdr

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.message import EmailMessage


class AccountManager:
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    def __init__(self):
        self.isLoggedIn = False
        self.isInit = False
        #self.initSMTP()


    def __del__(self):
        if self.isInit:
            self.smtp.close()


    def initSMTP(self):
        self.smtp = smtplib.SMTP(self.host, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.isInit = True

    def resetSMTP(self):
        self.smtp.close()
        del self.smtp
        self.initSMTP()


    def login(self, id, pw):
        if not self.isInit:
            self.initSMTP()
        else:
            self.resetSMTP()

        self.isLoggedIn = False
        try:
            self.smtp.login(id, pw)
        except smtplib.SMTPAuthenticationError:
            tkinter.messagebox.showerror("로그인 오류", "로그인 실패\n사유 : id 혹은 pw 가 틀렸습니다.")
            return False
        except UnicodeEncodeError:
            tkinter.messagebox.showerror("로그인 오류", "로그인 실패\n사유 : 유니코드 문자는 받을 수 없습니다.")
            return False
        except:
            tkinter.messagebox.showerror("로그인 오류", "로그인 실패\n사유 : 알 수 없는 로그인 오류입니다."
                                                   "\n       관리자에게 문의하세요.")
            return False

        self.id = id
        self.isLoggedIn = True
        tkinter.messagebox.showinfo("로그인 성공", "{id}\n로그인 되었습니다.".format(id=id))
        return True


    def sendMail(self, recipientAddrs, mailMsg):
        self.smtp.sendmail(self.id, recipientAddrs, mailMsg)




class GmailAndXMLSaveLoadFrame(Frame):
    def __init__(self, mainframe, window, viewport):
        super(GmailAndXMLSaveLoadFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
        self.accountManager = AccountManager()
        width = viewport.width

        TempFont = tkinter.font.Font(self, size=20, weight='bold', family='Consolas')

        tkinter.Label(self, font=TempFont, text="목록 내보내기 ").pack(side=tkinter.LEFT)

        setframe = tkinter.Frame(self)
        setframe.pack(side=tkinter.LEFT)
        gmailframe=tkinter.Frame(setframe)
        gmailframe.pack()
        TempFont = tkinter.font.Font(self, size=15, weight='bold', family='Consolas')
        tkinter.Label(gmailframe,   font=TempFont,text="Gmail   ").pack(side=tkinter.LEFT,anchor="w")
        self.dstGamilEntry = tkinter.Entry(gmailframe, width=int((width - 160) / 10), text="Gmail")
        self.dstGamilEntry.pack(side=tkinter.LEFT)
        tkinter.Button(gmailframe, text="보내기",command=self.procSendEmail).pack(side=tkinter.RIGHT)

        xmlframe = tkinter.Frame(setframe)
        xmlframe.pack(anchor="w",fill="x")
        TempFont = tkinter.font.Font(self, size=15, weight='bold', family='Consolas')
        tkinter.Label(xmlframe,font=TempFont, text="XML 파일").pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="불러오기",command=self.XMLopen).pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="내보내기",command=self.XMLsave).pack(side=tkinter.LEFT)


    def logIn(self, id, pw):
        self.accountManager.login(id, pw)

    def getIsLoggedIn(self):
        return self.accountManager.isLoggedIn

    def procSendEmail(self):
        dataSelected, mapImgReadData = self.mainframe.reciveEvent(getDataSelectedinSelection=None)
        if dataSelected == None:
            tkinter.messagebox.showerror("메일 전송 오류", "메일 전송 실패\n사유 : 메일을 보내기 이전에"
                                                     "\n     찜 목록에서 메일로 보낼 대상을 선택해야 합니다.")
            return

        if self.accountManager.isLoggedIn:
            self.sendEmail(dataSelected, mapImgReadData)
        else:
            tkinter.messagebox.showerror("메일 전송 오류", "메일 전송 실패\n사유 : 로그인이 되어있지 않습니다.")


    def sendEmail(self, dataSelected, mapImgReadData):      
        recipientAddr = self.dstGamilEntry.get()  # 받는 사람 email 주소.
       
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.makeTitleStringMsg()
        msg['From'] = self.accountManager.id
        msg['To'] = recipientAddr

        msgHtml = MIMEText('<br><img src="cid:image1">' + dataSelected.getStringInHtml(), 'html')
        msg.attach(msgHtml)

        msgImage = MIMEImage(mapImgReadData)
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)

        try:
            self.accountManager.sendMail(recipientAddr, msg.as_string())
            tkinter.messagebox.showinfo("메일 전송 성공", "메일을 전송하였습니다.")
        except:
            tkinter.messagebox.showerror("메일 전송 오류", "메일 전송 실패\n사유 : 알 수 없는 메일 전송 오류입니다."
                                                     "\n       관리자에게 문의하세요.")

    def makeTitleStringMsg(self):
        return "Your Selection House List From KPU_HOUSE, Sanbang"


    def XMLopen(self):
        filename=askopenfilename()


    def XMLsave(self):
        asksaveasfile()




