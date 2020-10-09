from selenium import webdriver

# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()

# print("切换frame----------------------------------------------------------------------------------")
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


# print("延时等待----------------------------------------------------------------------------------")
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(100000)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)


# print("前进后退----------------------------------------------------------------------------------")
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


# print("cookie 操作----------------------------------------------------------------------------------")
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

print("选项卡管理----------------------------------------------------------------------------------")
import time
from selenium import webdriver

browser = webdriver.Chrome()


browser.get('https://www.baidu.com')
browser.execute_script('window.open()')   # 打开一个新的选项卡
#
print(browser.window_handles)

browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
# time.sleep(1)

browser.execute_script('window.open()')    # 打开一个新的选项卡
# print(browser.window_handles)
browser.switch_to_window(browser.window_handles[2])   #  在第三个选项卡打开一个新的网页
browser.get('https://python.org')