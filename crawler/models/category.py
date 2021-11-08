from logging import Logger
from typing import List

from crawler.sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector

from crawler.models.response_model import ResponseModel


class Category(ResponseModel):

    name = 'category'

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def pages(self) -> List[Selector]:
        return self.response.xpath(self.sitemap.pages)
        
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

# End Of File