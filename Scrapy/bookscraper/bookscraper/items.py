# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def  serializer_price(value):
    return f'${str(value)}'


'''Items when we generate scrapy project, it gen. items.py files where we put these items.
It help us define what we want in block of data that we r scraping or returning.
priv we were using yield but now will use items.py and declear specific items in there.

The Field class is just an alias to the built-in dict class and doesn't provide any extra functionality or attributes. 
++In other words, Field objects are plain-old Python dicts. A separate class is used to support the item declaration syntax based on class attributes.
'''
class BookItem(scrapy.Item):
    url =scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax= scrapy.Field()
    price_incl_tax=scrapy.Field()
    tax=scrapy.Field()
    availability=scrapy.Field()
    num_reviews=scrapy.Field()
    stars=scrapy.Field()
    category=scrapy.Field()
    description=scrapy.Field()
    price=scrapy.Field()

