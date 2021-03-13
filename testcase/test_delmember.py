# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-13  下午3:37
# @Author  : ZhangChenXu
# @File    : test_delmember.py
from page.app import App


class TestDelmember():
    def setup(self):
        self.app = App()

    def test_delmember(self):
        page = self.app.start().goto_mainpage().goto_addresslist().goto_search()
        # 获取删除成员前结果页同名成员列表
        ele1 = page.get_searchs(name='a001')
        # 获取删除成员后结果页同名成员列表
        ele2 = page.goto_memberinfo().goto_delmember().delmember().results()
        # 判断前后列表长度之差是否为1，从而判定是否删除成功
        assert len(ele1) - len(ele2) == 1
