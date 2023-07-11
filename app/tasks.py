from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from app.models import Settings, User
from django.core import mail

# 配置日志记录器
import logging
logger = logging.getLogger('django')

# 异步发送验证邮件
@shared_task
def send_code(group_name,email_message,recipient_list):
    print("开始向" + str(recipient_list) + "发送验证码")
    channel_layer = get_channel_layer()  # 实例化get_channel_layer()对象，用于向组群发送消息
    #开始发送验证码
    try:
        mail.send_mail(
            subject='注册' + Settings.objects.get(id=1).web_name,  # 题目
            message=email_message,  # 消息内容
            from_email='algpythontest@outlook.com',  # 发送者[当前配置邮箱]
            recipient_list=recipient_list,  # 接收者邮件列表
            auth_password='ss699610'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
        )
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "email_code",
                'mode': 'code_message',
                'message': '验证码发送成功！'
            }
        )
    except:
        logger.error('邮件发送失败：' + str(recipient_list))
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "email_code",
                'mode': 'code_message',
                'message': '发送验证码出现异常！请检查你的邮箱！'
            }
        )