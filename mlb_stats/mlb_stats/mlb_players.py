import scrapy
from scrapy.crawler import CrawlerProcess
from items import MlbStatsItem

class MlbPlayersSpider(scrapy.Spider):
    name = "mlb_players"
    allowed_domains = ["www.baseball-reference.com"]
    start_urls = ["https://www.baseball-reference.com/players/a"]

    def parse(self, response):
        players = response.css("div.section_content#div_players_")
        mlb_stats = MlbStatsItem()
        names = []
        links = []
        for player in players:
            names.extend(player.css("p a::text").getall())
            links.extend(player.css("p a::attr(href)").getall())
            #yield {
                #"names" : player.css("p a::text").getall(),
                #"path_links" : player.css("p a::attr(href)").getall()
            #}
        mlb_stats["player_names"] = names
        mlb_stats["path_links"] = links

        yield mlb_stats

        #for letter in "bcdefghijklmnopqrstuvwxyz":
        for letter in "zyxwuvtsrqponmlkjihgfedcb":
            next_page_url = "https://www.baseball-reference.com/players/" + letter
            yield response.follow(next_page_url, callback=self.parse)


def run_spider():
    custom_settings = {
        #"FEEDS" : { "raw_data.csv": { "format": "csv",}},
        "LOG_LEVEL" : "WARNING",
        "DOWNLOAD_DELAY" : "5",
        "ROBOTSTXT_OBEY" : True,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "ITEM_PIPELINES" : { "pipelines.MlbStatsPipeline" : 300 }
    }

    process = CrawlerProcess(custom_settings)
    process.crawl(MlbPlayersSpider)
    process.start()
