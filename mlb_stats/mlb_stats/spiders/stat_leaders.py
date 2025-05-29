import scrapy

categories = []

class StatLeadersSpider(scrapy.Spider):
    name = "stat_leaders"
    allowed_domains = ["mlb.com"]
    start_urls = ["https://mlb.com/stats"]

    def parse(self, response):
        #players = response.css("tbody > tr:nth-child(1) > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").get()
        players = response.css("tbody")
        for player in players:
            yield player.css("tr > th > div > div.value-wrapper-Ym32XJij > div.top-wrapper-TqtRaIeD > div > a::attr(aria-label)").getall()
            yield player.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").getall()
        #yield players
