import tkinter as tk
from typing import Optional
from .placeholder_entry import PlaceholderEntry
from ..types import Window, DateLimits, DateOptionString


class DateEntry(PlaceholderEntry):
    DATE_LIMITS: DateLimits = {
        "day": 31,
        "month": 12,
        "year": 9999,
    }

    def __init__(
            self, master: Optional[Window] = None,
            date_option: Optional[DateOptionString] = None,
            *args,
            **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.bind("<Key>", lambda event: self.on_key_pressed(event, date_option))

    def on_key_pressed(self, event: tk.Event, date_option: DateOptionString) -> Optional[str]:
        max_value = self.DATE_LIMITS[date_option.value]
        max_length = len(str(max_value))
        allowed_key_codes = {111, 113, 114, 116, 22, 23, 119}
        if event.keycode in allowed_key_codes:
            return None

        if event.char.isdigit():
            return self._parse_digits(event, max_value, max_length)
        return "break"

    def _parse_digits(self, event: tk.Event, max_value: int, max_length: int) -> Optional[str]:
        user_input = int(self.get() + event.char)
        if self.select_present() and user_input >= 1:
            return None
        elif user_input > max_value or user_input == 0:
            self.bell()
            return "break"
        elif len(self.get()) >= max_length:
            self.bell()
            return "break"
        return None
