import email, getpass, poplib, sys

hostname = 'smtp.exmail.qq.com'
user = 'yanjp@feewee.cn'
passwd = 'Yanping32'



p = poplib.POP3_SSL('pop.gmail.com') #与SMTP一样，登录gmail需要使用POP3_SSL() 方法，返回class POP3实例
try:
    # 使用POP3.user(), POP3.pass_()方法来登录个人账户
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto: #可能出现的异常
    print('login failed')
else:
    response, listings, octets = p.list()
    for listing in listings:
        number, size = listing.split() #取出message-id
        number = bytes.decode(number)
        size = bytes.decode(size)
        print('Message', number, '( size is ', size, 'bytes)')

        response, lines, octets = p.top(number , 0)
        # 继续把Byte类型转化成普通字符串
        for i in range(0, len(lines)):
            lines[i] = bytes.decode(lines[i])
        #利用email库函数转化成Message类型邮件
        message = email.message_from_string('\n'.join(lines))
        # 输出From, To, Subject, Date头部及其信息
        for header in 'From', 'To', 'Subject', 'Date':
            if header in message:
            # print(": %s %s"  %(header,  message[header]))
            print(header)
            print(message[header])
        #与用户交互是否想查看邮件内容
        print('Read this message [ny]')
        answer = input()
        if answer.lower().startswith('y'):
            response, lines, octets = p.retr(number) #检索message并返回
            for i in range(0, len(lines)):
                lines[i] = bytes.decode(lines[i])
            message = email.message_from_string('\n'.join(lines))
            print('-' * 72)
            maintype = message.get_content_maintype()
            if maintype == 'multipart':
                for part in message.get_payload():
                    # if part.get_content_maintype() == 'text':
                mail_content = part.get_payload(decode=True).strip()
            elif maintype == 'text':
                mail_content = e.get_payload(decode=True).strip()
            try:
                mail_content = mail_content.decode('gbk')
            except UnicodeDecodeError:
                print('Decoding to gbk error')
                sys.exit(1)
            print(mail_content)
        print()
        print('Delete this message? [ny]')
        answer = input()
        if answer.lower().startswith('y'):
            p.dele(number)
            print('Deleted')
finally:
    print('log out')
    p.quit()