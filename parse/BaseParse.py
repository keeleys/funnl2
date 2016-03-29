#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from service.BlogService import BlogService


class BaseParse(object):
    def __init__(self):
        self.b_list = []
        self.blogService = BlogService()
    def parse(self):
        print "必须实现parse"
        pass

    def show(self):
        for item in self.b_list:
            print item
            print "===================="

    def process(self, show_log=False, insert_db=True):
        self.parse()

        if show_log:
            self.show()
        if insert_db:
            self.blogService.save_blog_all(self.b_list)