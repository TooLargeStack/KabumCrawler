from scrapy.http.request import Request
from scrapy.responsetypes import Response
import scrapy

from models import Home, Category, Product


class ProductFlowSpiderSpider(scrapy.Spider):
    name = 'product_flow_spider'
    # allowed_domains = ['kabum.com.br']
    start_urls = ['http://kabum.com.br/']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)

        self.home_model = Home
        self.category_model = Category
        self.product_model = Product

    def parse(self, response: Response):
        home = self.home_model(response)
        for category_link in home.categories_links:
            yield Request(
                url=category_link,
                callback=self.access_category
            )

    def access_category(self, response: Response):
        pass
