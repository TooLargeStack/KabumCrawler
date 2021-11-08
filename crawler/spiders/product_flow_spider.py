from scrapy.http.request import Request
from scrapy.responsetypes import Response
import scrapy

from crawler.models import Home, Category, Product


class ProductFlowSpiderSpider(scrapy.Spider):
    name = 'product_flow_spider'
    # allowed_domains = ['kabum.com.br']
    base_url = "https://www.kabum.com.br/"
    start_urls = [base_url]

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)

        self.home_model = Home
        self.category_model = Category
        self.product_model = Product

    def parse(self, response: Response):
        home = self.home_model(response)
        for category in home.categories:
            yield Request(
                url=home.get_category_link(category=category),
                callback=self.access_category,
                headers={
                    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Refer": self.base_url
                },
                meta={
                    'dont_redirect': True
                }
            )

    def access_category(self, response: Response):
        print(response.url)
        text = response.text
        category = self.category_model(response=response)
        for page in category.pages:
            pass

# End Of File