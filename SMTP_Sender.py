
# smtplib 用于邮件的发信动作
import smtplib
import sys
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头、


from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 发信方的信息：发信邮箱，QQ 邮箱授权码
c = sys.argv();
#参数：发信服务器 发件邮箱地址 发件邮箱密码/授权码 收件邮箱地址（多个用分号隔开）主题 附件位置（完整路径）
if(len(c) <= 5)
    print("参数错误！")
    print("请以下列格式输入参数：发信服务器 发件邮箱地址 发件邮箱密码/授权码 收件邮箱地址（多个用分号隔开）主题 附件位置（完整路径）")
    sys.exit()
# 收信方邮箱
#while True:
#    a=input('请输入收件人邮箱：')
#    #输入收件人邮箱
#    to_addrs.append(a)
#    #写入列表
#    b=input('是否继续输入，n退出，任意键继续：')
#    #询问是否继续输入
#    if b == 'n':
#        break

#print(to_addrs)

# 发信服务器
smtp_server = c[1]
from_addr = c[2]
password = c[3]
tmp_rec1 = c[4]
to_addrs = tmp_rec1.split(";")
title=c[5]
pdfFile=c[6]

 # 附件地址
#pdfFile = input('请输入文件路径')
#pdfFile = "d:/python/test.txt"
pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)

m = MIMEMultipart()
m.attach(pdfApart)

m['Subject'] = c[5]


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, m.as_string())
# 关闭服务器
server.quit()