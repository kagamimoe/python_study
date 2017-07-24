# -*- coding: utf-8 -*-
import urllib2
import sys, smtplib, poplib
from email.mime.text import MIMEText


reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup


msg_head = ['From:z7039585@163.com',
            'To:251162626@qq.com',
            'Subject:V2EX酷工作节点 每日职位信息']
msg_body = ''

base_url = 'https://www.v2ex.com/go/jobs?p='
href_url = 'https://www.v2ex.com'
t_list = []
link_list = []
words = [u'测试',u'QA',]   #这里设置抓取关键词

mailto_list=["251162626@qq.com"]   #收件人邮箱
mail_host="smtp.163.com"  #设置SMTP服务器
mail_user="z7039585@163.com"    #发件人邮箱
mail_pass="password"   #发件人邮箱密码
mail_postfix="163.com"  #发件箱的后缀



def get_house_list():
    global  t_list
    global  link_list
    i = 1

    while i < 15:
        print '*****第' + str(i) + '次抓取开始*****'
        page = urllib2.urlopen(base_url + str(i))
        html = page.read()
        soup = BeautifulSoup(html.decode("utf-8"))
        title_list = soup.find_all("span",class_="item_title")

        for tag in title_list:
            for word in words:
                if word in (tag.contents[0]).string:
                    t_list.append((tag.contents[0]).string)
                    link_list.append(href_url + (tag.contents[0])['href'])
        i = i + 1
    print '*****抓取完毕，总计抓取'+ str(i) +'页*****'
    return t_list, link_list


def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="admin"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    get_house_list()
    for i in range(len(t_list)):
        msg_body = msg_body + ''.join(t_list[i]) + '<br><href>' + ''.join(link_list[i]) + '</href><br><br>'

    if send_mail(mailto_list,"V2EX酷工作节点 每日职位信息 ",msg_body):
        print "邮件发送成功！"
    else:
        print "邮件发送失败！"
