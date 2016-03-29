#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21
from BaseParse import BaseParse
from pyquery import PyQuery as pq
from model.Blog import Blog


class Tickld(BaseParse):
    def parse(self):
        site_url = "http://www.tickld.com/all/new/1"
        d = pq(url=site_url)  # 抓取内容
        for article in d(".tickld-feed article"):
            b = Blog()
            article = pq(article)
            b.site = self.begin_url

            b.content_id = article.attr("id")  # 抓取ID
            b.title = article("h2").text()  # 抓取标题
            b.img = article("img").attr("src")  # 抓取显示图

            b.mp4 = article(".tickld_post_image_url").attr("data-link")  # 抓取显示图
            b.detail = article(".tickld_post_image_url").attr("href")  # 抓取详情链接
            b.type = '1' if b.mp4 is None else '2'  # 判断类型

            b.keys = article(".post-body .tags").text()
            b.keys = b.keys.replace(" ", ",")
            if b.img is None or b.img == '/images/nsfw.png':
                continue  # 跳过图片为空的异常请看

            self.b_list.append(b)


if __name__ == '__main__':
    Tickld().insert()
