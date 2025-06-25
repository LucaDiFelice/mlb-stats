import scrapy
from scrapy.crawler import CrawlerProcess


class EPitchingLeadersSpider(scrapy.Spider):
    name = "e_pitching_leaders"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/stats/pitching"]
    category_links = ["/total-batters-faced?expanded=true", "/number-of-pitches?expanded=true",
                      "/pitches-per-inning?expanded=true", "/quality-starts?expanded=true",
                      "/pitching/games-finished?expanded=true", "/holds?expanded=true",
                      "/intentional-walks?expanded=true", "/wild-pitch?expanded=true",
                      "/balk?expanded=true", "/grounded-into-double-plays?expanded=true",
                      "/ground-out-air-out-ratio?expanded=true", "/strikeouts-per-nine-innings?expanded=true",
                      "/walks-per-nine-innings?expanded=true", "/strikeout-to-walk-ratio?expanded=true",
                      "/babip?expanded=true", "/stolen-bases-allowed?expanded=true", "/caught-stealing?expanded=true",
                      "/pickoff?expanded=true"]
    
    custom_settings = {
        "LOG_LEVEL" : "WARNING",
        "ROBOTSTXT_OBEY" : True,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "ITEM_PIPELINES" : {"pipelines.Mlb_e_pitching_leaders" : 300}
    }

    def parse(self, response):
        if response.url in "https://www.mlb.com/stats/pitching":
            for link in self.category_links:
                next_page_url = "https://www.mlb.com/stats/pitching" + link
                yield response.follow(next_page_url, callback=self.parse)
        else:
            i = 0
            ii = 1
            e_pitching_leaders = {}
            players = response.css("tbody")
            names = players.css("tr > th > div > div.value-wrapper-Ym32XJij > div.top-wrapper-TqtRaIeD > div > a::attr(aria-label)").getall()
            teams = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").getall()
            tbf = []
            np = []
            p_ip = []
            qs = []
            gf = []
            hld = []
            ibb = []
            wp = []
            bk = []
            gdp = []
            go_ao = []
            so_9 = []
            bb_9 = []
            k_bb = []
            babip = []
            sb = []
            cs = []
            pk = []
            while i < len(names):
                tbf.append(players.css(f"tr:nth-child({ii}) > td:nth-child(3)::text").get())
                np.append(players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text").get())
                p_ip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text").get())
                qs.append(players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text").get())
                gf.append(players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text").get())
                hld.append(players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text").get())
                ibb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text").get())
                wp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text").get())
                bk.append(players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text").get())
                gdp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text").get())
                go_ao.append(players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text").get())
                so_9.append(players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text").get())
                bb_9.append(players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text").get())
                k_bb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text").get())
                babip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text").get())
                sb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(18)::text").get())
                cs.append(players.css(f"tr:nth-child({ii}) > td:nth-child(19)::text").get())
                pk.append(players.css(f"tr:nth-child({ii}) > td:nth-child(20)::text").get())
                i += 1
                ii += 1
            yield names,teams,tbf,np,p_ip,qs,gf,hld,ibb,wp,bk,gdp,go_ao,so_9,bb_9,k_bb,babip,sb,cs,pk

def run_spider():
    custom_settings = {
        "LOG_LEVEL" : "WARNING",
        "ROBOTSTXT_OBEY" : True,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "ITEM_PIPELINES" : {"pipelines.Mlb_e_pitching_leaders" : 300}
    }
    process = CrawlerProcess(custom_settings)
    process.crawl(EPitchingLeadersSpider)
    process.start()
