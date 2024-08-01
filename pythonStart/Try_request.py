import requests

r = requests.get('https://www.douban.com/search', params={
    'q': 'python', 'cat': '1001'
})

# print(r.url)
# 检测编码 utf-8 
# print(r.encoding)
# 获取响应头
# print(r.headers)
