from CustomTkClass import*
from tkinter.filedialog import askopenfilename,asksaveasfile

import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


class GmailAndXMLSaveLoadFrame(Frame):
    def __init__(self, mainframe, window, viewport):
        super(GmailAndXMLSaveLoadFrame, self).__init__(window, viewport)
        self.mainframe = mainframe
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
        tkinter.Button(gmailframe, text="보내기",command=self.sendEmail).pack(side=tkinter.RIGHT)

        xmlframe = tkinter.Frame(setframe)
        xmlframe.pack(anchor="w",fill="x")
        TempFont = tkinter.font.Font(self, size=15, weight='bold', family='Consolas')
        tkinter.Label(xmlframe,font=TempFont, text="XML 파일").pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="불러오기",command=self.XMLopen).pack(side=tkinter.LEFT)
        tkinter.Button(xmlframe, text="내보내기",command=self.XMLsave).pack(side=tkinter.LEFT)



    def sendEmail(self):
        # # MIME 문서를 생성합니다.
        # htmlFD = open(htmlFileName, 'rb')
        # HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
        # htmlFD.close()
        #
        # # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        # msg.attach(HtmlPart)

        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"

        senderAddr = self.mainframe.id  # 보내는 사람 email 주소.
        recipientAddr = self.dstGamilEntry.get()  # 받는 사람 email 주소.
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = self.makeStringMsg()
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        try:
            # 메일을 발송한다.
            s = smtplib.SMTP(host, port)
            # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(self.mainframe.id, self.mainframe.pw)
            s.sendmail(senderAddr, [recipientAddr], msg.as_string())
            s.close()
        except:
            self.raiseErrorWhenSendingMail()


    def XMLopen(self):
        filename=askopenfilename()
    def XMLsave(self):
        asksaveasfile()


    def raiseErrorWhenSendingMail(self):
        # 메일을 보낼 때, 문제가 발생시, 이 함수가 호출된다.
        # 에러 윈도우를 띄우거나 혹은 다른 방식으로 사용자에게 에러를 알려야 한다.
        pass


    def makeStringMsg(self):
        return "Test email in GmailAndXMLSaveLoadFrame"

