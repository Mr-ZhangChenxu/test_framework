# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:13
# @Author  : ZhangChenXu
# @File    : main_page.py
from conftest import root_log
from page.addresslist_page import AddresslistPage
from page.base_page import BasePage


class MainPage(BasePage):
    '''
    1、跳转到通讯录界面
    '''
    def goto_addresslist(self):
        root_log.info("点击通讯录")
        self.parse_action('../page/datas/mainpage.yml', 'goto_addresslist')
        return AddresslistPage(self.driver)

