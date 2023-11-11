import flet as ft

from ..types import DateLimits, DateLimitOption, DateOptionString


class DateInput(ft.TextField):
    DATE_LIMITS: DateLimits = {
        "day": (1, 31),
        "month": (1, 12),
        "year": (1, 9999),
    }

    def __init__(self, date_option: DateOptionString, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.saved_input = None
        self.on_change = lambda event: self._content_control(event, date_option.value)

    def _content_control(self, event: ft.ControlEvent, option: DateLimitOption) -> None:
        user_input = event.data
        self.saved_input = self.value

        if not user_input.isdigit():
            self.value = "".join(char for char in user_input if char.isdigit())
            self.update()
            return None

        min_value, max_value = self.DATE_LIMITS[option]
        user_value = int(user_input)
        if user_value == 0:
            self.value = ""
        elif min_value <= user_value <= max_value:
            self.value = user_input
        else:
            self.value = user_input[: len(str(max_value)) - 1]

        self.update()
