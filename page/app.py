# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:13
# @Author  : ZhangChenXu
# @File    : app.py
from appium import webdriver

from page.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):
    '''
    1、配置capability
    2、跳转到主页
    '''
    _packge = 'com.tencent.wework'
    _activity = '.launch.WwMainActivity'

    def start(self):
        # 如果driver为None，生成driver
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = self._packge
            desired_caps['appActivity'] = self._activity
            # 不清空缓存启动App
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
            # 生成driver后立刻设置隐式等待
            self.driver.implicitly_wait(5)

        else:
            self.driver.start_activity(self._packge, self._activity)

        return self

    def goto_mainpage(self):
        return MainPage(self.driver)