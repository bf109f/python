import requests


def request_html(url):
    html = requests.get(url, headers=headers)


if __name__ == '__main__':
    headers = {

    }
    urls = ['{}'.format(str(i)) for i in range(1, 10, 2)]
    print(urls)