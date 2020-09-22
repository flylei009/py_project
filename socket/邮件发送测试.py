import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "yanjp@feewee.cn"  # 用户名
mail_pass = "Yanping321"  # 口令

sender = 'yanjp@feewee.cn'
receivers = ['404206459@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender, [receivers, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    print("邮件发送成功")
    server.quit()  # 关闭连接

except smtplib.SMTPException as ex:
    print ("error  :%s\n" %ex)
    print("Error: 无法发送邮件")