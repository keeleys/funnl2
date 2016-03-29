#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

import threading
import os
import parse.game9
import parse.omgif
import parse.tickld

path = os.getcwd()


def run():
    show_log = True  # 是否显示日志
    insert_db = True  # 是否插入数据库

    threading.Thread(target=lambda: parse.game9.Parse().process(show_log, insert_db)).start()
    threading.Thread(target=lambda: parse.omgif.Parse().process(show_log, insert_db)).start()
    threading.Thread(target=lambda: parse.tickld.Parse().process(show_log, insert_db)).start()


if __name__ == '__main__':
    run()