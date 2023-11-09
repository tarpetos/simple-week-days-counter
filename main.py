import tkinter as tk
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional, Union, Type, Literal, TypedDict


class DateOption(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


DateOptionString: Type = Literal[DateOption.DAY, DateOption.MONTH, DateOption.YEAR]


class PlaceholderEntry(tk.Entry):
    def __init__(
            self,
            master: Optional[Union[tk.Tk, tk.Frame]] = None,
            placeholder: str = "",
            *args,
            **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.on_entry_focus_in)
        self.bind("<FocusOut>", self.on_entry_focus_out)
        self.config(fg="grey")

    def on_entry_focus_in(self, event: tk.Event) -> None:
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg="black")

    def on_entry_focus_out(self, event: tk.Event) -> None:
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg="grey")


class DateEntry(PlaceholderEntry):
    DATE_LIMITS: Dict[str, int] = {
        "day": 31,
        "month": 12,
        "year": 9999,
    }

    def __init__(
            self, master: Optional[Union[tk.Tk, tk.Frame]] = None,
            date_option: Optional[DateOptionString] = None,
            *args,
            **kwargs
    ) -> None:
        super(master, *args, **kwargs).__init__(*args, **kwargs)
        super().__init__(master, *args, **kwargs)
        self.bind("<Key>", lambda event: self.on_key_pressed(event, date_option))

    def on_key_pressed(self, event: tk.Event, date_option: DateOptionString) -> Optional[str]:
        max_value = self.DATE_LIMITS[date_option.value]
        max_length = len(str(max_value))

        print(event.keycode)
        allowed_key_codes = (111, 113, 114, 116, 22, 23, 119)
        if event.keycode in allowed_key_codes:
            return None

        if max_length is not None and len(self.get()) >= max_length:
            self.bell()
            return "break"

        if event.char.isdigit():
            user_input = int(self.get() + event.char)
            if self.select_present() and user_input >= 1:
                return None

            if user_input > max_value or user_input < 1:
                self.bell()
                return "break"


class WeekDaysCounterApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Weekdays Counter")

        self.label_start_date = tk.Label(self, text="Enter start date:")
        self.start_input_date_frame = tk.Frame(self)
        self.label_start_day = tk.Label(self.start_input_date_frame, text="Day:")
        self.entry_start_day = DateEntry(
            self.start_input_date_frame,
            placeholder="1-31",
            date_option=DateOption.DAY,
            width=10
        )
        self.label_start_month = tk.Label(self.start_input_date_frame, text="Month:")
        self.entry_start_month = DateEntry(
            self.start_input_date_frame,
            placeholder="1-12",
            date_option=DateOption.MONTH,
            width=10
        )
        self.label_start_year = tk.Label(self.start_input_date_frame, text="Year:")
        self.entry_start_year = DateEntry(
            self.start_input_date_frame,
            placeholder="2000",
            date_option=DateOption.YEAR,
            width=10
        )

        self.label_end_date = tk.Label(self, text="Enter end date:")
        self.end_input_date_frame = tk.Frame(self)
        self.label_end_day = tk.Label(self.end_input_date_frame, text="Day:")
        self.entry_end_day = DateEntry(
            self.end_input_date_frame,
            placeholder="1-31",
            date_option=DateOption.DAY,
            width=10
        )
        self.label_end_month = tk.Label(self.end_input_date_frame, text="Month:")
        self.entry_end_month = DateEntry(
            self.end_input_date_frame,
            placeholder="1-12",
            date_option=DateOption.MONTH,
            width=10
        )
        self.label_end_year = tk.Label(self.end_input_date_frame, text="Year:")
        self.entry_end_year = DateEntry(
            self.end_input_date_frame,
            placeholder="2000",
            date_option=DateOption.YEAR,
            width=10
        )

        self.calculate_button = tk.Button(
            self, text="Calculate Weekdays", command=self.calculate_weekdays
        )
        self.result_text = tk.Text(self, height=7, state=tk.DISABLED)
        self.place_widgets()

    def place_widgets(self) -> None:
        self.label_start_date.pack()
        self.start_input_date_frame.pack()
        self.label_start_day.pack(side=tk.LEFT)
        self.entry_start_day.pack(side=tk.LEFT)
        # self.label_start_month.pack(side=tk.LEFT)
        # self.entry_start_month.pack(side=tk.LEFT)
        # self.label_start_year.pack(side=tk.LEFT)
        # self.entry_start_year.pack(side=tk.LEFT)

        # self.label_end_date.pack(pady=(20, 0))
        # self.end_input_date_frame.pack()
        # self.label_end_day.pack(side=tk.LEFT)
        # self.entry_end_day.pack(side=tk.LEFT)
        # self.label_end_month.pack(side=tk.LEFT)
        # self.entry_end_month.pack(side=tk.LEFT)
        # self.label_end_year.pack(side=tk.LEFT)
        # self.entry_end_year.pack(side=tk.LEFT)
        # self.calculate_button.pack(pady=20)
        self.result_text.pack()

    @staticmethod
    def count_weekdays_by_day(start_date_str: str, end_date_str: str) -> Dict[str, int]:
        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

        weekdays_count = {
            "Monday": 0,
            "Tuesday": 0,
            "Wednesday": 0,
            "Thursday": 0,
            "Friday": 0,
            "Saturday": 0,
            "Sunday": 0,
        }

        current_date = start_date
        while current_date <= end_date:
            weekdays_count[current_date.strftime("%A")] += 1
            current_date += timedelta(days=1)

        return weekdays_count

    def calculate_weekdays(self) -> None:
        start_date_input = "".join(
            f"{self.entry_start_day.get()}-"
            f"{self.entry_start_month.get()}-"
            f"{self.entry_start_year.get()}"
        )
        end_date_input = "".join(
            f"{self.entry_end_day.get()}-"
            f"{self.entry_end_month.get()}-"
            f"{self.entry_end_year.get()}"
        )

        result = self.count_weekdays_by_day(start_date_input, end_date_input)

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        for day, count in result.items():
            self.result_text.insert(tk.END, f"{day}: {count}\n")
        self.result_text.config(state=tk.DISABLED)

    def start(self) -> None:
        self.mainloop()


def main():
    app = WeekDaysCounterApp()
    app.start()


if __name__ == "__main__":
    main()
