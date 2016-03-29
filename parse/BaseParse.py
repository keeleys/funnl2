#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from service.BlogService import BlogService

class BaseParse(object):
    def __init__(self):
        self.b_list = []
        self.blogService = BlogService()
        self.begin_url = "http://9gag.com/"  # 开始抓取的路径

    def parse(self):
        print "必须实现parse"
        pass

    def show(self):
        self.parse()
        for item in self.b_list:
            print item
            print "===================="

    def insert(self):
        self.parse()
        self.blogService.save_blog_all(self.b_list)
        pass


if __name__ == '__main__':
    BaseParse().insert()
