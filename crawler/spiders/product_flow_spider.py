import scrapy


class ProductFlowSpiderSpider(scrapy.Spider):
    name = 'product_flow_spider'
    allowed_domains = ['kabum.com.br']
    start_urls = ['http://kabum.com.br/']

    def parse(self, response):
        pass
