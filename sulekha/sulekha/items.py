# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AddressItem(scrapy.Item):
    street_address = scrapy.Field()
    address_locality = scrapy.Field()
    address_region = scrapy.Field()
    postal_code = scrapy.Field()
    land_mark = scrapy.Field()

class SulekhaItem(scrapy.Item):
    category = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field(serializer=AddressItem)
    email = scrapy.Field()
    website = scrapy.Field()
    contact_preson = scrapy.Field()
    working_hours = scrapy.Field()
    #url = scrapy.Field()

class AddressItemLoader(ItemLoader):
    default_item_class = AddressItem
    default_output_processor = TakeFirst()

class SulekhaItemLoader(ItemLoader):
    default_item_class = SulekhaItem
    default_output_processor = TakeFirst()
    
    
    
    
    
