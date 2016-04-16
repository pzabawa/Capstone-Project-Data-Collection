# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class CraigslistPhiladelphiaItem(Item):
    id = Field()
    reposting_id = Field()
    title = Field()
    link = Field()
    price = Field()
    bedrooms = Field()
    neighborhood = Field()
