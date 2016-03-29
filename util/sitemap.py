#!/usr/bin/env python
# -*- coding: utf-8 -*-
from service.BlogService import BlogService


def write(path="sitemap.xml", size=1000):
    url = "http://alifunny.com/%s.html"
    bs = BlogService()
    blogs = bs.select_blog(size)
    if blogs is None:
        return
    # 这是我的一个测试文件
    file = open(path, 'w')
    file.write(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">')
    for d in blogs:
        date_time = d.get('create_time').strftime('%Y-%m-%dT%H:%M:%SZ')
        file.write('<url><loc>%s</loc><lastmod>%s</lastmod></url>'
                   % (url % d.get('id'), date_time))

    file.write('</urlset>')
    file.flush()
    file.close()
