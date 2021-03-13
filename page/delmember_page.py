# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:18
# @Author  : ZhangChenXu
# @File    : delmember_page.py
from appium.webdriver.common.mobileby import MobileBy

from conftest import root_log
from page.base_page import BasePage


class DelmemberPage(BasePage):
    '''
    1、滑动查找删除按钮并点击
    2、获取删除后页面显示数量
    '''
    def delmember(self):
        root_log.info("删除联系人")
        self.parse_action('../page/datas/delmemberpage.yml', 'delmember')

        return self
    def results(self):
        root_log.info("获取删除后的结果数量")
        self._elements2 = self.finds(MobileBy.XPATH,
                                     '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')
        return self._elements2