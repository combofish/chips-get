#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import struct

#print(struct.pack('123796'))
#print(struct.unpack('>IH','\xf0\xf0\xfo'))



def use:
    return 0


def use:
    return 0


def use:
    return 0


def ha:
    pass


"""
import base64

"""

"""
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
"""

"""
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity
    def __setitem(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)
"""        

"""
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
odd = OrderedDict()
odd['z'] = 3
odd['y'] = 2
odd['x'] = 1
print(odd)
"""

"""
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['k'] = 'abc'
print(dd['k'])
print(dd['kw'])
"""

"""
from collections import deque
q=deque(['a','b','c'])
q.append('a')
q.appendleft('v')
print(q)
"""

"""
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)
print(isinstance(p,tuple))
print(isinstance(p,Point))
"""

"""
import re
test1 = 'someone@gmail.com'
test2 = 'bill.gates@microsoft.com'
test3 = '<Tom Paris> tom@voyager.org'
re1 = r'^([a-z]+)@([a-z]+).(com|cn|org|cc)$'
re2 = r'^([a-z]+).?([a-z]+)@([a-z]+).(com|cn|org)$'
re3 = r'^<(\w+)(\s*)(\w+)>(\s*)([a-z]+)@([a-z]+).(us|cn|com|org)$'
print(re.match(re2,test1).groups())
print(re.match(re2,test2).groups())
print(re.match(re3,test3).groups())
"""

"""
import re
print('a b    c'.split(' '))
print(re.split(r'\s+','a c    b'))
print(re.split(r'[\s\,\;]+','a b,c,d,,e;;;;e;f;g;h;d'))
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5]?[0-9])\:([0-5]?[0-9])$',t)
print(m)
print(m.group(0))
print(m.group(1))
print(m.groups())
print(re.match(r'^(\d+)(0*)$','102300').groups())
print(re.match(r'^(\d+?)(0*)$','102300').groups())
re_telephone = re.compile(r'^\d{3}-(\d{3,8})$')
print(re_telephone.match('010-23445').group(0))
mr = re_telephone.match('100-8086')
print(mr.groups())
"""

"""
print(r'ABC\-001')
import re
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
test = 'hahah123'
if re.match(r'^\w\w*\d{0,8}$',test):
    print('Ok')
else:
    print('Failed')
"""

"""
#taskmanager.py

import random, time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

#print(dir(Queue))
task_queue = Queue()
result_queue = Queue()

class QueueManager(BaseManager):
    pass
QueueManager.register('get_tesk_queue',callable = lambda: task_queue)
QueueManager.register('get_result_queue',callable = lambda: result_queue)

manager = QueueManager(address=('',5000),authkey=12)

manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)
print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
manager.shutdown()    
"""

"""
import threading

local_school = threading.local()

def process_student():
    print('hello, %s (in %s)' % (local_school.student,threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()
t1 = threading.Thread(target = process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target = process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
"""
    
"""
global_dict = {}
def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()
def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_1(std)

def do_tesk_1(std):
    do_subtask_1(std)
    do_subtesk_2(std)

def do_tesk_2(std):
    do_subtesk_2(std)
    do_subtest_2(std)
"""

"""
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
"""
    
"""
import time,threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
"""

"""
import time,threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n= 0
    while n <10:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)
"""

"""
from multiprocessing import Process,Queue
import os, time, random

def write(q):
    for value in ['a','b','c']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
"""

"""
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task,args=(i,))
    print('Waitting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
"""

"""
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Process will start.')
    p.start()
##    p.join()
    print('Process end.')
"""

"""
import os

print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) amd my parent is %s.' % (os.getpid(),os.getppid()))
else :
    print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
"""

"""
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('liming',20,99)
#print(json.dumps(s))

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age":20,"score":88,"name":"Bon"}'
print(json.loads(json_str,object_hook = dict2student))
"""

"""
import json

d = dict(name='Bob',age=20,score=100)
print(json.dumps(d))
print(json.loads(json.dumps(d)))
"""

"""
try:
    import cPickle as pickle
except ImportError:
    import pickle
d= dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))

with open('/home/liming/Documents/dump.txt','wb') as f:
    pickle.dump(d,f)
    
with open('/home/liming/Documents/dump.txt','rb') as fi:
    d = pickle.load(f)
    print(d)    
"""

"""
import os

def search(str,abspath):
#    abspath = os.path.abspath('.')
    for x in os.listdir(abspath):
        if os.path.isdir(x):
            next_dir = os.path.join(abspath,x)
            search(str,next_dir)
        if os.path.isfile(x):
            if str in x:
                print(os.path.join(abspath,x)

#abs_path = os.path.abspath('.')
strn='py'

#    abspath = os.path.abspath('.')
for x in os.listdir('.'):
    if os.path.isdir(x):
        next_dir = os.path.join('.',x)
        search(strn,next_dir)
    if os.path.isfile(x):
        if strn in x:
            print(os.path.join('.',x)
"""

"""
print([x for x in os.listdir('.')])
"""

#abspath = os.path.abspath('.')

"""                
def search(str,abspath):
#    abspath = os.path.abspath('.')
    for x in os.listdir(abspath):
        if os.path.isdir(x):
            next_dir = os.path.join(abspath,x)
            search(str,next_dir)
        if os.path.isfile(x):
            if str in x:
                print(os.path.join(abspath,x)
##if __name__ == 'main':
##    search('py','.')      
"""
                  
"""
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.jpg'])
"""

"""
print(os.name)
print(os.uname())
print(os.environ)
print(os.getenv('PATH'))
"""

"""
import codecs

with codecs.open('/home/liming/test.txt.python','w','utf-8') as f:
    f.write('hahahh')
"""

"""
with open('/home/liming/test.txt.python','w') as f:
    f.write('hahahhaha!')
"""

"""
f = open('/home/liming/ha.jpg','rb')
print(f.read())
f.close()
"""

"""
with open('/home/liming/vimrc.bak','r') as f:
##    print(f.read())
    for line in f.readlines():
##        print(line)
        print(line.strip())
##    print(f.read(4))
"""

"""
try:
    f = open('/home/liming/vimrc.bak','r')
    print(f.read())
finally:
    if f:
        f.close()
"""        
        
"""
import re
m=re.search('(?<=abc)def','abcdef')
print(m.group(0))
"""

"""
import unittest

class Dict(dict):
    '''
    >>>d1 = Dict()
    >>>d1['x'] = 100
    >>>d1.x
    100
    >>>d1.y = 200
    >>>d1['y']
    200
    >>>d2 = Dict(a=1,b=2,c='3')
    >>>d2.c
    '3'
    >>>d2['empty']
    '''
    
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Dict" object has no attribute "%s"' % key)
    def __setattr__(self,key,value):
        self[key] = value

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
if __name__ == 'main':
#    unittest.main()
    import doctest
    doctest.testmod()
"""

"""
import pdb
import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n= int(s)
##logging.info('n = %d' % n)
pdb.set_trace()
print(10 / n)
"""

"""
def foo(s):
    n = int(s)
    assert n != 0,'n is zero!'
    return 10 / n
def main():
    foo('0')
main()
"""

"""
try:
    10 /0
except ZeroDivisionError:
    raise ValueError('input error!')
"""

"""
class FooError(StandardError):
    pass

def foo(s):
    n=int(s)
    if n == 0:
        raise FooError('invalid valu: %s' % s)
    return 10 / n

def bar(s):
    return foo(s) *2
def main():
    try:
        bar('0')
    except StandardError:
       # logging.exception()
        raise
main()
print('end')
"""

"""
try:
    print('try...')
    r = 10 /0
    print('result:' ,r)
except ZeroDivisionError:
    print('except:')
finally:
    print('finally...')
print('End')    
"""

"""
class Student(object):
    name = 'Student'
s= Student()
print(s.name)
print(Student.name)
s.name = 'liming'
print(s.name)
print(Student.name)
del s.name
print(s.name)
"""

"""
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varcar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new_(cls,name,bases,attrs)
        mappings = dict()
        for k,v in attrs.iteritems():
            if isinstance(v,Field):
                print('Found mapping: %s==>%s' % (k,v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name
        attrs['__mappings__'] = mappings
        return type.__new__(cls,name,bases,attrs)
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            
            raise AttributeError("'model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.iteritems():
            fields.append(v.name)
            fields.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,',',join(fields),','.join(paams))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))
        
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    passwd = StringField('password')

u = User(id=12345,name='liming',email='test@123.com',password='my-pwd')
u.save()
"""

"""
li = list()
li.add(1)
print(li)

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

class Mylist(list):
    __metaclass__ = ListMetaclass

l=Mylist()
l.add(1)
print(l)
"""

"""
def fn(self,name='world'):
    print('hello,%s.' % name)
Hello = type('Hello',(object,),dict(hello=fn))
h=Hello()
print(h.hello())
h.hello()
print(type(h))
print(type(Hello())
"""      

"""
class Student(object):
    def __init__(self,name):
        self._name=name
    def __call__(self):
        print('My name is %s。' % self._name)
s= Student('liming')
##print(s)
print(s())
print(callable(s))
"""

"""
#链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    
    def __str__(self):
        return self._path

print(Chain().status.user.timeline.list)
"""

"""
class Student(object):
    def __init__(self):
        self.name='liming'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 29
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s=Student()
print(s.name)
print(s.score)
print(s.age())
print(s.abs)
"""

"""
print(range(19,388)[5:10])

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a >100000:
            raise StopIteration()
        return self.a
    
class Fibn(object):    
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop=n.stop
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>= start:
                    l.append(a)
                a,b=b,a+b
            return l
print(Fibn()[12:200])        
print(Fibn()[5])
print(Fibn()[20])
for n in Fib():
    print(n)
"""
    
"""
class Student(object):
    def __init__(self,name):
        self.name= name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__=__str__
s=Student('liming')
print(s)
print(s.__repr__())
"""

"""
class Anmial(object):
    pass

#大类
class Mammal(Anmial):
    pass

class Bird(Anmial):
    pass

#各种动物
class Dog(Mammal,Runnable):
    pass

class Cat(Mammal,Runnable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Flyable):
    pass

class Runnable(object):
    pass

class Flyable(object):
    pass
"""

"""
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score= value

    @property
    def hang(self):
        return 2014-self._score

s=Student()
s.score=60
print(s.score)
print(s.hang)
s.score=999
"""

"""
from types import MethodType

class Stu:
    __slots__=('name','age','score')
    pass
class Daxue(Stu):
    __slots__=('str')
    pass
d=Daxue()
d.str=10
#d.uu=100
print(d.str)
d.score=100
print(d.score)
s=Stu()
s.name='hah'
print(s.name)
s2=Stu()
#print(s2.name)
def set_age(self,age):
    self.age=age
##s.set_age = MethodType(set_age,s)
Stu.set_age = MethodType(set_age,Stu)
s.set_age(10)
print(s.age)
#s2.set_age(28)
s2.set_age(12)
print(s2.age)
s.score=102
"""

"""
class Fu:
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x
    
f=Fu()
print(hasattr(f,'x'))
setattr(f,'x',12)
print(getattr(f,'x'))
print(getattr(f,'y',10))
fn=getattr(f,'power')
print(fn)
print(fn())
"""

"""
print(len('asc'))
print(dir('abc'))
print('abc'.__len__())
"""

"""
import types
import math

a=list()
class Dog():
    pass
b=Dog()
class Zangao(Dog):
    pass
c=Zangao()
print(isinstance('a',str))
print(type('abs')==types.StringType)
print(type([])==types.ListType)
print(isinstance(c,Dog))
print(isinstance(a,list))
print(isinstance(b,Dog))
print(type(b))
print(type(abs(3)))
print(type(abs))
"""

"""
from __future__ import unicode_literals

#print('\'xxx\'',isinstance('xxx',unicode))
#print('u\'xxx\'',isinstance(u'xxx',unicode))
print('\'xxx\'',isinstance('xxx',str))
print('b\'xxx\'',isinstance(b'xxx',str))
"""

"""
import sys

print(sys.path)
print(10/3)
"""

"""
import hello

hello.test()
print(hello.__doc__)
"""

"""
import functools
print(int("23312"))
print(int("128",10))
int2 = functools.partial(int,base=2)
print(int2("101001010"))
"""

"""
def log(test):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():"%(test,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print("sdfa'1.23,safdsfds23'")
now()
"""

"""
def log(func):
    def wrapper(*args,**kw):
        print("call %s():"%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2013-12-25')
now()
"""

"""
def nuo():
    pass
print(nuo.__name__)
"""

"""
def build(x):
    return lambda : x*x 
f=build(100)
print(f())
print(build(1000)())

def now():
    print('hahah')
f = now
f()

print(*map(lambda x: x*x, [1,2,3,4,5,6,7,8]))
"""

#匿名函数
"""
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())
"""

"""
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5,6,7)
f2=lazy_sum(1,2,3,4,5,6,7)

print(f)
print(f())
print(f2 == f)
"""

"""
def calc_sum(*args):
    ax=0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(*[1,2,3,4,5,6,7]))
"""

"""
print(sorted(['bon','sdfs','sdfa']))

def cmp_ignore_case(s1,s2):
    u1=s1,upper()
    u2=s2.upper()
    if u1 < u2 :
        return -1
    if u2 > u2 :
        return 1
    return 0
print(*sorted(['dfgd','tyuy','yth','hsdfk'],cmp_ignore_case))

l=[1,23,324,53,643,76,754,45,0]
def up_to_down(x,y):
    if x > y :
        return -1
    elif x == y :
        return 0
    else:
        return 1
#print(sorted(up_to_down,l))
print(sorted(l,up_to_down))
"""

#print(sorted([21,24,532,64,7,43,7,3542,87,32243]))


"""
def isPrime(n):
    nm=1
    for i in range(1,n):
        nm=i+1
        if n%i == 0:
            break
    if nm == n :
        return True
    return False

l=[]

for num in range(1,101):
    l.append(num)
print(*filter(isPrime,l))
"""

"""
def ou(n):
    return n%2 == 0

l=[1,2,3,4,5,6,7]
print(*filter(ou,l))

def not_empty(s):
    return s and s.strip()

l=filter(not_empty,['a','','s','','','sd'])
print(*l)
"""

"""
name=['sd','asSSAFF','fasS']
def toStringName(l=[]):
    def up(n=[]):
        n[0]=n[0]-32
    for n in l:
        n.lower()
        up[n]
    return l
print(toStringName(name))
"""

"""
def x2(x):
    return x*x
l=[1,2,3,4,5,6,7,8,9]
def ad(x,m):
    return x+m
print(reduce(ad,l))
print(*map(x2,l))
print(l)
print(*map(str,[1,2,3,4,5]))

def add(a,b,fn):
    return fn(a)+fn(b)
print(add(-4,2,abs))
"""

"""
print(abs)
f=abs
ft=abs(-19)
print(f)
print(ft)
abs = 10
print(abs)
"""

"""
def fib(n):
    i,f1,f2=0,0,1
    while i<n:
#        print(f2)
        yield f2
        i=i+1
        f1,f2=f2,f1+f2
q=fib(6)        
print(q)
#q.next()
for i in fib(6):
    print(i)
"""
    
"""
g=(x*x for x in range(1,10))
for x in g:
    print(x)
"""

"""
l=['saASDADf','sfSSAd','reweSDDF']
print([s.lower() for s in l])
"""

"""
d={'x':'a','y':'b','z':'c'}
for k,v in d.iteritems():
    print(k,'=',v)
"""

"""
import os
print([d for d in os.listdir('.')])
"""

"""
l=[]
for i in range(1,10):
    l.append(i*i)
print(l)
print([m+n for m in 'avbc' for n in 'ajds'])
#range
range(1,100)
print(range(1,100))
"""

"""
for x,y in [(1,2),(2,3),(3,4)]:
    print(x,'now',y)
l=[1,2,3,4,5,6,7,9]
for i,value in enumerate(l):
    print(i,'is',value)
"""

"""
d={'sa':12,'dkfj':23,'sdf':34}
for key in d:
    print(key)
j='sldjfgasl'
for cr in j:
    print(cr)
"""

"""
name=('liingj','kjjjj')
print(name[1:2])
print(name)
charn='liyubhbk'
print(charn[-5:])
l=[]
for i in range(100):
    l.append(i+1)
print(l)
print(l[:10:5])
print(l[:10:2])
"""

"""
l=['liming','bob','jiu']
print(l[0])
for i in range(3):
    print(l[i])
print(l[:3])
print(l[:2])
print(l[-3:-2])
"""
"""
l=[]
for i in range(50):
    i=i+1
    l.append(2*i-1)
print(l)
"""

"""
def fact_large(n):
    result=1
    for i in range(n):
        result = result * (i+1)
    return result
print(fact_large(1000))
"""
"""
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
#print(fact(4))
#print(fact(100))

def fact_new(n):
    return fact_use(n,1)

def fact_use(n,result):
    if n==1:
        return result
    return fact_use(n-1,n*result)
print(fact_new(1000))
"""

"""
def func(a,b,c=0,*args,**kw):
    print("a=",a,"b=",b,"c=",c,'args=',args,'kw=',kw)
func(1,2)
func(1,2,c=4)
func(1,2,*(1,2,3,4,5,6,7),**{'kw':'3435'})
func(1,2,3,*[1,2,3,4,5],x=99)
func(1,2,3,'a','b')
a=[1,2,3,4]
b={'as':223,'sfg':00}
func(*a,**b)
"""

"""
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)
person('liming',12,gender='M',job='Engineer')
person('liming',13)
"""
    
"""
#可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3,4,5,6,7))
print(calc(*[1,2,3,4,56,7]))
"""

"""
#def add_end(l=[]):
def add_end(l=None):
    if l is None:
        l=[]
    l.append("end")
    return l

m=[1,2,3,4,56,90]
print(add_end(m))
print(add_end())
print(add_end())
print(add_end())
"""

"""
def power(x):
    return x*x

def power(x,n=3):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(2))
print(power(3,4))
"""


"""
def nop():
    pass
#nop()

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x<0 :
        return -x
    else :
        return x
print(my_abs(-293))
print(my_abs("a"))
#a=abs()
a=abs
print(a(-10))
"""

"""
s1=set([1,2,3,4,5,65,6,5,5,5,3,4,3,3])
s2=set([2,3,4,56,7,8,9,0])
print(s1 & s2)
print(s1 | s2)

a='abc'
b=a.replace('a',"A")
print(a)
print(b)

g=['d','z','a','c','h','j']
#print(g.sort())
print(g)
g.sort()
print(g)

d={"liming":12,"Bob":90,"Jhon":123}
print(d.get("Bob"))
d.pop("Jhon")
print("liming" in d)
print("Jhon" in d) 
for x in range(2):
    if x < 1:
        print("programer is continue") 


num = 2
#num = int(input("Enter a number"))
if num > 5:
    print("large then 5")


sum = 0
for x in range(101):
    sum+=x
print(sum)

age=10
if age >=18:
    print("Your age is",age)
else: 
    print("Your age is",age) 
    print("tennager")


b=(0,)
print(len(b))




classmates=['sjjdsfh','jsfk','jfsiw']
print(len(classmates))
for name in classmates:
    print(name)






print('Hi,%s' % u'立即')
print('中文测试正常')
#print ("haha","toto","three")
#print (1000+29099)
print (10/3)

a="ABC"
b=a
a="XYZ"
print(b)


print(len(u'中文'.encode('utf-8')))
###

print(ord('A'))
print(chr(65))
#print("\\\n\\")

#print(r'\\\\n\\')
"""
"""
print('''hah
        sdjfha
        safj''')


if not 0:
    print("False")
"""
"""
#print("hahah\"liming\"you")
#print(1.333e45)
#name = input("Input your name: ")
#print ("hello ",name)
a=100 
if a>= 100:
    print(a)
else:
    print(-a)
"""
