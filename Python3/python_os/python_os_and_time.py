def write_date():
    import time

    now = time.time()
    str = time.ctime(now)
    fout = open('save_time.txt','wt')
    print(str,file=fout)
    fout.close()

def list_dir():
    import os

    print("当前目录下的文件： ",os.listdir('.'),
          "\n父目录下的文件： ",os.listdir('../'))
    os.chdir('../')
    print("父目录下的文件： ",os.listdir('./'))

def do_this():
    import os
    import random
    import time

    t = random.randint(1,5)
    print("Wait %s seconds, process %s " % (t,os.getpid()))
    time.sleep(t)
    now = time.time()
    print("Process %s End time: %s " % (os.getpid(),time.ctime(now)))


def use_process():
    import multiprocessing
    for n in range(3):
        p = multiprocessing.Process(target=do_this)
        p.start()

def use_date():
    from datetime import date

    birthday = date(2003,6,7)
    fmt = "%A"
    week = birthday.strftime(fmt)


    from datetime import timedelta
    one_day = timedelta(days = 1)

    the_other_day = one_day * 10000 + birthday

    print("生日： ", birthday, \
          "\n生日是星期： ",week,\
          "\n出生后1万天的日期是： ",the_other_day)

def use_str_date():
    import time
    
    str = 'Fri Jul 26 12:36:27 2019'
    fmt = "%a %b %d %H:%M:%S %Y"
    time1 = time.strptime(str,fmt)
    time2 = time.mktime(time1)
    time3 = time.ctime(time2)
    print("解析后的时间： ",time1,\
        "\n纪元值： ",time2,\
        "\n转换成字符串： ",time3)
    
if __name__ == '__main__':
    # write_date()
    # list_dir()
    # use_process()
    # use_date()
    use_str_date()
