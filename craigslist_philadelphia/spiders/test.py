from scrapy.spiders import Spider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from craigslist_philadelphia.items import CraigslistPhiladelphiaItem

class MySpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "http://philadelphia.craigslist.org/search/apa",
        "http://philadelphia.craigslist.org/search/apa?s=100",
        "http://philadelphia.craigslist.org/search/apa?s=200",
        "http://philadelphia.craigslist.org/search/apa?s=300",
        "http://philadelphia.craigslist.org/search/apa?s=400",
        "http://philadelphia.craigslist.org/search/apa?s=500",
        "http://philadelphia.craigslist.org/search/apa?s=600",
        "http://philadelphia.craigslist.org/search/apa?s=700",
        "http://philadelphia.craigslist.org/search/apa?s=800",
        "http://philadelphia.craigslist.org/search/apa?s=900",
        "http://philadelphia.craigslist.org/search/apa?s=1000",
        "http://philadelphia.craigslist.org/search/apa?s=1100",
        "http://philadelphia.craigslist.org/search/apa?s=1200",
        "http://philadelphia.craigslist.org/search/apa?s=1300",
        "http://philadelphia.craigslist.org/search/apa?s=1400",
        "http://philadelphia.craigslist.org/search/apa?s=1500",
        "http://philadelphia.craigslist.org/search/apa?s=1600",
        "http://philadelphia.craigslist.org/search/apa?s=1700",
        "http://philadelphia.craigslist.org/search/apa?s=1800",
        "http://philadelphia.craigslist.org/search/apa?s=1900",
        "http://philadelphia.craigslist.org/search/apa?s=2000",
        "http://philadelphia.craigslist.org/search/apa?s=2100",
        "http://philadelphia.craigslist.org/search/apa?s=2200",
        "http://philadelphia.craigslist.org/search/apa?s=2300",
        "http://philadelphia.craigslist.org/search/apa?s=2400",
    ]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//p[@class='row']")
        items = []
        for titles in titles:
            item = CraigslistPhiladelphiaItem()
            item["id"] = titles.xpath("@data-pid").extract()
            item["reposting_id"] = titles.xpath("@data-repost-of").extract()
            item["title"] = titles.xpath(".//a[@class='hdrlnk']/span/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            item["price"] = titles.xpath(".//span[@class='price']/text()").extract()
            item["bedrooms"] = titles.xpath(".//span[@class='housing']/text()").extract()
            item["neighborhood"] = titles.xpath(".//span[@class='pnr']/small/text()").extract()
            items.append(item)
        return items
