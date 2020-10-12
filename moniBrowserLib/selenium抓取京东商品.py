

# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)




# try:
#     chrome_options = webdriver.ChromeOptions()
#     #chrome_options.add_argument('--headless')
#     # 下一行代码是为了以开发者模式打开chrome
#     chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get("https://s.taobao.com/search?q=iPad")
#     button = browser.find_element_by_class_name('login-switch')
#     button.click()
#     button = browser.find_element_by_class_name('weibo-login')
#     button.click()
#     user_name = browser.find_element_by_name('username')
#     user_name.clear()
#     user_name.send_keys('*****') #输入微博名 需要事先绑定淘宝
#     time.sleep(1)
#     user_keys = browser.find_element_by_name('password')
#     user_keys.clear()
#     user_keys.send_keys('*****') #输入微博密码
#     time.sleep(1)
#     button = browser.find_element_by_class_name('W_btn_g')
#     button.click()
#     time.sleep(1)
#     cookies = browser.get_cookies()
#     ses=requests.Session() # 维持登录状态
#     c = requests.cookies.RequestsCookieJar()
#     for item in cookies:
#         c.set(item["name"],item["value"])
#         ses.cookies.update(c)
#         ses=requests.Session()
#         time.sleep(1)
#     print('登录成功')
# except:
#     print("登录失败")

import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote
import config
import  time

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'

KEYWORD = '铅笔'

MAX_PAGE = 100

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 30)   #等待一定的时间加载
'''建议设置时长30s以上'''
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://search.jd.com/Search?keyword=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            html = browser.page_source
            # print(html)

            # input = wait.until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form input')))
            # submit = wait.until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#form button')))
            # input.clear()
            # input.send_keys(page)
            # submit.click()
            button = browser.find_element_by_css_selector('.fp-next')
            # button.click()
            browser.execute_script("arguments[0].click();", button)    # 京东有一个弹窗覆盖，需要处理一下

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.fp-text b'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#J_goodsList ')))

        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_goodsList  .gl-warp li .gl-i-wrap .p-img a')
    print(items)
    skuList = []


# def save_to_mongo(result):
#     """
#     保存至MongoDB
#     :param result: 结果
#     """
#     try:
#         if db[MONGO_COLLECTION].insert(result):
#             print('存储到MongoDB成功')
#     except Exception:
#         print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()