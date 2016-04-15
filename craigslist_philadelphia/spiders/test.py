from scrapy.spiders import Spider
from scrapy.selector import Selector
from craigslist_philadelphia.items import CraigslistPhiladelphiaItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraigslistPhiladelphiaItem()
            item["id"] = titles.xpath("a/@data-id").extract()
            item["title"] = titles.xpath("a/span/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return items

