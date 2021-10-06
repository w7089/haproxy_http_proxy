import requests

if __name__ == '__main__':
    r = requests.get('http://http_proxy')
    print(r.text)
