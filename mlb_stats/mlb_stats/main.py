import mlb_players as mlb_players

from textual import work
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.binding import Binding
from textual.widgets import Footer, Label, Tabs, TabPane, Button, Markdown, TabbedContent, DataTable

TABS = ["Hitting Leaders", "Pitching Leaders", "Search",]
sub_rows = ["Standard", "Expanded"]
hitting_rows = [
    ("PLAYER", "TEAM", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "SO", "SB", "CS", "AVG", "OBP", "SLG", "OPS"),
]
expanded_hitting_rows = [
    ("PLAYER", "TEAM", "PA", "HBP", "SAC", "SF", "GIDP", "GO/AO", "XBH", "TB", "IBB", "BABIP", "ISO", "AB/HR", "BB/K", "BB%", "SO%")
]
pitching_rows = [
    ("PLAYER", "W", "L", "ERA", "G", "GS", "CG", "SHO", "SV", "SVO", "IP", "H", "R", "ER", "HR", "HB", "BB", "SO", "WHIP", "AVG")
]
expanded_pitching_rows = [
    ("PLAYER", "TEAM", "TBF", "NP", "P/IP", "QS", "GF", "HLD", "IBB", "WP", "BK", "GDP", "GO/AO", "SO/9", "BB/9", "K/BB")
]


class Mlb_stats_ui(App):

    def compose(self) -> ComposeResult:
        #yield Tabs(TABS[0], TABS[1], TABS[2])
        yield Label()
        yield Footer()
        with TabbedContent():
            with TabPane(TABS[0], id="hitting-leaders-id"):
                with TabbedContent("Standard", "Expanded"):
                    with TabPane(sub_rows[0]):
                        yield DataTable(id="hitting-table")
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
        h_table = self.query_one("#hitting-table", DataTable)
        h_table.add_columns(*hitting_rows[0])
        h_table.add_rows(hitting_rows[1:])

        h_e_table = self.query_one("#expanded-hitting-table", DataTable)
        h_e_table.add_columns(*expanded_hitting_rows[0])
        h_e_table.add_rows(expanded_hitting_rows[1:])

        p_table = self.query_one("#pitching-table", DataTable)
        p_table.add_columns(*pitching_rows[0])
        p_table.add_rows(pitching_rows[1:])

        p_e_table = self.query_one("#expanded-pitching-table", DataTable)
        p_e_table.add_columns(*expanded_pitching_rows[0])
        p_e_table.add_rows(expanded_pitching_rows[1:])
    
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
    

def main():
    # runs the spider
    #mlb_players.run_spider()
    names = []
    with open("player_names.csv", "r") as file_names:
        for line in file_names:
            names.append(line.strip())

    file_names.close()
    mlb = Mlb_stats_ui()
    mlb.run()
main()

