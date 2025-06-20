import scrapy
from scrapy.crawler import CrawlerProcess

class PitchingLeadersSpider(scrapy.Spider):
    name = "pitching_leaders"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/stats/pitching"]
    category_links = ["/wins", "/losses", "/era", "/games",
                      "/games-started", "/complete-games",
                      "/shutout", "/saves", "/save-opportunities",
                      "/innings-pitched", "/hits-allowed",
                      "/runs-allowed", "/earned-runs", "/home-runs-allowed",
                      "hit-batsmen", "/walks-allowed", "/pitching",
                      "/whip", "/avg-allowed-by-the-pitcher"]

    def parse(self, response):
        if response.url in "https://www.mlb.com/stats/pitching":
            for link in self.category_links:
                next_page_url = "https://www.mlb.com/stats/pitching" + link
                yield response.follow(next_page_url, callback=self.parse)
        else:
            i = 0
            ii = 1
            pitching_leaders = {}
            players = response.css("tbody")
            names = players.css("tr > th > div > div.value-wrapper-Ym32XJij > div.top-wrapper-TqtRaIeD > div > a::attr(aria-label)").getall()
            teams = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").getall()
            w = []
            l = []
            era = []
            g = []
            gs = []
            cg = []
            sho = []
            sv = []
            svo = []
            ip = []
            h = []
            r = []
            er = []
            hr = []
            hb = []
            bb = []
            so = []
            whip = []
            avg = []
            while i < len(names):
                w.append(players.css(f"tr:nth-child({ii}) > td:nth-child(3)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text"):
                    l.append(players.css(f"tr:nth-child({ii}) > td:nth-child(4) > a::text").get())
                else:
                    l.append(players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text"):
                    era.append(players.css(f"tr:nth-child({ii}) > td:nth-child(5) > a::text").get())
                else:
                    era.append(players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text"):
                    g.append(players.css(f"tr:nth-child({ii}) > td:nth-child(6) > a::text").get())
                else:
                    g.append(players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text"):
                    gs.append(players.css(f"tr:nth-child({ii}) > td:nth-child(7) > a::text").get())
                else:
                    gs.append(players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text"):
                    cg.append(players.css(f"tr:nth-child({ii}) > td:nth-child(8) > a::text").get())
                else:
                    cg.append(players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text"):
                    sho.append(players.css(f"tr:nth-child({ii}) > td:nth-child(9) > a::text").get())
                else:
                    sho.append(players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text"):
                    sv.append(players.css(f"tr:nth-child({ii}) > td:nth-child(10) > a::text").get())
                else:
                    sv.append(players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text"):
                    svo.append(players.css(f"tr:nth-child({ii}) > td:nth-child(11) > a::text").get())
                else:
                    svo.append(players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text"):
                    ip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(12) > a::text").get())
                else:
                    ip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text"):
                    h.append(players.css(f"tr:nth-child({ii}) > td:nth-child(13) > a::text").get())
                else:
                    h.append(players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text"):
                    r.append(players.css(f"tr:nth-child({ii}) > td:nth-child(14) > a::text").get())
                else:
                    r.append(players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text"):
                    er.append(players.css(f"tr:nth-child({ii}) > td:nth-child(15) > a::text").get())
                else:
                    er.append(players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text"):
                    hr.append(players.css(f"tr:nth-child({ii}) > td:nth-child(16) > a::text").get())
                else:
                    hr.append(players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text").get())

                if not players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text"):
                    hb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(17) > a::text").get())
                else:
                    hb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(18)::text"):
                    bb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(18) > a::text").get())
                else:
                    bb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(18)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(19)::text"):
                    so.append(players.css(f"tr:nth-child({ii}) > td:nth-child(19) > a::text").get())
                else:
                    so.append(players.css(f"tr:nth-child({ii}) > td:nth-child(19)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(20)::text"):
                    whip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(20) > a::text").get())
                else:
                    whip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(20)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(21)::text"):
                    avg.append(players.css(f"tr:nth-child({ii}) > td:nth-child(21) > a::text").get())
                else:
                    avg.append(players.css(f"tr:nth-child({ii}) > td:nth-child(21)::text").get())
                i += 1
                ii += 1
            yield names,teams,w,l,era,g,gs,cg,sho,sv,svo,ip,h,r,er,hr,hb,bb,so,whip,avg
    
def run_spider():
    custom_settings = {
        "LOG_LEVEL" : "WARNING",
        "ROBOTSTXT_OBEY" : True,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "ITEM_PIPELINES" : {"pipelines.Mlb_pitching_leaders" : 300}
    }
    process = CrawlerProcess(custom_settings)
    process.crawl(PitchingLeadersSpider)
    process.start()