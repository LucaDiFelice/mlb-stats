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
            if not players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text"):
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK > a::text").get())
            else:
                hitting_leaders[names[i]][1]["Standard"].append(players.css(f"tr:nth-child({ii}) > td.selected-h6IPIIxg.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").get())
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

            if not hitting_leaders[names[i]][2]["Expanded"]:
                hitting_leaders[names[i]][2]["Expanded"].append("asd")
            i += 1
            ii += 1
        #stats-app-root > section > section > div.stats-body-table.player > div.table-wrapper-mxbeN3qL > div > table > tbody > tr:nth-child(1) > td:nth-child(3)
        #test2 = players.css("tr > td > a::text").getall() # this is important
        #g_played = players.css("tr > td:nth-child(3)::text").getall() # this is important
        #ab = players.css(f"tr:nth-child({num}) > td:nth-child(4)::text").getall()
        #r = players.css("tr > td:nth-child(5)::text").getall()
        #h = players.css("tr > td:nth-child(6) > a::text").getall()
        #two_b = players.css("tr > td:nth-child(7) > a::text").getall()
        #three_b = players.css("tr > td:nth-child(8) > a::text").getall()
        #stats-app-root > section > section > div.stats-body-table.player > div.table-wrapper-mxbeN3qL > div > table > tbody > tr:nth-child(1) > td:nth-child(8)
        #stats-app-root > section > section > div.stats-body-table.player > div.table-wrapper-mxbeN3qL > div > table > tbody > tr:nth-child(1) > td:nth-child(4)
        yield hitting_leaders

#g_played = players.css("tr > td.col-group-start-Gn6clGbi.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
#stat1 = players.css("tr > td.col-group-end-BOW7diD7.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
#stat2 = players.css("tr > td.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
#stat3 = players.css("tr > td.number-GoaicxKV.align-right-TwjGe_gi.is-table-pinned-lGP8KWTK::text").getall()
"""
while i < len(names):
    if names[i] not in hitting_leaders:
        hitting_leaders[names[i]] = []
        hitting_leaders[names[i]].append(teams[i]) # team
        hitting_leaders[names[i]].append({"Standard" : []})
        hitting_leaders[names[i]].append({"Expanded" : []})
        hitting_leaders[names[i]][1]["Standard"].append(g_played[stat_i]) # g
        hitting_leaders[names[i]][1]["Standard"].append(stat1[stat_i]) # ab
        hitting_leaders[names[i]][1]["Standard"].append(g_played[stat_i+1]) # r
        # something wrong here
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i]) # h
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i+1]) # 2b
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i+2]) # 3b
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i+3]) # hr
        hitting_leaders[names[i]][1]["Standard"].append(stat1[stat_i+1]) # rbi
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i+4]) # bb
        hitting_leaders[names[i]][1]["Standard"].append(stat2[stat2_i+5]) # so
        hitting_leaders[names[i]][1]["Standard"].append(g_played[stat_i+2]) # sb
        hitting_leaders[names[i]][1]["Standard"].append(stat1[stat_i+2]) # cs
        hitting_leaders[names[i]][1]["Standard"].append(g_played[stat_i+3]) # .avg
        hitting_leaders[names[i]][1]["Standard"].append(stat3[stat3_i]) # obp
        hitting_leaders[names[i]][1]["Standard"].append(stat3[stat3_i+1]) # slg
        hitting_leaders[names[i]][1]["Standard"].append(stat1[stat_i+3]) # OPS


        stat_i += 4
        stat2_i += 5
        stat3_i += 9

        i += 1
"""