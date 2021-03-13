# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  上午11:18
# @Author  : ZhangChenXu
# @File    : memberinfo_page.py
from conftest import root_log
from page.base_page import BasePage
from page.delmember_page import DelmemberPage


class MemberinfoPage(BasePage):
    '''
    1、点击个人信息页右上角更多按钮
    2、点击编辑联系人
    3、跳转到编辑页
    '''
    def goto_delmember(self):
        root_log.info("进入联系人编辑/删除页")
        self.parse_action('../page/datas/memberinfopage.yml', 'goto_delmember')
        return DelmemberPage(self.driver)
        
