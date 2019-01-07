# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeproxyItem(scrapy.Item):
    # 代理ip
    ip_info = scrapy.Field()
    # 代理端口号
    port_info = scrapy.Field()
    # 代理采集时间
    time = scrapy.Field()
    # 免费代理来源
    source = scrapy.Field()
    # 代理类型(http还是https)
    type = scrapy.Field()
    # 代理位置
    position = scrapy.Field()
    # 响应时间
    response_speed = scrapy.Field()
    # 最后验证时间
    verification_time = scrapy.Field()
