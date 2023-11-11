import flet as ft
from .ui import build_window


class WeekDaysCounter:
    @staticmethod
    def start() -> None:
        ft.app(target=build_window)
