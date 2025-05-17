import spiders.mlb_players as mlb_players
from textual import work
#from textual.app import App, ComposeResult
#from textual.containers import VerticalScroll
#from textual.widgets import Input, Markdown

"""
class DictionaryApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search for a word", id="dictionary-search")
        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    async def on_input_changed(self, message: Input.Changed) -> None:
        A coroutine to handle a text changed message.
        if message.value:
            self.lookup_word(message.value)
        else:
            # Clear the results
            await self.query_one("#results", Markdown).update("")
    
        @work(exclusive=True)
        async def lookup_word(self, word: str) -> None:
            with open("player_names.csv", "w") as player_file:
                player_file.read()
"""
def main():
    mlb_players.run_spider()
    #with open("player_names.csv", "r") as player_data:


main()