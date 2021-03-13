# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:13
# @Author  : ZhangChenXu
# @File    : base_page.py
from typing import Dict, List

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import root_log


class BasePage:
    '''
    1、定义基类&公用方法
    2、定义关键字驱动
    '''

    _blacklist = [(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gu_"]')]  # 定义弹框黑名单列表
    _error_num = 0  # 定义错误计数器
    _error_max = 3  # 定义错误数上限
    _params = {}    # 定义传参字典
    _elements1 = [] # 删除前的元素列表
    _elements2 = [] # 删除后的元素列表

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 定义查找 find_element 方法
    def find(self, by, locator):
        root_log.info(f'find: by={by}, locator={locator}')
        try:
            ele = self.driver.find_element(by, locator)
            self._error_num = 0
            return ele
        except Exception as e:
            root_log.info("未找到元素")
            # 遇到异常时进行截图保存
            self.driver.get_screenshot_as_file('../testcase/result/tmp.png')
            allure.attach.file('../testcase/result/tmp.png', attachment_type=allure.attachment_type.PNG)
            # 记录错误次数
            self._error_num += 1
            if self._error_num >= self._error_max:
                raise e
            # 弹框异常处理
            for black in self._blacklist:
                eles = self.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            raise e

    # 定义查找 find_element 方法
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)


    # 定义查找点击
    def find_click(self, by, locator):
        return self.find(by, locator).click()

    # 定义输入数据
    def find_sendkeys(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    # 定义滑动查找
    def swip_click(self, text):
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}").'
                                                               'instance(0));').click()
    # 定义显示等待
    def waitfor_click(self, locator):
        locato = (MobileBy.XPATH, locator)
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locato))
        return ele.click()

    # 定义关键字驱动
    def parse_action(self, path, fun_name):
        # 读取yaml文件
        with open(path, 'r', encoding='utf-8') as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
            for step in steps:
                if step['action'] == 'find_click':
                    self.find_click(step['by'], step['locator'])
                elif step['action'] == 'swip_click':
                    self.swip_click(step['text'])
                elif step['action'] == 'find_sendkeys':
                    value: str = step['value']
                    for param in self._params:
                        value = value.replace("${" + param + "}", self._params[param])
                    self.find_sendkeys(step['by'], step['locator'], value)
                elif step['action'] == 'finds':
                    self.finds(step['by'], step['locator'])
