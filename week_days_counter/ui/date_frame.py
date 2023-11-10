import flet as ft

from .date_input import DateInput
from .grid_builder import GridBuilder
from ..types import EntryFrameOption, DateOption


class DateFrame(ft.UserControl, GridBuilder):
    def __init__(self, frame_name: EntryFrameOption) -> None:
        super().__init__()
        self.title_label = ft.Text(
            value=f"{frame_name.upper()} DATE",
            text_align=ft.TextAlign.CENTER,
            size=25,
        )

        self.day_label = ft.Text(value="Day", text_align=ft.TextAlign.CENTER)
        self.month_label = ft.Text(value="Month", text_align=ft.TextAlign.CENTER)
        self.year_label = ft.Text(value="Year", text_align=ft.TextAlign.CENTER)

        self.day_input = DateInput(DateOption.DAY, text_align=ft.TextAlign.CENTER, label="1-31", max_length=2)
        self.month_input = DateInput(DateOption.MONTH, text_align=ft.TextAlign.CENTER, label="1-12", max_length=2)
        self.year_input = DateInput(DateOption.YEAR, text_align=ft.TextAlign.CENTER, label="1000-9999", max_length=4)

        self.rows = [
            self.build_row(self.title_label),
            self.build_row(
                self.day_label, self.day_input,
                self.month_label, self.month_input,
                self.year_label, self.year_input,
            ),
        ]

    def build(self) -> ft.Column:
        return self.build_column(*self.rows)
