from operator import itemgetter
from typing import Any, Self

from textual._two_way_dict import TwoWayDict
from textual.app import App, ComposeResult
from textual.events import Click
from textual.widgets import DataTable
from textual.widgets.data_table import CellType, ColumnKey, RowKey

ROWS = [
    ("lane", "swimmer", "country", "time", "date"),
    (4, "Joseph Schooling", "Singapore", 50.39, "26/07/23"),
    (2, "Michael Phelps", "United States", 51.14, "26/05/21"),
    (5, "Chad le Clos", "South Africa", 51.14, "26/07/19"),
    (6, "László Cseh", "Hungary", 51.14, "28/07/18"),
    (3, "Li Zhuhao", "China", 51.26, "15/03/22"),
    (8, "Mehdy Metella", "France", 51.58, "02/02/23"),
    (7, "Tom Shields", "United States", 51.73, "08/07/23"),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84, "06/09/22"),
    (10, "Darren Burns", "Scotland", 51.84, "02/08/20"),
]


class CustomDataTable(DataTable):
    def __init__(self) -> None:
        self._sorted_rows = False
        super().__init__()

    def on_data_table_header_selected(self, event: Click) -> None:
        """Sort `DataTable` items by the clicked column header."""
        self._sorted_rows = not self._sorted_rows
        if event.label.plain.lower() == "date":
            self.custom_date_sort(event.column_key, reverse=not self._sorted_rows)
        else:
            self.sort(event.column_key, reverse=not self._sorted_rows)

    def custom_date_sort(
        self, *columns: ColumnKey | str, reverse: bool = False
    ) -> Self:
        """Custom implementation of the built-in DataTable sort method. Sort the rows
        in the `DataTable` by one or more column keys.
        Args:
            columns: One or more columns to sort by the values in.
            reverse: If True, the sort order will be reversed.
        Returns:
            The `DataTable` instance.
        """

        def sort_by_date(row: tuple[RowKey, dict[ColumnKey | str, CellType]]) -> Any:
            _, row_data = row
            result = itemgetter(*columns)(row_data)
            d, m, y = result.split("/")
            return f"{y}{m}{d}"

        ordered_rows = sorted(
            self._data.items(),
            key=sort_by_date,
            reverse=reverse,
        )
        self._row_locations = TwoWayDict(
            {key: new_index for new_index, (key, _) in enumerate(ordered_rows)}
        )
        self._update_count += 1
        self.refresh()
        return self


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield CustomDataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])


app = TableApp()
if __name__ == "__main__":
    app.run()