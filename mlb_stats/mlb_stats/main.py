import mlb_players as mlb_players
import stat_leaders as stat_leaders
import e_hitting_leaders as e_hitting_leaders
import pitching_leaders as pitching_leaders
import e_pitching_leaders as e_pitching_leaders_s

from rich.text import Text

from textual._two_way_dict import TwoWayDict
from textual.app import App, ComposeResult
from textual.events import Click
from textual.widgets import DataTable
from textual.widgets.data_table import CellType, ColumnKey, RowKey

from textual import work
from textual.app import App, ComposeResult
from textual.events import Click
from textual.widgets import Footer, Label, Tabs, TabPane, TabbedContent, DataTable

TABS = ["Hitting Leaders", "Pitching Leaders", "Search",]
sub_rows = ["Standard", "Expanded", "Statcast"]
hitting_columns = [
    ("PLAYER", "TEAM", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "SO", "SB", "CS", "AVG", "OBP", "SLG", "OPS"),
]
expanded_hitting_columns = [
    ("PLAYER", "TEAM", "PA", "HBP", "SAC", "SF", "GIDP", "GO/AO", "XBH", 
     "TB", "IBB", "BABIP", "ISO", "AB/HR", "BB/K", "BB%", "SO%")
]
pitching_columns = [
    ("PLAYER", "TEAM", "W", "L", "ERA", "G", "GS", "CG", "SHO", "SV", 
     "SVO", "IP", "H", "R", "ER", "HR", "HB", "BB", "SO", "WHIP", "AVG")
]
expanded_pitching_columns = [
    ("PLAYER", "TEAM", "TBF", "NP", "P/IP", "QS", "GF", "HLD", "IBB", "WP", 
     "BK", "GDP", "GO/AO", "SO/9", "BB/9", "K/BB", "BABIP", "SB", "CS", "PK")
]
hitting_leaders = []
hitting_leaders_e = []
pitching_leaders_ = []
e_pitching_leaders_ = []


class Mlb_stats_ui(App):

    def compose(self) -> ComposeResult:
        #yield Tabs(TABS[0], TABS[1], TABS[2])
        yield Label()
        yield Footer()
        with TabbedContent():
            with TabPane(TABS[0], id="hitting-leaders-id"):
                with TabbedContent("Standard", "Expanded"):
                    with TabPane(sub_rows[0]):
                        yield CustomDataTable(id="hitting-table")
                    with TabPane(sub_rows[1]):
                        yield CustomDataTable(id="e-hitting-table")
            with TabPane(TABS[1], id="pitching-leaders-id"):
                with TabbedContent("Standard", "Expanded"):
                    with TabPane(sub_rows[0]):
                        yield CustomDataTable(id="pitching-table")
                    with TabPane(sub_rows[1]):
                        yield CustomDataTable(id="expanded-pitching-table")
            with TabPane(TABS[2], id="search-id"):
                pass

        
    def on_mount(self) -> None:
        self.query_one(Tabs).focus()
        h_table = self.query_one("#hitting-table", CustomDataTable)
        h_table.add_columns(*hitting_columns[0])
        h_table.add_rows(hitting_leaders)
        h_table.zebra_stripes = True

        h_e_table = self.query_one("#e-hitting-table", CustomDataTable)
        h_e_table.add_columns(*expanded_hitting_columns[0])
        h_e_table.add_rows(hitting_leaders_e)
        h_e_table.zebra_stripes = True

        p_table = self.query_one("#pitching-table", CustomDataTable)
        p_table.add_columns(*pitching_columns[0])
        p_table.add_rows(pitching_leaders_)
        p_table.zebra_stripes = True

        p_e_table = self.query_one("#expanded-pitching-table", CustomDataTable)
        p_e_table.add_columns(*expanded_pitching_columns[0])
        p_e_table.add_rows(e_pitching_leaders_)
        p_e_table.zebra_stripes = True
    
    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        label = self.query_one(Label)
        if event.tab is None:
            label.visible = False
        else:
            label.visible = True
            label.update(event.tab.label)
    
    def action_add(self) -> None:
        tabs = self.query_one(Tabs)
        TABS[:] = [*TABS[1:], TABS[0]]
        tabs.add_tab(TABS[0])

    def action_remove(self) -> None:
        tabs = self.query_one(Tabs)
        active_tab = tabs.active_tab
        if active_tab is not None:
            tabs.remove_tab(active_tab.id)

    def action_clear(self) -> None:
        self.query_one(Tabs).clear()

class CustomDataTable(DataTable):

    def __init__(self, *args, **kwargs) -> None:
        self._sorted_rows = False
        super().__init__(*args, **kwargs)

    def on_data_table_header_selected(self, event: Click) -> None:
        #self._sorted_rows = not self._sorted_rows
        self.sort(event.column_key, reverse=not self._sorted_rows)

def main():
    # runs the spider that get all players
    #mlb_players.run_spider()

    # runs the stat_leader spider
    #stat_leaders.run_spider()

    # runs the e_hitting_leaders spider
    #e_hitting_leaders.run_spider()

    #runs the pitching_leaders spider
    #pitching_leaders.run_spider()

    #runs the e_pitching_leaders spider
    #e_pitching_leaders_s.run_spider()
    
    names = []
    with open("player_names.csv", "r") as file_names:
        for line in file_names:
            names.append(line.strip())

    file_names.close()
    
    
    temp = []
    
    with open("hitting_leaders_s.csv", "r") as file_names:
        for line in file_names:
            temp.append(line.strip())

    ii = 0
    for i in range(0, len(temp), 18):
        hitting_leaders.append(temp[i:i+2])
        hitting_leaders[ii].append(int(temp[i+2]))
        hitting_leaders[ii].append(int(temp[i+3]))
        hitting_leaders[ii].append(int(temp[i+4]))
        hitting_leaders[ii].append(int(temp[i+5]))
        hitting_leaders[ii].append(int(temp[i+6]))
        hitting_leaders[ii].append(int(temp[i+7]))
        hitting_leaders[ii].append(int(temp[i+8]))
        hitting_leaders[ii].append(int(temp[i+9]))
        hitting_leaders[ii].append(int(temp[i+10]))
        hitting_leaders[ii].append(int(temp[i+11]))
        hitting_leaders[ii].append(int(temp[i+12]))
        hitting_leaders[ii].append(int(temp[i+13]))
        hitting_leaders[ii].append(float(temp[i+14]))
        hitting_leaders[ii].append(float(temp[i+15]))
        hitting_leaders[ii].append(float(temp[i+16]))
        hitting_leaders[ii].append(float(temp[i+17]))

        ii += 1
    #for i in range(len(hitting_leaders)):
    temp2 = []
    with open("e_hitting_stats.csv", "r") as file:
        for line in file:
            temp2.append(line.strip())

    ii = 0
    for i in range(0, len(temp2), 17):        
        hitting_leaders_e.append(temp2[i:i+2])
        hitting_leaders_e[ii].append(int(temp2[i+2]))
        hitting_leaders_e[ii].append(int(temp2[i+3]))
        hitting_leaders_e[ii].append(int(temp2[i+4]))
        hitting_leaders_e[ii].append(int(temp2[i+5]))
        hitting_leaders_e[ii].append(int(temp2[i+6]))
        hitting_leaders_e[ii].append(float(temp2[i+7]))
        hitting_leaders_e[ii].append(int(temp2[i+8]))
        hitting_leaders_e[ii].append(int(temp2[i+9]))
        hitting_leaders_e[ii].append(int(temp2[i+10]))
        hitting_leaders_e[ii].append(float(temp2[i+11]))
        hitting_leaders_e[ii].append(float(temp2[i+12]))
        hitting_leaders_e[ii].append(float(temp2[i+13]))
        hitting_leaders_e[ii].append(float(temp2[i+14]))
        hitting_leaders_e[ii].append(float(temp2[i+15]))
        hitting_leaders_e[ii].append(float(temp2[i+16]))
        ii += 1

    temp3 = []
    with open("pitching_leaders.csv", "r") as file:
        for line in file:
            temp3.append(line.strip())

    ii = 0
    for i in range(0,len(temp3), 21):
        pitching_leaders_.append(temp3[i:i+2])
        pitching_leaders_[ii].append(int(temp3[i+2]))
        pitching_leaders_[ii].append(int(temp3[i+3]))
        pitching_leaders_[ii].append(float(temp3[i+4]))
        pitching_leaders_[ii].append(int(temp3[i+5]))
        pitching_leaders_[ii].append(int(temp3[i+6]))
        pitching_leaders_[ii].append(int(temp3[i+7]))
        pitching_leaders_[ii].append(int(temp3[i+8]))
        pitching_leaders_[ii].append(int(temp3[i+9]))
        pitching_leaders_[ii].append(int(temp3[i+10]))
        pitching_leaders_[ii].append(float(temp3[i+11]))
        pitching_leaders_[ii].append(int(temp3[i+12]))
        pitching_leaders_[ii].append(int(temp3[i+13]))
        pitching_leaders_[ii].append(int(temp3[i+14]))
        pitching_leaders_[ii].append(int(temp3[i+15]))
        pitching_leaders_[ii].append(int(temp3[i+16]))
        pitching_leaders_[ii].append(int(temp3[i+17]))
        pitching_leaders_[ii].append(int(temp3[i+18]))
        pitching_leaders_[ii].append(float(temp3[i+19]))
        pitching_leaders_[ii].append(float(temp3[i+20]))
        ii += 1
    
    temp4 = []
    with open("e_pitching_leaders.csv", "r") as file:
        for line in file:
            temp4.append(line.strip())

    ii = 0
    for i in range(0,len(temp3), 20):
        e_pitching_leaders_.append(temp4[i:i+2])
        e_pitching_leaders_[ii].append(int(temp4[i+2]))
        e_pitching_leaders_[ii].append(int(temp4[i+3]))
        e_pitching_leaders_[ii].append(float(temp4[i+4]))
        e_pitching_leaders_[ii].append(int(temp4[i+5]))
        e_pitching_leaders_[ii].append(int(temp4[i+6]))
        e_pitching_leaders_[ii].append(int(temp4[i+7]))
        e_pitching_leaders_[ii].append(int(temp4[i+8]))
        e_pitching_leaders_[ii].append(int(temp4[i+9]))
        e_pitching_leaders_[ii].append(int(temp4[i+10]))
        e_pitching_leaders_[ii].append(int(temp4[i+11]))
        e_pitching_leaders_[ii].append(float(temp4[i+12]))
        e_pitching_leaders_[ii].append(float(temp4[i+13]))
        e_pitching_leaders_[ii].append(float(temp4[i+14]))
        e_pitching_leaders_[ii].append(float(temp4[i+15]))
        e_pitching_leaders_[ii].append(float(temp4[i+16]))
        e_pitching_leaders_[ii].append(int(temp4[i+17]))
        e_pitching_leaders_[ii].append(int(temp4[i+18]))
        e_pitching_leaders_[ii].append(int(temp4[i+19]))
        ii += 1
    

    mlb = Mlb_stats_ui()
    mlb.run()
    
main()

