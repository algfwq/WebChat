from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from app.models import Settings
from django.conf import settings
from django.core.cache import cache #引入缓存模块
from django.core import mail
import random
import json

#配置日志记录器
import logging
logger = logging.getLogger('django')

class login(WebsocketConsumer):
    def websocket_connect(self, message):
        '''
        当有客户端向后端发送websocket连接请求时，自动触发该函数
        :param message:
        :return:
        '''
        # 服务器允许客户端创建连接
        self.accept()
        self.send(json.dumps({'mode': 'load',
                              'web_name':Settings.objects.get(id=1).web_name,
                              'email':Settings.objects.get(id=1).email_ture }))

    def websocket_receive(self, message):
        '''
        浏览器基于websocket向后端发送数据，自动触发接受消息，并且处理信息
        :param message:
        :return:
        '''
        # 输出消息
        print(message['text'])
        text = dict(eval(message['text']))
        #如果为发送验证码请求
        if text['mode'] == 'send_code':
            #生成验证码
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1,9)
            code =  a*1000 + b*100 + c*10 + d
            #缓存验证码到Redis
            cache.set(text['email'], code, 30 * 60)  # 写入key为v，值为555的缓存，有效期30分钟
            #发送验证码到用户邮箱
            email = text['email']
            email_message = "您正在注册" + Settings.objects.get(id=1).web_name + "，您的验证码是：" + str(code) + "。有效期30分钟。如果这不是你本人操作，您的邮箱账号很可能已经泄漏，并且被他人用于非法目的。"
            recipient_list = []
            recipient_list.append(email)
            try:
                mail.send_mail(
                    subject='注册' + Settings.objects.get(id=1).web_name,  # 题目
                    message=email_message,  # 消息内容
                    from_email='algpythontest@outlook.com',  # 发送者[当前配置邮箱]
                    recipient_list=recipient_list,  # 接收者邮件列表
                    auth_password='ss699610'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
                )
                self.send(json.dumps({'mode':'code_message','message':'验证码发送成功！'}))
            except:
                logger.error('邮件发送失败：' + email)
                self.send(json.dumps({'mode':'code_message','message':'发送验证码出现异常！请检查你的邮箱！'}))

    def websocket_disconnect(self, message):
        '''
        客户端与服务端断开连接时，自动触发该函数
        :param message:
        :return:
        '''
        print('断开连接')
        raise StopConsumer()