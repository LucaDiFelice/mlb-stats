# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MlbStatsPipeline:
    def process_item(self, item, spider):
        file_names = open("player_names.csv", "a")
        file_links = open("path_links.csv", "a")
        if "path_links" in item:
            for link in item["path_links"]:
                file_links.write(link)
                file_links.write("\n")
        if "player_names" in item:
            for name in item["player_names"]:
                file_names.write(name)
                file_names.write("\n")
        file_names.close()
        file_links.close()
        return item
