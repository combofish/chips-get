#!/usr/bin/env python
#-*- coding:utf-8 -*-


def fibonacci():
    a,b = 0,1
    while True:
        yield b a,b = b , a
fib = fibonacci()
print(fib.next())


"""
class MyIterator(object):
    def __init__(self,step):
        self.step=step
    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -=1
        return self.step
    def __iter__(self):
        return self
for el in MyIterator(4):
    print(el)
"""    

"""
i = iter('abcd')
i.next()
print(i.next())

print([i for i in range(10) if i % 2 == 0])
seq = ['one','two','three']
for i, element in enumerate(seq):
    seq[i] = '%d:%s' % (i,seq[i])
print(seq)
def _treatment(pos,element):
    return '%d:%s' % (pos,element)
se = [ 'one', 'two' , 'three']
print([ _treatment(i,el) for i ,el in enumerate(se)])
"""

"""
import os
os.mkdir('haha')

os.makedirs('test/multiple/levels')
f = open('test/multiple/levels/file','w')
f.write("inspector praline")
f.close()
"""

"""
#for file in os.listdir('/home/liming'):
#    print(file)
print(os.getcwd())
#os.chdir('/home/liming')
#print(os.getcwd())
print(os.pardir)
os.chdir(os.pardir)
print(os.getcwd())
"""

"""
import __builtin__
def function(a,b):
    print(a,b)
apply(function,("whi","cannc"))
apply(function,(1,2+3))
"""

"""
import os.path

print(os.path.commonpath('/home/liming/Documents/'))
print(os.path.abspath('/home'))
"""

"""
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
"""

"""
print('haha')
"""

"""
import poplib

email =''
password =''
pop3_server = ''

server = poplib.POP3(pop3_server)
print(server.getwelcome())
server.user(email)
server.pass_(password)

print('Message: %s.size:%s' % server.stat())

resp,mails,octets = server.list()

print(mails)
index = len(mails)
resp,lines,octets = server.retr(index)

msg_content = '\r\n'.join(lines)
msg = Parser().parsestr(msg_content)
server.quit()
"""

"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
###
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(), \
                       addr.encode('utf-8')))
from_addr = '18233092052@163.com'
password ='confidence'
smtp_server = 'smtp.163.com'
to_addr = '18233092052@139.com'

msg = MIMEText('hello,send by Python...','plain','utf-8')
msg['From'] = _format_addr('Python <%s> '% from_addr)
msg['To'] = _format_addr('admin:<%s>' % to_addr)
msg['Subject'] =Header('from smtp :','utf-8'.encode())
                       
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""

"""
from email.mime.text import MIMEText
msg = MIMEText('hello,send by python...','plain','utf-8')
from_addr = '18233092052@163.com'
password ='confidence'
smtp_server = 'smtp.163.com'
to_addr = '18233092052@139.com'

import smtplib
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""

"""    
import socket
import threading

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(r'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == r'exit' or not data:
            break
        sock.send(r'hello,%s!' % data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9998))
s.listen(5)
print('Waitting for connection...')
while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
"""

"""
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
#s.send(str('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'))

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
s.close()
header,html = data.split('\r\n\r\n',1)
print(header)
with open('sina.html','wb') as f:
    f.write(html)
"""
    
"""
from tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.hellLabel = Label(self,text='hello,world')
        self.hellLabel.pack()
        self.quitButton = Button(self,text='quit',command=self.quit)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','hello,%s'% name)
        
app = Application()
app.master.title('hello world')
app.mainloop()
"""

"""
import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndChar():
    return chr(random.randint(65,90))
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 *4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('Arial.ttf',36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndColor())
for t in range(4):
    draw.text((60*t + 10,10),rndChar(),font = font,fill= rndColor2())

image = image.filter(IMageFilter.BLUR)
image.save('code.jpg','jpeg')
"""

"""
######---模糊效果---
import Image,ImageFilter
im = Image.open()
im2 = im.filter(ImageFilter.BLUR)
im2.save('',jpeg')
"""

"""
import Image

im = Image.open('/home/liming/Document/pictures_learn/use.jpg')
w,h = im.size
im.thumbnail((w//2,h//2))
im.save('/home/liming/use_smaller.jpg','jpeg')
"""

"""
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_stringtag(self,tag,attrs):
        print('<%s>' % tag)
    def handle_endtag(self,tag):
        print('<%s>', tag)
    def handle_startendtag(self,tag,attrs):
        print('<%s/>' % tag)
    def handle_data(self,data):
        print('data')
    def handle_comment(self,data):
        print('data')
    def handle_entityref(self,name):
        print('&%s;' % name)
    def handle_charref(self,name):
        print('&#%s;' % name)
parser = MyHTMLParser()
parser.fes('<html><head></head><body><p>Some <a href=\"#\">html></a> tutorial...<br>END</p></body></html>')
"""

"""
l = []
l.append(r'<?xml version="1.0"?>')
l.append(r'<root>')
#l.append(encode('some & data'))
l.append('hahaha')
l.append(r'</root>')
print(''.join(l))
"""

"""
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:star_element:%s,attrs:%s' % (name,str(attrs)))
    def end_element(self,name):
        print('sax:end_element:%s' % name)
    def char_data(self,text):
        print('sax:char_data:%s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a><li>
    <li><a href="/ruby">Ruby</a><li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.end_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = hadler.char_data
parser.Parse(xml)
"""

"""
import itertools

ri = map(lambda x : x *x,itertools.count(1))
for i in ri:
    print(i)
r = map(lambda x: x * x,[1,2,3])
print(*r)
print(r)
"""

"""
for x in itertools.imap(lambda x,y : x * y,[10,20,30], itertools.count(1)):
    print(x)
"""    

"""
natuals = itertools.count(1)
for n in natuals:
    print(n)
"""    

"""
cs = itertools.cycle('ABC')
for c in cs:
    print(c)
"""

"""
ns = itertools.repeat('a',10)
for n in ns:
    print(n)
"""

"""    
naturals2 = itertools.count(1)
ns2 = itertools.takewhile(lambda x:x <=10,naturals2)
for n in ns2:
    print(n)
"""

"""
for c in chain('anbijnl','ajhsd'):
    print(c)
"""

"""
for key,group in itertools.groupby('aaabbbbvccccCccdddd',lambda c : c.upper()):
    print(key,list(group))
"""
    
"""
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in')
print(md5.hexdigest())
"""
