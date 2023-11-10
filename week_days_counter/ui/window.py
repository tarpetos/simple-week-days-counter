from typing import Callable, Optional

import flet as ft
from .window_config import WindowConfig
from .grid_builder import GridBuilder
from .date_frame import DateFrame


class WeekDaysCounterApp(ft.UserControl, GridBuilder):
    BUTTON_WIDTH = 400
    BUTTON_HEIGHT = 100

    def __init__(self, config: WindowConfig) -> None:
        super().__init__()
        self.start_date_frame = DateFrame("start")
        self.end_date_frame = DateFrame("end")
        self.calculate_weekdays = self.build_button(text="Calculate week days", callback=self.on_calculate_weekdays)
        self.randomize_inputs = self.build_button(text="Randomize inputs", callback=self.on_randomize_inputs)
        self.result_output = ft.TextField(
            text_align=ft.TextAlign.CENTER,
            read_only=True,
            min_lines=7, max_lines=7,
            expand=True
        )

        self.rows = [
            self.build_row(self.start_date_frame),
            self.build_row(self.end_date_frame),
            self.build_row(self.calculate_weekdays, self.randomize_inputs),
            self.build_row(self.result_output),
        ]

    def on_calculate_weekdays(self, event: ft.ControlEvent) -> None:
        print(1)

    def on_randomize_inputs(self, event: ft.ControlEvent) -> None:
        print(2)

    def build_button(self, text: str, callback: Optional[Callable]) -> ft.ElevatedButton:
        return ft.ElevatedButton(
            text=text,
            on_click=callback,
            expand=True
        )

    def build(self) -> ft.Column:
        return self.build_column(*self.rows)


def build_window(page: ft.Page) -> None:
    config = WindowConfig(page)
    page.add(WeekDaysCounterApp(config))
