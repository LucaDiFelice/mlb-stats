import scrapy

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
        g_played = players.css("tr > td.col-group-start-Gn6clGbi.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
        stat1 = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
        stat2 = players.css("tr > td.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK > a::text").getall()
        stat3 = players.css("tr > td.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
        while i < len(names):
            if names[i] not in hitting_leaders:
                hitting_leaders[names[i]] = [] # name
            hitting_leaders[names[i]].append(teams[i]) # team
            hitting_leaders[names[i]].append(g_played[stat_i]) # g
            hitting_leaders[names[i]].append(stat1[stat_i]) # ab
            hitting_leaders[names[i]].append(g_played[stat_i+1]) # r
            hitting_leaders[names[i]].append(stat2[stat2_i]) # h
            hitting_leaders[names[i]].append(stat2[stat2_i+1]) # 2b
            hitting_leaders[names[i]].append(stat2[stat2_i+2]) # 3b
            hitting_leaders[names[i]].append(stat2[stat2_i+3]) # hr
            hitting_leaders[names[i]].append(stat1[stat_i+1]) # rbi
            hitting_leaders[names[i]].append(stat2[stat2_i+4]) # bb
            hitting_leaders[names[i]].append(stat2[stat2_i+5]) # so
            hitting_leaders[names[i]].append(g_played[stat_i+2]) # sb
            hitting_leaders[names[i]].append(stat1[stat_i+2]) # cs
            hitting_leaders[names[i]].append(g_played[stat_i+3]) # .avg
            hitting_leaders[names[i]].append(stat3[stat3_i]) # obp
            hitting_leaders[names[i]].append(stat3[stat3_i+1]) # slg
            hitting_leaders[names[i]].append(stat1[stat_i+3]) # OPS
            

            stat_i += 4
            stat2_i += 5
            i += 1
        yield hitting_leaders