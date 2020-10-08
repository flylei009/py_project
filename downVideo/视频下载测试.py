import requests

hd = {
    # 'Connection': 'keep-alive',
    'Host': 'www.xvideos.com:443',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Referer': 'https://www.xvideos.com/video30753249/_.mp4'
}

print("开始下载")
url = 'https://www.xvideos.com/video30753249/_.mp4'
r = requests.get(url, headers=hd, stream=True)

with open('test.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)

print("下载结束")