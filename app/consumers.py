from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from app.models import Settings

#配置日志记录器
import logging
logger = logging.getLogger(__name__)

class login(WebsocketConsumer):
    def websocket_connect(self, message):
        '''
        当有客户端向后端发送websocket连接请求时，自动触发该函数
        :param message:
        :return:
        '''
        # 服务器允许客户端创建连接
        self.accept()
        self.send(text_data=json.dumps({'mode': 'load','web_name':''}))


    def websocket_receive(self, message):
        '''
        浏览器基于websocket向后端发送数据，自动触发接受消息，并且处理信息
        :param message:
        :return:
        '''
        # 输出消息
        print(message)
        # 服务端向前端回消息
        self.send('服务器收到了你的消息：%s' % (message['text']))

    def websocket_disconnect(self, message):
        '''
        客户端与服务端断开连接时，自动触发该函数
        :param message:
        :return:
        '''
        print('断开连接')
        raise StopConsumer()