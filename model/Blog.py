#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21


class Blog(object):
    title = ""  # 标题
    type = ""  # 类型 1 图片 2 gif 3 视频
    img = ""  # 图片路径
    detail = ""  # 详情路径
    content_id = ""  # 该站点的信息唯一标识
    mp4 = ""  # gif或者视频的路径
    site = ""  # 站点名称
    keys = ""  # 关键字
    db = None

    def __repr__(self):
        tmp_str = "site = %s ,title = %s,type = %s , img = %s ,mp4=%s, detail = %s ,content_id = %s , keys =%s," \
               % (self.site, self.title, self.type, self.img,self.mp4, self.detail, self.content_id, self.keys)
        return tmp_str.encode("utf-8")
