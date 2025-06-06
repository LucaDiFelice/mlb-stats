import scrapy


class EHittingLeadersSpider(scrapy.Spider):
    name = "e_hitting_leaders"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/stats"]

    stat_categories = []

    def parse(self, response):
        if response.url in "https://www.mlb.com/stats":
            for stat in ["/plate-appearances?expanded=true"]:
                next_page_url = "https://www.mlb.com/stats" + stat
                yield response.follow(next_page_url, callback=self.parse)
        else:
            i = 0
            ii = 1
            e_hitting_leaders = {}
            players = response.css("tbody")
            names = players.css("tr > th > div > div.value-wrapper-Ym32XJij > div.top-wrapper-TqtRaIeD > div > a::attr(aria-label)").getall()
            teams = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-left-L6MdxTlJ.is-table-pinned-lGP8KWTK::text").getall()
            pa = []
            hbp = []
            sac = []
            sf = []
            gidp = []
            go_ao = []
            xbh = []
            tb = []
            ibb = []
            babip = []
            iso = []
            ab_hr = []
            bb_k = []
            bb_per = []
            so_per = []
            while i < len(names):
                pa.append(players.css(f"tr:nth-child({ii}) > td:nth-child(3)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text"):
                    hbp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(4) > a::text").get())
                else:
                    hbp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(4)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text"):
                    sac.append(players.css(f"tr:nth-child({ii}) > td:nth-child(5) > a::text").get())
                else:
                    sac.append(players.css(f"tr:nth-child({ii}) > td:nth-child(5)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text"):
                    sf.append(players.css(f"tr:nth-child({ii}) > td:nth-child(6) > a::text").get())
                else:
                    sf.append(players.css(f"tr:nth-child({ii}) > td:nth-child(6)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text"):
                    gidp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(7) > a::text").get())
                else:
                    gidp.append(players.css(f"tr:nth-child({ii}) > td:nth-child(7)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text"):
                    go_ao.append(players.css(f"tr:nth-child({ii}) > td:nth-child(8) > a::text").get())
                else:
                    go_ao.append(players.css(f"tr:nth-child({ii}) > td:nth-child(8)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text"):
                    xbh.append(players.css(f"tr:nth-child({ii}) > td:nth-child(9) > a::text").get())
                else:
                    xbh.append(players.css(f"tr:nth-child({ii}) > td:nth-child(9)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text"):
                    tb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(10) > a::text").get())
                else:
                    tb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(10)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text"):
                    ibb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(11) > a::text").get())
                else:
                    ibb.append(players.css(f"tr:nth-child({ii}) > td:nth-child(11)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text"):
                    babip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(12) > a::text").get())
                else:
                    babip.append(players.css(f"tr:nth-child({ii}) > td:nth-child(12)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text"):
                    iso.append(players.css(f"tr:nth-child({ii}) > td:nth-child(13) > a::text").get())
                else:
                    iso.append(players.css(f"tr:nth-child({ii}) > td:nth-child(13)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text"):
                    ab_hr.append(players.css(f"tr:nth-child({ii}) > td:nth-child(14) > a::text").get())
                else:
                    ab_hr.append(players.css(f"tr:nth-child({ii}) > td:nth-child(14)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text"):
                    bb_k.append(players.css(f"tr:nth-child({ii}) > td:nth-child(15) > a::text").get())
                else:
                    bb_k.append(players.css(f"tr:nth-child({ii}) > td:nth-child(15)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text"):
                    bb_per.append(players.css(f"tr:nth-child({ii}) > td:nth-child(16) > a::text").get())
                else:
                    bb_per.append(players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text").get())
                if not players.css(f"tr:nth-child({ii}) > td:nth-child(16)::text"):
                    so_per.append(players.css(f"tr:nth-child({ii}) > td:nth-child(17) > a::text").get())
                else:
                    so_per.append(players.css(f"tr:nth-child({ii}) > td:nth-child(17)::text").get())
                i += 1
                ii += 1
            
            
            yield pa,hbp,sac,sf,gidp,go_ao,xbh,tb,ibb,babip,iso,ab_hr,bb_k,bb_per,so_per

def run_spider():
    custom_settings = {

    }
