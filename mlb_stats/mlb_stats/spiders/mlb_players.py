import scrapy


class MlbPlayersSpider(scrapy.Spider):
    name = "mlb_players"
    allowed_domains = ["www.baseball-reference.com"]
    start_urls = ["https://www.baseball-reference.com/players/a"]

    def parse(self, response):
        players = response.css("div.section_content#div_players_")
        for player in players:
            yield {
                "name" : player.css("p a::text").getall()
            }
        
        for letter in "bcdefghijklmnopqrstuvwxyz":
            next_page_url = "https://www.baseball-reference.com/players/" + letter
            yield response.follow(next_page_url, callback=self.parse)