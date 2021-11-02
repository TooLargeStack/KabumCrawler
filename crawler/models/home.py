from typing import Union

from sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector


class Home:
    
    sitemap_name = 'home_page'

    def __init__(self, response: Union[Response, Response]) -> None:
        self.response = response
        self.sitemap = sitemap.get(self.sitemap_name, {})

        self._values: Selector = self.response.xpath(
            self.sitemap['values_block']
        )

    @property
    def categories(self) -> Selector:
        pass

    @property
    def categories_links(self) -> str:
        pass

    @property
    def category_name(self) -> str:
        pass

# End Of File