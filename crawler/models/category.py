from logging import Logger
from typing import List

from sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector


class Category:

    sitemap_name = 'category'

    def __init__(self, response: Response) -> None:
        self.response = response
        self.sitemap = sitemap.get(self.sitemap_name, {})

        self._values: Selector = self.response.xpath(
            self.sitemap['values_block']
        )

    @property
    def categories(self) -> List[Selector]:
        return self.response.xpath(
            self.sitemap['categories']
        )

# End Of File