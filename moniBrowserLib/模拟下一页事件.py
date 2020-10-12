from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://search.jd.com/Search?keyword=ipad')

for i in range(1,100,1):
    time.sleep(1)
    button = browser.find_element_by_css_selector('.fp-next')
    print(i)
    button.click()
    # browser.delete_all_cookies()
