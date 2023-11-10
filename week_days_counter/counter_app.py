import random
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox
from typing import Dict, Optional, Tuple

from .custom_entries import DateEntry
from .types import DateOption, EntryFrameOption, DateFrame, LabelFramePadding


class WeekDaysCounterApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Weekdays Counter")

        start_frame = self.build_date_frame("start")
        self.label_start_date = start_frame["frame"]
        self.start_input_date_frame = start_frame["frame_name"]
        self.label_start_day = start_frame["labels"][0]
        self.entry_start_day = start_frame["entries"][0]
        self.label_start_month = start_frame["labels"][1]
        self.entry_start_month = start_frame["entries"][1]
        self.label_start_year = start_frame["labels"][2]
        self.entry_start_year = start_frame["entries"][2]

        end_frame = self.build_date_frame("end")
        self.label_end_date = end_frame["frame"]
        self.end_input_date_frame = end_frame["frame_name"]
        self.label_end_day = end_frame["labels"][0]
        self.entry_end_day = end_frame["entries"][0]
        self.label_end_month = end_frame["labels"][1]
        self.entry_end_month = end_frame["entries"][1]
        self.label_end_year = end_frame["labels"][2]
        self.entry_end_year = end_frame["entries"][2]

        self.buttons_frame = tk.Frame(self)
        self.calculate_button = tk.Button(
            self.buttons_frame,
            text="Calculate week days",
            command=self.calculate_weekdays,
        )
        self.randomize_button = tk.Button(
            self.buttons_frame,
            text="Calculate randomize entries",
            command=self.randomize_entries,
        )

        self.result_text = tk.Text(self, height=7, state=tk.DISABLED)

        self.place_date_frame_widgets(start_frame)
        self.place_date_frame_widgets(end_frame, name_padding=(20, 0))
        self.place_widgets()

    def build_date_frame(self, entry_frame_option: EntryFrameOption) -> DateFrame:
        label_date = tk.Label(self, text=f"Enter {entry_frame_option} date:")
        input_date_frame = tk.Frame(self)
        label_day = tk.Label(input_date_frame, text="Day:")
        entry_day = DateEntry(
            input_date_frame, placeholder="1-31", date_option=DateOption.DAY, width=10
        )
        label_month = tk.Label(input_date_frame, text="Month:")
        entry_month = DateEntry(
            input_date_frame, placeholder="1-12", date_option=DateOption.MONTH, width=10
        )
        label_year = tk.Label(input_date_frame, text="Year:")
        entry_year = DateEntry(
            input_date_frame, placeholder="2000", date_option=DateOption.YEAR, width=10
        )
        return {
            "frame": input_date_frame,
            "frame_name": label_date,
            "labels": [label_day, label_month, label_year],
            "entries": [entry_day, entry_month, entry_year],
        }

    @staticmethod
    def place_date_frame_widgets(
        date_frame: DateFrame, name_padding: Optional[LabelFramePadding] = None
    ) -> None:
        date_frame["frame_name"].pack(pady=name_padding if name_padding else 0)
        date_frame["frame"].pack()

        for label_entry in range(len(date_frame["labels"])):
            date_frame["labels"][label_entry].pack(side=tk.LEFT)
            date_frame["entries"][label_entry].pack(side=tk.LEFT)

    def place_widgets(self) -> None:
        self.buttons_frame.pack(pady=20)
        self.calculate_button.pack(side=tk.LEFT)
        self.randomize_button.pack(side=tk.LEFT)
        self.result_text.pack()

    @staticmethod
    def randomize_entry(entry: tk.Entry, date_option: DateOption) -> None:
        entry.delete(0, tk.END)

        option_dict = {
            DateOption.DAY: random.randint(1, 28),
            DateOption.MONTH: random.randint(1, 12),
            DateOption.YEAR: random.randint(1000, 4000),
        }

        entry.insert(0, str(option_dict[date_option]))
        entry.config(fg="black")

    def randomize_entries(self) -> None:
        self.randomize_entry(self.entry_start_day, DateOption.DAY)
        self.randomize_entry(self.entry_start_month, DateOption.MONTH)
        self.randomize_entry(self.entry_start_year, DateOption.YEAR)
        self.randomize_entry(self.entry_end_day, DateOption.DAY)
        self.randomize_entry(self.entry_end_month, DateOption.MONTH)
        self.randomize_entry(self.entry_end_year, DateOption.YEAR)

    @staticmethod
    def get_later_date(
        start_date: datetime, end_date: datetime
    ) -> Tuple[datetime, datetime]:
        if start_date < end_date:
            return start_date, end_date
        return end_date, start_date

    def count_weekdays_by_day(
        self, start_date_str: str, end_date_str: str
    ) -> Optional[Dict[str, int]]:
        try:
            start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
            end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
        except ValueError as e:
            print(e)
            messagebox.showerror(title="Invalid date", message=f"{str(e).capitalize()}")
            return None

        start_date, end_date = self.get_later_date(start_date, end_date)

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

    @staticmethod
    def build_entry(*entries) -> str:
        return "-".join(entry.get() for entry in entries)

    def calculate_weekdays(self) -> None:
        start_date_input = self.build_entry(
            self.entry_start_day, self.entry_start_month, self.entry_start_year
        )
        end_date_input = self.build_entry(
            self.entry_end_day, self.entry_end_month, self.entry_end_year
        )

        result = self.count_weekdays_by_day(start_date_input, end_date_input)
        if result is None:
            return None

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        for day, count in result.items():
            self.result_text.insert(tk.END, f"{day}: {count}\n")
        self.result_text.config(state=tk.DISABLED)

    def start(self) -> None:
        self.mainloop()
