import mlb_players as mlb_players
import stat_leaders as stat_leaders

from operator import itemgetter
from typing import Any, Self

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
    ("PLAYER", "TEAM", "PA", "HBP", "SAC", "SF", "GIDP", "GO/AO", "XBH", "TB", "IBB", "BABIP", "ISO", "AB/HR", "BB/K", "BB%", "SO%")
]
pitching_columns = [
    ("PLAYER", "W", "L", "ERA", "G", "GS", "CG", "SHO", "SV", "SVO", "IP", "H", "R", "ER", "HR", "HB", "BB", "SO", "WHIP", "AVG")
]
expanded_pitching_columns = [
    ("PLAYER", "TEAM", "TBF", "NP", "P/IP", "QS", "GF", "HLD", "IBB", "WP", "BK", "GDP", "GO/AO", "SO/9", "BB/9", "K/BB")
]
hitting_leaders = []


class Mlb_stats_ui(App):

    BINDINGS = [
        ("u", "update", "Update")
    ]

    def compose(self) -> ComposeResult:
        #yield Tabs(TABS[0], TABS[1], TABS[2])
        yield Label()
        yield Footer()
        with TabbedContent():
            with TabPane(TABS[0], id="hitting-leaders-id"):
                with TabbedContent("Standard", "Expanded"):
                    with TabPane(sub_rows[0]):
                        yield CustomDataTable()
                    with TabPane(sub_rows[1]):
                        yield DataTable(id="expanded-hitting-table")
            with TabPane(TABS[1], id="pitching-leaders-id"):
                with TabbedContent("Standard", "Expanded"):
                    with TabPane(sub_rows[0]):
                        yield DataTable(id="pitching-table")
                    with TabPane(sub_rows[1]):
                        yield DataTable(id="expanded-pitching-table")
            with TabPane(TABS[2], id="search-id"):
                pass

        
    def on_mount(self) -> None:
        self.query_one(Tabs).focus()
        h_table = self.query_one(DataTable)
        h_table.add_columns(*hitting_columns[0])
        h_table.add_rows(hitting_leaders)
        h_table.zebra_stripes = True

        h_e_table = self.query_one("#expanded-hitting-table", DataTable)
        h_e_table.add_columns(*expanded_hitting_columns[0])
        h_e_table.add_rows(expanded_hitting_columns[1:])

        p_table = self.query_one("#pitching-table", DataTable)
        p_table.add_columns(*pitching_columns[0])
        p_table.add_rows(pitching_columns[1:])

        p_e_table = self.query_one("#expanded-pitching-table", DataTable)
        p_e_table.add_columns(*expanded_pitching_columns[0])
        p_e_table.add_rows(expanded_pitching_columns[1:])
    
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
    def __init__(self) -> None:
        self._sorted_rows = False
        super().__init__()

    def on_data_table_header_selected(self, event: Click) -> None:
        #self._sorted_rows = not self._sorted_rows
        self.sort(event.column_key, reverse=not self._sorted_rows)
    

def main():
    # runs the spider
    #mlb_players.run_spider()

    # runs the stat_leader spider
    #stat_leaders.run_spider()
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
    

    mlb = Mlb_stats_ui()
    mlb.run()
    
main()

