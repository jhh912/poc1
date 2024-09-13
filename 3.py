# import requests
#
# url = "https://ts1.cn.mm.bing.net/th/id/R-C.34a129d338121fbd429801e1a677c4fc?rik=ABc6ki0tw0XlHA&riu=http%3a%2f%2fent.qingdaonews.com%2fimages%2f2020-09%2f11%2ff30b916c-01f2-47f1-ab3e-0464a7bcfff7.jpg&ehk=NHdBk9da%2f0LELZ6uz%2fY2UhJKKvj5%2fjTkIAADlYIIlEk%3d&risl=&pid=ImgRaw&r=0"
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
# }
# response = requests.get(url=url, headers=headers)
# with open('女神.png', 'wb') as f:
#     f.write(response.content)


# import requests
# requests.packages.urllib3.disable_warnings()
# url = 'https://121.231.208.166:8443/'
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
# }
# response = requests.get(url=url, headers=headers, verify=False)
# print(response.text)


# import requests
# url = 'https://www.youtube.com/s/desktop/eb72fb02/img/favicon.ico'
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
# }
#  proxies = {
#      'http': 'http://127.0.0.1:7890',
#      'https': 'http://127.0.0.1:7890'
#  }
#  try:
#      response = requests.get(url=url, headers=headers,timeout=5, proxies=proxies)
#      print(response.content)
#      with open('youtobe.ico','wb') as f:
#          f.write(response.content)
# except Exception as e:
#      print(e)
# print(response.status_code)
# print(1)

