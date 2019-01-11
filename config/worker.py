# coding:utf-8
# -*- coding: utf-8 -*-
# @Time    : 1/9/19 3:25 PM
# @Author  : Kevin
# @Site    : 
# @File    : worker.py.py
# @Descri  : 
# @Software: pycharm


from __future__ import absolute_import
from config.common import *

BACKEND = 'frontera.contrib.backends.hbase.HBaseBackend'

MAX_NEXT_REQUESTS = 2048
NEW_BATCH_DELAY = 5.0

HBASE_THRIFT_HOST = '10.1.220.8'  # HBase Thrift server host and port
HBASE_THRIFT_PORT = 9090
# HBASE_THRIFT_PORT = 2181
