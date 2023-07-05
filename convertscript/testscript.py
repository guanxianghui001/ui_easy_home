from selenium import webdriver
from selenium.webdriver.common import by
from app.utils.assert_util import screenshot, assert_element_exist
driver= webdriver.Chrome()
name = '场景名'
print(name)
def test_1():
    driver.get('https://www.baidu.com')
    screenshot(driver, '首页_1.png')
    assert_element_exist(driver, '201', 'kw')
def test_2():
    driver.find_element_by_id('kw').send_keys('胡雪岩')
    screenshot(driver, '首页_2.png')
def exit():
    driver.quit()
if __name__ == '__main__':
    test_1()
    test_2()
    exit()