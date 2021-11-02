import scrapy


class UpdateProductProcessSpider(scrapy.Spider):
    name = 'update_product_process'
    # allowed_domains = ['kabum.com.br']
    # start_urls = ['http://kabum.com.br/']

    def parse(self, response):
        pass
