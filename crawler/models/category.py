from logging import Logger
from os import link
from typing import List
from urllib.parse import urlencode

from crawler.sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector

from crawler.models.response_model import ResponseModel


class Category(ResponseModel):

    name: str = 'category'
    sitemap: sitemap.category

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def pages(self) -> List[Selector]:
        return self.response.xpath(self.sitemap.pages)
    
    def get_pages_links(self) -> List[str]:
        # import ipdb; ipdb.set_trace()
        # links = []
        # for page_number in range(1, int(self.pages.pop().get()) + 1):
        #     # import ipdb; ipdb.set_trace()
        #     parameters = urlencode({"page_number": page_number})
        #     # print(f"{self.response.url}?{parameters}")
        #     links.append(f"{self.response.url}?{parameters}")
        return [
            f"{self.response.url}?{urlencode({'page_number': page_number})}"
            for page_number in range(1, int(self.pages.pop().get()) + 1)
        ]
        # import ipdb; ipdb.set_trace()
        # return links

    @property
    def products(self) -> List[Selector]:
        return self.response.xpath(self.sitemap.products)

    def get_product_link(self, product: Selector) -> str:
        return self.response.urljoin(
            product.xpath(
                self.sitemap.products_links
            ).get(
                default=''
            )
        )

    def get_products_links(self) -> List[str]:
        return [
            product.xpath(self.sitemap.products_links).get('')
            for product in self.products
        ]

# End Of File
