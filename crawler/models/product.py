from types import resolve_bases
from crawler.sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector


# TODO: impl product response model


class Product():

    sitemap_name = 'product_page'

    def __init__(self, response: Response) -> None:
        self.response = response
        self.sitemap = sitemap.get(self.sitemap_name, {})

        self._values: Selector = self.response.xpath(
            self.sitemap['values_block']
        )

    @property
    def original_price(self):
        return self._values.xpath(
            self.sitemap['values']['original']
        ).get("")

    @property
    def main_price(self):
        return self._values.xpath(
            self.sitemap['values']['main']
        ).get("")


    @property
    def defer_price(self):
        return self._values.xpath(
            self.sitemap['values']['defer']
        ).get("")

# End Of File
