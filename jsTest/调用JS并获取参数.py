# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# import time
#
#
# browser = webdriver.Chrome()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
#
#
# browser.get('http://car.bitauto.com/changancs75plus/m143938/peizhi/')
# wait = WebDriverWait(browser, 30)  # 等待一定的时间加载
# html = browser.page_source
# print(html)
# # returnJson = browser.execute_script("return carCompareJson")
# # print(returnJson)


import re

from bs4 import BeautifulSoup

data = """
<script>
var a = 'hello';
var b = 'hi';
var c = 'halo';
</script>
"""
soup = BeautifulSoup(data, "html.parser")
pattern = re.compile(r"var a = '(.*?)';$", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)
print(script)

