#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21
from BaseParse import BaseParse
from pyquery import PyQuery as pq
from model.Blog import Blog


class GameParse(BaseParse):

    def parse(self):
        site_url = "http://www.omgif.net/"
        d = pq(url=site_url)  # 抓取内容
        for article in d(".post-container >div"):
            b = Blog()
            article = pq(article)

            b.site = self.begin_url
            b.content_id = article.attr("id")  # 抓取ID
            b.title = article("h2").text()  # 抓取标题
            b.img = article("img").attr("src")  # 抓取显示图
            b.mp4= article("img").attr("data-gif")  # 抓取显示图
            b.detail = article(".featured-media").attr("href")  # 抓取详情链接
            b.type = '1' if b.mp4 is None else '2'  # 判断类型
            if b.img is None:
                continue  # 跳过图片为空的异常请看

            self.b_list.append(b)

if __name__ == '__main__':
    GameParse().insert()
