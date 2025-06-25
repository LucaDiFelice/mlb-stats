from twisted.internet import asyncioreactor
asyncioreactor.install()
import time

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from e_hitting_leaders import EHittingLeadersSpider
from pitching_leaders import PitchingLeadersSpider
import sys

process = CrawlerProcess()
process.crawl(EHittingLeadersSpider)
process.crawl(PitchingLeadersSpider)
process.start()


