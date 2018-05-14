#coding=utf8
import itchat
import requests
from threading import Timer

itchat.auto_login(hotReload=True)

def get_news():
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    contents  = r.json()['content']
    translation = r.json()['translation']
    return contents, translation

def send_news():
    try:
        itchat.auto_login(hotReload = True)
        my_friend = itchat.search_friends(name = '毛蛋')
        MaoDan = my_friend[0]["UserName"]
        myself = 'filehelper'

        #获取金山字典内容
        message1 = str(get_news()[0])
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "来自Jason"
        #发送消息
        itchat.send('中午好!', toUserName = MaoDan)
        #itchat.send(message2, toUserName = myself)
        #itchat.send(message3, toUserName = myself)
        #itchat.send(u'测试消息发送', 'filehelper') 
        t = Timer(86400, send_news)
        t.start()
    except:
        itchat.send(u"今天消息发送失败了", 'filehelper') 

if __name__ == "__main__":
    send_news()
