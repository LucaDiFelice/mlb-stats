import scrapy


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
            print("yeah")
            for link in self.category_links:
                next_page_url = "https://www.mlb.com/stats/pitching" + link
                yield response.follow(next_page_url, callback=self.parse)
        else:
            i = 0
            ii = 0
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