import mlb_players as mlb_players

from textual import work
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Footer, Label, Tabs

TABS = ["Hitting Leaders", "Pitching Leaders", "Search",]

class Mlb_stats_ui(App):
    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    Label {
        margin:1 1;
        width: 100%;
        height: 100%;
        background: $panel;
        border: tall $primary;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Tabs(TABS[0], TABS[1], TABS[2])
        yield Label()
        yield Footer()
        
    def on_mount(self) -> None:
        self.query_one(Tabs).focus()
    
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

