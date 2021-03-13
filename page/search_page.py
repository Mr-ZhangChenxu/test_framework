# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:17
# @Author  : ZhangChenXu
# @File    : search_page.py
from appium.webdriver.common.mobileby import MobileBy

from conftest import root_log
from page.base_page import BasePage
from page.memberinfo_page import MemberinfoPage


class SearchPage(BasePage):
    '''
    1、获取第一次搜索结果的数量
    2、跳转个人信息页
    '''
    def get_searchs(self, name):
        root_log.info(f"输入用户名{name}，获取删除前结果数量")
        self._params['name'] = name
        self.parse_action('../page/datas/searchpage.yml', 'get_searchs')
        self._elements1 = self.finds(MobileBy.XPATH, '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')

        return self._elements1

    def goto_memberinfo(self):
        root_log.info("点击第一个成员")
        if len(self._elements1) > 0:
            self._elements1[0].click()
        return MemberinfoPage(self.driver)



