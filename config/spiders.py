# coding:utf-8
# -*- coding: utf-8 -*-
# @Time    : 1/9/19 3:27 PM
# @Author  : Kevin
# @Site    : 
# @File    : spiders.py
# @Descri  : 
# @Software: pycharm


from __future__ import absolute_import
from config.common import *

BACKEND = 'frontera.contrib.backends.remote.messagebus.MessageBusBackend'
KAFKA_GET_TIMEOUT = 0.5
LOCAL_MODE = False  # by default Frontera is prepared for single process mode