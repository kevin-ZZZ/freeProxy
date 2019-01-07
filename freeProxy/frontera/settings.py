# coding:utf-8
# -*- coding: utf-8 -*-
# @Time    : 1/7/19 4:41 PM
# @Author  : Kevin
# @Site    : 
# @File    : settings.py
# @Descri  : 
# @Software: pycharm

from freeProxy.settings import SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

# print("xxxxxxxx有调用到frontera框架！")
SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
})

DOWNLOADER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
})

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

HTTPCACHE_ENABLED = False  # Turns off disk cache, which has low hit ratio during broad crawls
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 120
RETRY_ENABLED = False  # Retries can be handled by Frontera itself, depending on crawling strategy
DOWNLOAD_MAXSIZE = 10 * 1024 * 1024  # Maximum document size, causes OOM kills if not set
LOGSTATS_INTERVAL = 10  # Print stats every 10 secs to console

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25  # Any small enough value, it will be adjusted during operation by averaging
# with response latencies.
RANDOMIZE_DOWNLOAD_DELAY = False

# concurrency
CONCURRENT_REQUESTS = 256  # Depends on many factors, and should be determined experimentally
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.0
