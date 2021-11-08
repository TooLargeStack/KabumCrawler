from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings

from crawler.spiders.product_flow_spider import ProductFlowSpiderSpider


class Runner(CrawlerProcess):

    def __init__(self, spider:CrawlSpider, settings=None, install_root_handler=True):
        super().__init__(settings=settings, install_root_handler=install_root_handler)
        self._spider = spider

    def execute(self):
        self.crawl(crawler_or_spidercls=self._spider)
        self.start()

if __name__ == "__main__":
    runner = Runner(spider=ProductFlowSpiderSpider, settings=get_project_settings())
    runner.execute()

# End Of File