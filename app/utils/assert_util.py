# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome
@File ：assert_util.py
@Author ：huxueyan
@Date ：2023/7/5 15:32
"""
import base64
import os

from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException

from app.conf import config
from app.utils.convert_codes import c_element_location_type
from app.utils.custom_exception import ArgumsErrException
from selenium.webdriver.common.by import By
ss_dir = config.screenshot_dir

def screenshot(driver, pngname):
    """实现截图
    pngname: 图片名称，场景_步骤顺序即可
    """
    screenshot_dir = os.path.join(os.path.dirname(__file__), ss_dir)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    base64_data = driver.get_screenshot_as_base64()
    png_data = base64.b64decode(base64_data)
    filename = os.path.join(screenshot_dir, pngname)
    with open(filename,'wb') as f:
        f.write(png_data)

def assert_element_exist(driver, element_location_type, element_location, msg=None):
    """
    断言元素存在，断言成功返回True，断言失败返回False
    :key driver: 浏览器对象
    :key element_location_type:元素定位方式（直接传码值即可）
    :key element_location: 元素定位内容
    :key msg:错误信息
    """
    # 响应结果
    flag = None
    location_type = c_element_location_type(element_location_type)
    type_list = ['By.ID','By.NAME','By.CLASS_NAME','By.TAG_NAME','By.LINK_TEXT','By.XPATH','By.CSS_SELECTOR']
    try:
        if location_type in type_list:
            driver.find_element(eval(location_type), element_location)
        else:
            raise ArgumsErrException('9999', '元素定位类型错误，请查看码值是否正确，码值支持范围为201-207')
    except ArgumsErrException as e:
        print('断言出错啦！')
        print(e)
        flag = None
    except NoSuchElementException as e:
        if msg == None:
            print('断言失败，元素不存在！')
        else:
            print(msg)
        print(e)
        flag = False
    except ElementNotVisibleException as e:
        if msg == None:
            print('断言失败，元素不存在！')
        else:
            print(msg)
        print(e)
        flag = False
    else:
        print('断言成功，元素存在！')
        flag = True
    return flag

def assert_element_noexist(driver, element_location_type, element_location, msg=None):
    """
    断言元素不存在，断言成功返回True，断言失败返回False
    :key driver: 浏览器对象
    :key element_location_type:元素定位方式（直接传码值即可）
    :key element_location: 元素定位内容
    :key msg:错误信息
    """
    # 响应结果
    flag = None
    location_type = c_element_location_type(element_location_type)
    type_list = ['By.ID','By.NAME','By.CLASS_NAME','By.TAG_NAME','By.LINK_TEXT','By.XPATH','By.CSS_SELECTOR']
    try:
        if location_type in type_list:
            driver.find_element(eval(location_type), element_location)
        else:
            raise ArgumsErrException('9999','元素定位类型错误，请查看码值是否正确，码值支持范围为201-207')
    except ArgumsErrException as e:
        print('断言出错啦！')
        print(e)
        flag = None
    except NoSuchElementException as e:
        print('断言成功，元素不存在！')
        print(e)
        flag = True
    except ElementNotVisibleException as e:
        print('断言成功，元素不存在！')
        print(e)
        flag = True
    else:
        if msg == None:
            print('断言失败，元素存在！')
        else:
            print(msg)
        flag = False
    return flag

def assert_element_equal_expecttext(driver, element_location_type, element_location, expect_text, msg=None):
    """
    断言元素textContent属性值与期望值相等，断言成功返回True，断言失败返回False
    :key driver: 浏览器对象
    :key element_location_type:元素定位方式（直接传码值即可）
    :key element_location: 元素定位内容
    :key expect_text:期望值
    :key msg:错误信息
    """
    # 响应结果
    flag = None
    location_type = c_element_location_type(element_location_type)
    type_list = ['By.ID','By.NAME','By.CLASS_NAME','By.TAG_NAME','By.LINK_TEXT','By.XPATH','By.CSS_SELECTOR']
    try:
        if location_type in type_list:
            element = driver.find_element(eval(location_type), element_location)
            ele_text = element.get_attribute('textContent')
            if ele_text == expect_text:
                flag = True
                print('断言成功，元素的textContent与期望值相等！')
            else:
                flag = False
                if msg == None:
                    print('元素的实际textContent是 %s,而期望值是 %s,两者不相等！' % (ele_text, expect_text))
                else:
                    print(msg)
        else:
            raise ArgumsErrException('9999','元素定位类型错误，请查看码值是否正确，码值支持范围为201-207')
    except ArgumsErrException as e:
        print('断言出错啦！')
        print(e)
        flag = None
    return flag

def assert_element_noequal_expecttext(driver, element_location_type, element_location, expect_text, msg=None):
    """
    断言元素textContent属性值与期望值不相等，断言成功返回True，断言失败返回False
    :key driver: 浏览器对象
    :key element_location_type:元素定位方式（直接传码值即可）
    :key element_location: 元素定位内容
    :key expect_text:期望值
    :key msg:错误信息
    """
    # 响应结果
    flag = None
    location_type = c_element_location_type(element_location_type)
    type_list = ['By.ID', 'By.NAME', 'By.CLASS_NAME', 'By.TAG_NAME', 'By.LINK_TEXT', 'By.XPATH', 'By.CSS_SELECTOR']
    try:
        if location_type in type_list:
            element = driver.find_element(eval(location_type), element_location)
            ele_text = element.get_attribute('textContent')
            if ele_text != expect_text:
                flag = True
                print('断言成功，元素的textContent与期望值不相等！')
            else:
                flag = False
                if msg == None:
                    print('断言失败，元素的textContent与期望值相等！')
                else:
                    print(msg)
        else:
            raise ArgumsErrException('9999','元素定位类型错误，请查看码值是否正确，码值支持范围为201-207')
    except ArgumsErrException as e:
        print('断言出错啦！')
        print(e)
        flag = None
    return flag











