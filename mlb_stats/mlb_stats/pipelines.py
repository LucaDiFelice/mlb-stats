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

class MlbLeadersPipeline:
    names = []
    def process_item(self, item, spider):
        file_leaders = open("hitting_leaders_s.csv", "a")

        i = 0
        keys = list(item.keys())
        for name in item:
            if keys[i] not in self.names:
                self.names.append(keys[i])
                file_leaders.write(keys[i])
                file_leaders.write("\n")
                file_leaders.write(str(item[name][0]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][0]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][1]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][2]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][3]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][4]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][5]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][6]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][7]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][8]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][9]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][10]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][11]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][12]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][13]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][14]))
                file_leaders.write("\n")
                file_leaders.write(str(item[name][1]["Standard"][15]))
                file_leaders.write("\n")
            i += 1
        file_leaders.close()
        print(self.names)

class Mlb_E_Hitting_Leaders:
    names = []
    def process_item(self, item, spider):
        file_e_hitting_l = open("e_hitting_stats.csv", "a")
        for i in range(len(item[0])):
            index = 0
            if item[0][i] not in self.names:
                self.names.append(item[0][i])
                file_e_hitting_l.write(item[0][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[1][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[2][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[3][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[4][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[5][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[6][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[7][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[8][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[9][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[10][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[11][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[12][i])
                file_e_hitting_l.write("\n")
                if item[13][i] != "-.--":
                    file_e_hitting_l.write(item[13][i])
                else:
                    file_e_hitting_l.write("0.00")
                file_e_hitting_l.write("\n")
                if item[14][i] != ".---":
                    file_e_hitting_l.write(item[14][i])
                else:
                    file_e_hitting_l.write(".000")
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[15][i])
                file_e_hitting_l.write("\n")
                file_e_hitting_l.write(item[16][i])
                print(item[0][i])
                file_e_hitting_l.write("\n")
        file_e_hitting_l.close()

class Mlb_pitching_leaders:
    names = []
    def process_item(self, item, spider):
        file_pitching_l = open("pitching_leaders.csv", "w")
        for i in range(len(item[0])):
            index = 0
            if item[0][i] not in self.names:
                self.names.append(item[0][i])
                file_pitching_l.write(item[0][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[1][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[2][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[3][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[4][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[5][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[6][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[7][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[8][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[9][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[10][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[11][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[12][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[13][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[14][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[15][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[16][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[17][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[18][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[19][i])
                file_pitching_l.write("\n")
                file_pitching_l.write(item[20][i])
                file_pitching_l.write("\n")
        file_pitching_l.close()