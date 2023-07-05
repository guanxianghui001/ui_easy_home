# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome
@File ：convert_codes.py
@Author ：huxueyan
@Date ：2023/7/5 15:32
"""
from selenium.webdriver.common.by import By


def c_element_location_type(location_type):
    if location_type == '201':
        result = 'By.ID'
        return result
    elif location_type == '202':
        result = 'By.NAME'
        return result
    elif location_type == '203':
        result = 'By.CLASS_NAME'
        return result
    elif location_type == '204':
        result = 'By.TAG_NAME'
        return result
    elif location_type == '205':
        result = 'By.LINK_TEXT'
        return result
    elif location_type == '206':
        result = 'By.XPATH'
        return result
    elif location_type == '207':
        result = 'By.CSS_SELECTOR'
        return result