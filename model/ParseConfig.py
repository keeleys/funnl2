#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21


class ParseConfig(object):
    referer= None  # header的抓取参数
    begin_url = None  # 开始抓取的URL
    container = None  # 列表的主要函数

    type = "1"  # 1,2,3
    title = None
    img = None
    site = None
    content_id = None
    detail = None

    def __init__(self):
        pass

if __name__ == '__main__':
    pass