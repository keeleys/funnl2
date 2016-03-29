#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

import threading
import os

import util.sitemap

import parse.game9
import parse.omgif
import parse.tickld

import ConfigParser

path = os.getcwd()

cf = ConfigParser.ConfigParser()
cf.read('_config.conf')


def run():
    show_log = cf.get("db", "show_log")  # 是否显示日志
    insert_db = cf.get("db", "insert_db")  # 是否显示日志

    threading.Thread(target=lambda: parse.game9.Parse().process(show_log, insert_db)).start()
    threading.Thread(target=lambda: parse.omgif.Parse().process(show_log, insert_db)).start()
    threading.Thread(target=lambda: parse.tickld.Parse().process(show_log, insert_db)).start()


def other():
    file_path = cf.get("sitemap", "filename")
    threading.Thread(target=lambda: util.sitemap.write(file_path)).start()


if __name__ == '__main__':
    run()
    other()
