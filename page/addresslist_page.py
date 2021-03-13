# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:14
# @Author  : ZhangChenXu
# @File    : addresslist_page.py
from conftest import root_log
from page.base_page import BasePage
from page.search_page import SearchPage


class AddresslistPage(BasePage):
    '''
    1、跳转到搜索界面
    '''
    def goto_search(self):
        root_log.info("点击搜索")
        self.parse_action('../page/datas/addresslistpage.yml','goto_search')
        return  SearchPage(self.driver)
