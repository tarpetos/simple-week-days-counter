import flet as ft
from typing import Callable, Optional
from .date_frame import DateFrame
from .toplevel_dialog import ToplevelDialog
from .utils import WeekDaysCalculator, DateRandomizer
from .grid_builder import GridBuilder
from .config import WindowConfig
from ..types import DateOption


class WeekDaysCounterApp(ft.UserControl, GridBuilder):
    BUTTON_WIDTH = 400
    BUTTON_HEIGHT = 100
    ERROR_DIALOG_TITLE = "ERROR"

    def __init__(self, config: WindowConfig) -> None:
        super().__init__()
        self.start_date_frame = DateFrame("start")
        self.end_date_frame = DateFrame("end")
        self.calculate_weekdays = self.build_button(
            text="Calculate week days", callback=self.on_calculate_weekdays
        )
        self.randomize_inputs = self.build_button(
            text="Randomize inputs", callback=self.on_randomize_inputs
        )
        self.result_output = ft.TextField(
            text_align=ft.TextAlign.CENTER,
            read_only=True,
            min_lines=7,
            max_lines=7,
            expand=True,
        )

        self.rows = [
            self.build_row(self.start_date_frame),
            self.build_row(self.end_date_frame),
            self.build_row(self.calculate_weekdays, self.randomize_inputs),
            self.build_row(self.result_output),
        ]

    @staticmethod
    def _convert_to_date_str(*inputs: ft.TextField) -> str:
        return "-".join(input_.value for input_ in inputs)

    def on_calculate_weekdays(self, event: ft.ControlEvent) -> None:
        start_date = self._convert_to_date_str(
            self.start_date_frame.day_input,
            self.start_date_frame.month_input,
            self.start_date_frame.year_input,
        )
        end_date = self._convert_to_date_str(
            self.end_date_frame.day_input,
            self.end_date_frame.month_input,
            self.end_date_frame.year_input,
        )
        calculator = WeekDaysCalculator(start_date, end_date)
        result_data = calculator.count_control()

        self.result_output.value = ""
        if isinstance(result_data, dict):
            for day, count in result_data.items():
                self.result_output.value += f"{day}: {count}\n"
        elif not all(
            [
                self.start_date_frame.day_input.value,
                self.start_date_frame.month_input.value,
                self.start_date_frame.year_input.value,
                self.end_date_frame.day_input.value,
                self.end_date_frame.month_input.value,
                self.end_date_frame.year_input.value,
            ]
        ):
            error_message = "One or more input fields are empty!"
            ToplevelDialog(
                self.page,
                dialog_title=self.ERROR_DIALOG_TITLE,
                dialog_content=error_message,
            )
        else:
            error_message = f"{str(result_data)[0].upper()}{str(result_data)[1:]}.\n"
            ToplevelDialog(
                self.page,
                dialog_title=self.ERROR_DIALOG_TITLE,
                dialog_content=error_message,
            )

        self.update()

    @staticmethod
    def _insert_data_to_inputs(randomizer: DateRandomizer, frame: DateFrame) -> None:
        random_data = randomizer.randomize()
        frame.day_input.value = str(random_data[DateOption.DAY])
        frame.month_input.value = str(random_data[DateOption.MONTH])
        frame.year_input.value = str(random_data[DateOption.YEAR])
        frame.update()

    def on_randomize_inputs(self, event: ft.ControlEvent) -> None:
        randomizer = DateRandomizer()
        self._insert_data_to_inputs(randomizer, self.start_date_frame)
        self._insert_data_to_inputs(randomizer, self.end_date_frame)

    @staticmethod
    def build_button(text: str, callback: Optional[Callable]) -> ft.ElevatedButton:
        return ft.ElevatedButton(text=text, on_click=callback, expand=True)

    def build(self) -> ft.Column:
        return self.build_column(*self.rows)


def build_window(page: ft.Page) -> None:
    config = WindowConfig(page)
    page.add(WeekDaysCounterApp(config))
