#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

from util.MysqlKit import DB


class BlogService(object):
    db = None

    def __init__(self):
        self.db = DB('localhost', 3306, 'root', '123456', 'funny')

    def save_blog(self, blog):
        self.db.update(u"insert into blog(title,type,img,site,detail,content_id,mp4,create_time,check_num,html_keys)"
                       u" VALUES(%s,%s,%s,%s,%s,%s,%s,now(),0,%s)",
                       (blog.title, blog.type, blog.img, blog.site,
                        blog.detail, blog.content_id, blog.mp4, blog.keys))

    def save_blog_all(self, blog_list):
        blist = []
        for blog in blog_list:
            blist.append((blog.title, blog.type, blog.img, blog.site,
                        blog.detail, blog.content_id, blog.mp4, blog.keys))

        self.db.update_all(u"insert into blog(title,type,img,site,detail,content_id,mp4,create_time,check_num,html_keys)"
                           u" VALUES(%s,%s,%s,%s,%s,%s,%s,now(),0,%s)", blist)

    def has_blog(self, blog):
        data = self.db.query("select * from blog where site = %s and content_id = %s",
                             (blog.site, blog.content_id))
        return len(data) > 0


if __name__ == '__main__':
    pass
