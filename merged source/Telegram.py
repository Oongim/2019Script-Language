import telepot
import traceback
import sys
import MainFrame
from GoogleMap import Parsing_KAKAOMAP_Address,make_googlemap_url
import urllib.request
import PIL.Image
import PIL.ImageTk
import io
import os
class Telegram:
    def __init__(self):
        self.bot=telepot.Bot('893098103:AAEyC5H6VX3rbUKDGUQMAEnTYKxogA8PETw')
        self.bot.getMe()

        self.bot.sendMessage('759465478', '안녕')
        self.bot.message_loop(self.handle)

    def sendMessage(self,user, msg,photo=None):
        print(photo)
        try:
            self.bot.sendMessage(user, msg)
            if photo:
                self.bot.sendPhoto(chat_id=user, photo=open('./Image/TelegramSendImage.png', 'rb'))

        except:
            traceback.print_exc(file=sys.stdout)

    def replyAptData(self, user):
        res_list = MainFrame.mainframe.selectionInfoFrame.dataList
        if len(res_list) is 0:
            self.sendMessage( user, '찜목록에 데이터가 없습니다.' )
            return
        msg = ''

        for r in res_list:
            strAdress = r.data["법정동"] + r.data["지번"]
            map_url = make_googlemap_url(Parsing_KAKAOMAP_Address(strAdress)[0])
            with urllib.request.urlopen(map_url) as uFile:
                imgSrc = uFile.read()
            rawImage = PIL.Image.open(io.BytesIO(imgSrc))
            rawImage.save(os.path.join(os.getcwd()+'/Image', 'TelegramSendImage.png'))

            msg = str(r)+'\n'
            self.sendMessage(user, msg, rawImage)


    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')
        if text.startswith('찜목록'):
            print('try to 찜목록')
            self.replyAptData(chat_id)
        else:
            self.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [지역번호], 저장 [지역번호], 확인 중 하나의 명령을 입력하세요.')

if __name__ == "__main__":
    Telegram()