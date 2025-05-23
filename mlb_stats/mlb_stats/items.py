# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MlbStatsItem(scrapy.Item):
    player_names = scrapy.Field()
    path_links = scrapy.Field()
