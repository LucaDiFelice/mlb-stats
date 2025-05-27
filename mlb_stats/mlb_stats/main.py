import mlb_players as mlb_players

from textual import work
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.binding import Binding
from textual.widgets import Footer, Label, Tabs, TabPane, Button, Markdown, TabbedContent, DataTable

TABS = ["Hitting Leaders", "Pitching Leaders", "Search",]
hitting_rows = [
    ("TEAM", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "SO", "SB", "CS", "AVG", "OBP", "SLG", "OPS"),
]
pitching_rows = [
    ("TEAM", "W", "L", "ERA", "G", "GS", "CG", "SHO", "SV", "SVO", "IP", "H", "R", "ER", "HR", "HB", "BB", "SO", "WHIP", "AVG")
]


class Mlb_stats_ui(App):

    def compose(self) -> ComposeResult:
        #yield Tabs(TABS[0], TABS[1], TABS[2])
        yield Label()
        yield Footer()
        with TabbedContent():
            with TabPane(TABS[0], id="hitting-leaders-id"):
                yield DataTable(id="hitting-table")
            with TabPane(TABS[1], id="pitching-leaders-id"):
                yield DataTable(id="pitching-table")
            with TabPane(TABS[2], id="search-id"):
                pass

        
    def on_mount(self) -> None:
        self.query_one(Tabs).focus()
        h_table = self.query_one("#hitting-table", DataTable)
        h_table.add_columns(*hitting_rows[0])
        h_table.add_rows(hitting_rows[1:])

        p_table = self.query_one("#pitching-table", DataTable)
        p_table.add_columns(*pitching_rows[0])
        p_table.add_rows(pitching_rows[1:])
    
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

