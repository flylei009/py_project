import requests,re,os
from hashlib import md5
from selenium import webdriver

def get_cookies(url):
    str=''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for i in browser.get_cookies():
        try:
            name=i.get('name')
            value=i.get('value')
            str=str+name+'='+value+';'
        except ValueError as e:
            print(e)
    return str

def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1602031859621',
        '_signature': 'WQuP9AAgEBCfXDZ5DxizslkKzuAAAZ33pdVFcrAkrwLEF9lYSOxgNNXM6.tqoItXB9BIZqZveJtxuiYRBCVfkRJuacPPCFZSO3qv8kR9sOE9tiq3.dYK1zmgcIQn9ahmYuy'


    }
    url='https://www.toutiao.com/api/search/content/'
    try:
        r=requests.get(url,params=params,headers=headers)
        if r.status_code==200:
            return r.json()
        else:
            print('requests get_page error!')
    except requests.ConnectionError:
        return None

def get_images(json):
    data=json.get('data')
    if data:
        for i in data:
            if i.get('title'):
                title=re.sub('[\t]','',i.get('title'))
                url=i.get('article_url')
                if url:
                    r=requests.get(url,headers=headers)
                    if r.status_code==200:
                        images_pattern = re.compile('JSON.parse\("(.*?)"\),\n', re.S)
                        result = re.search(images_pattern, r.text)
                        if result:
                            b_url='http://p3.pstatp.com/origin/pgc-image/'
                            up=re.compile('url(.*?)"width',re.S)
                            results=re.findall(up,result.group(1))
                            if results:
                                for result in results:
                                    yield {
                                        'title':title,
                                        'image':b_url+re.search('F([^F]*)\\\\",',result).group(1)
                                    }
                        else:
                            images = i.get('image_list')
                            for image in images:
                                origin_image = re.sub("list.*?pgc-image", "large/pgc-image",
                                                      image.get('url'))  # 改成origin/pgc-image是原图
                                yield {
                                    'image': origin_image,
                                    'title': title
                                }

def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path) # 生成目录文件夹
    try:
        resp = requests.get(item.get('image'))
        if requests.codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e,'none123')

def main(offset):
    a = get_page(offset)
    for i in get_images(a):
        save_image(i)

# cookies = get_cookies('https://www.toutiao.com')
headers = {
    # 'cookie': cookies,
    'cookie': 'tt_webid=6880672974127564301; s_v_web_id=verify_kfyo7l8b_VdMFoBc2_8xcy_4Pn2_9vCb_USXAeppEXbTM; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6880672974127564301; ttcid=c32df3a0c0d84961957f31f9cba7b4a728; MONITOR_WEB_ID=05b893d9-6139-40cb-ba8a-c35081a05050; __tasessionId=or1nsqoas1602031533534; csrftoken=439a900479e8cdcad9d7fd8faa7f479d; tt_scid=ead1iRjYLTytYpztoxiTsEcE9NwezzUJIeWRP6nGm2lnBBCW4jVVh.fq4IZfK1Gx9123',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
}

if __name__=='__main__':
    main(0)
    #p.map(main,[0]) #之所以不用Pool多进程是因为目前还没有办法实现跨进程共享Cookies
    #map(main,[x*20 for x in range(3)]) map没有输出，不知道为什么

    # for i in [x*20 for x in range(3)]:
    #     main(i)
