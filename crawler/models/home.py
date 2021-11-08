from typing import Union, List

from crawler.sitemap import sitemap
from scrapy.responsetypes import Response
from scrapy.selector import Selector

from crawler.models.response_model import ResponseModel


class Home(ResponseModel):
    
    name = 'home'

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def categories(self) -> List[Selector]:
        return self.response.xpath(self.sitemap.categories)

    def get_category_link(self, category: Selector) -> str:
        return self.response.urljoin(
            category.xpath(
                self.sitemap.link
            ).get(
                default=''
            )
        )

    def get_category_name(self, category: Selector) -> str:
        return category.xpath(self.sitemap.name).get(default='')

# End Of File