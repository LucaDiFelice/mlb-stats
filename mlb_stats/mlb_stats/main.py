import mlb_players as mlb_players

#from textual import work
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
        if message.value:
            self.lookup_word(message.value)
        else:
            # Clear the results
            await self.query_one("#results", Markdown).update("")
"""
        #@work(exclusive=True)
        #async def lookup_player(self, word: str) -> None:
            #with open("player_names.csv", "w") as player_file:
                #for line in player_file:
                    #print(line.strip())

def main():
    mlb_players.run_spider()
    #print(mlb_players.)
    #data = open("raw_data.csv", "r")
    #names = open("player_names.csv", "w")
    #path_links = open("path_links.csv", "w")
    #for line in data:
        #if line.startswith("") and line.endswith('"\n'):
    #with open("player_names.csv", "w") as player_file:
        #for line in player_file:
            #if line.startswith("") and line.endswith('"\n'):
                #line = line.strip()[1:-1]
                #player_names.extend(line.split(","))

main()
