import scrapy
from scrapy.crawler import CrawlerProcess

categories = []

class StatLeadersSpider(scrapy.Spider):
    name = "stat_leaders"
    allowed_domains = ["mlb.com"]
    start_urls = ["https://mlb.com/stats"]

    def parse(self, response):
        i = 0
        stat_i = 0
        stat2_i = 0
        stat3_i = 7
        hitting_leaders = {}
        players = response.css("tbody")
        names = players.css("tr > th > div > div.value-wrapper-Ym32XJij > div.top-wrapper-TqtRaIeD > div > a::attr(aria-label)").getall()
        teams = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").getall()

        i = 0
        ii = 1
        num = 1
        while i < len(names):
            if names[i] not in hitting_leaders:
                hitting_leaders[names[i]] = []
                hitting_leaders[names[i]].append(teams[i]) # team
                hitting_leaders[names[i]].append({"Standard" : []})
                hitting_leaders[names[i]].append({"Expanded" : []})
            hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(3)::text").get())
            hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text").get())
            hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(6) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(7) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(8) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text").get())
            #if not players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text"):
                #hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK > a::text").get())
            #else:
                #hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(9) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(10) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(11) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(12) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(13) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(14) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(15) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(16) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(17) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text").get())
            if not players.css(f"tr:nth-child({ii}) > td:nth-child(18)::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(18) > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td:nth-child(18)::text").get())
            i += 1
            ii += 1
        
        for item in ["/games", "/at-bats", "/runs", "/hits", "/doubles", "/triples", "/rbi", "/walks", "/strikeouts", "/stolen-bases", "/caught-stealing", "/batting-average", "/on-base-percentage", "/slugging-percentage", "/ops"]:
            next_page_url = "https://mlb.com/stats" + item
            yield response.follow(next_page_url, callback=self.parse)
        
        yield hitting_leaders

def run_spider():
    custom_settings = {
        #"DOWNLOAD_DELAY" : "5",
        "LOG_LEVEL" : "WARNING",
        "ROBOTSTXT_OBEY" : True,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "ITEM_PIPELINES" : { "pipelines.MlbLeadersPipeline" : 300}
    }

    process = CrawlerProcess(custom_settings)
    process.crawl(StatLeadersSpider)
    process.start()


#backup
