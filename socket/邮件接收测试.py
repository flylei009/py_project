import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getpass, poplib

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "yanjp@feewee.cn"  # 用户名
mail_pass = "Yanping321"  # 口令

sender = 'yanjp@feewee.cn'
receivers = ['404206459@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


M = poplib.POP3_SSL(mail_host)
M.user(mail_user)
M.pass_(mail_pass)
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)