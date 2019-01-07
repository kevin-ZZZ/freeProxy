# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
from freeProxy.items import FreeproxyItem


class KuaidailiSpider(CrawlSpider):
    name = 'kuaidaili'

    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    rules = (
        Rule(LinkExtractor(allow=r'free\/inha\/\d+'), follow=True, callback="parse_item"),
    )

    # def start_requests(self):
    #     urls = ["https://www.kuaidaili.com/free/inha/" + str(i) + "/" for i in range(1, 30)]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse_item)

    # def parse(self, response):
    #     pass

    def parse_item(self, response):
        # print(response.request.headers['User-Agent'])
        print('url是:', response.url)
        item = FreeproxyItem()
        nodes = response.xpath('//div[@id="list"]//tr')
        if len(nodes) >= 2:
            nodes = nodes[1:]
            for node in nodes:
                # 代理ip
                print("xxxxxxxxxxx", node.xpath('./td[1]/text()').extract()[0])
                item["ip_info"] = node.xpath('./td[1]/text()').extract()[0]
                # 代理端口号
                item["port_info"] = node.xpath('./td[2]/text()').extract()[0]
                # 代理采集时间
                item["time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 免费代理来源
                item["source"] = "快代理"
                # 代理类型(http还是https)
                item["type"] = node.xpath('./td[4]/text()').extract()[0]
                # 代理位置
                item["position"] = node.xpath('./td[5]/text()').extract()[0]
                # 响应时间
                item["response_speed"] = node.xpath('./td[6]/text()').extract()[0]
                # 最后验证时间
                item["verification_time"] = node.xpath('./td[7]/text()').extract()[0]
                yield item
        else:
            yield item
