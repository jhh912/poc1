import argparse
import os

# os.remove("1.py")  #删除文件
# os.rename("1.txt","2.txt")   #修改文件名
# print(os.name) #输出当前的操作系统
# prinit(os.system("whoami"))
# print(os.path.isdir("E:/XA信思"))
# print(os.path.abspath("2.txt"))
# print(os.path.join("E:/XA信思/课件知识点/第三阶段/第二天/1.内置模块.md","ccc","bbbb"))
# url="http://www.baidu.com"
# payload = 'a/readme.txt'
# print(os.path.join(url, payload))


# import time
# print(time.time())  #1724922791.792511  时间戳 1970第一台计算机
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# time.sleep(5)  #常用于延时注入
# print(1)


# import json
# dic={'name':'admin','age':18,'sex':'male'}
# print(type(dic))
# dic1=json.dumps(dic)
# print(type(json.loads(dic1)))


# import pickle
# dic={'name':'alvin','age':23,'sex':'male'}
# print(type(pickle.dumps(dic)))
# c = pickle.dumps(dic)
# print(type(pickle.loads(c)))

# import base64
# str = '1.py'
# str1 = base64.b64encode(str.encode('UTF-8'))
# print(type(str1.decode('UTF-8')))

# fd = open('password.txt', 'w', encoding='utf-8')
# fd.write('admin\n')
# fd.write('admin1\n')
# fd.write('admin2\n')
# fd.write('admin3\n')

# import base64
# with open('username.txt','r',encoding='utf-8') as f:
#     for username in f.readlines():
#         with open('password.txt','r',encoding='utf-8') as f1:
#             for password in f1.readlines():
#                 ccc = username.strip()+":"+password.strip()
#                 #print(ccc)
#                 ddd = base64.b64encode(ccc.encode('utf-8'))
#                 with open('result.txt','a',encoding='utf-8') as f2:
#                     f2.write(ddd.decode('utf-8')+'\n')


# import urllib.parse
# keyword = "后台"
#
# k2 = urllib.parse.quote(keyword)
# print(urllib.parse.unquote(k2))



# import sys
# print(sys.argv)
# if sys.argv[-1] == 'www.baidu.com':
#     print("hahaah")


# try:
#     with open(4.txt, 'r',encoding='utf-8') as f:
#         f.readlines()
# except Exception as e:
#     print(e)
# print(1)


# import time
# from multiprocessing.dummy import Pool
#
# def poc(url):
#     while True:
#         print(url)
#         time.sleep(url)
# target=[1,2,3,4,5,6,7,8,9,10]
#
# mp = Pool(20)
# mp.map(poc, target)
# mp.close()
# mp.join()


#最后一个库 argparse

#处理命令含参数的 好用
#import argparse

#第一步，实例化
#parser = argparse.ArgumentParser(description="这是我的第一个脚本")
#第二部添加参数
#parser.add_argument("-u","--url",dest='url',type=str,help="Please input url")
#调用
#args = parser.parse_argsO()
#
#print(args.url)



import argpare



