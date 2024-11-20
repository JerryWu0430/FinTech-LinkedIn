import requests

proxies = {
    'http': 'http://your_proxy:port',
    'https': 'http://your_proxy:port',
}

response = requests.get('http://example.com/api', proxies=proxies)
print(response.text)
