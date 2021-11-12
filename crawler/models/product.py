from types import resolve_bases
from crawler.sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector

from crawler.models.response_model import ResponseModel


# TODO: impl product response model


class Product(ResponseModel):

    name: str = 'product'
    sitemap: sitemap.product

    def __init__(self, response) -> None:
        super().__init__(response=response)
        # self.response = response
        # self.sitemap = sitemap.product

        # self._values: Selector = self.response.xpath(
        #     self.sitemap['values_block']
        # )

    @property
    def unavailable(self) -> bool:
        return bool(self.response.xpath(self.sitemap.unavailable))

    @property
    def values_block(self) -> Selector:
        return self.response.xpath(self.sitemap.values_block)

    @property
    def original_price(self):
        return self.values_block.xpath(self.sitemap.original).get('0')

    @property
    def main_price(self):
        return self.values_block.xpath(self.sitemap.main).get('0')

    @property
    def defer_price(self):
        return self.values_block.xpath(self.sitemap.defer).get('0')

# End Of File
