import time
from datetime import datetime
from typing import Dict, Tuple, Optional, Union

from ..types import WeekDaysStatistic


class WeekDaysCalculator:
    weekdays_map = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    def __init__(self, start_date: str, end_date: str) -> None:
        self.start_date = start_date
        self.end_date = end_date

    def count_control(self) -> Union[WeekDaysStatistic, ValueError, OverflowError]:
        try:
            result = self._count_weekdays(self.start_date, self.end_date)
        except ValueError as exception_message:
            return exception_message
        except OverflowError as exception_message:
            return exception_message
        return result

    def _count_weekdays(
            self, start_date_str: str, end_date_str: str
    ) -> Optional[WeekDaysStatistic]:
        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

        start_date, end_date = self._get_later_date(start_date, end_date)

        weekdays_count = {
            "Monday": 0,
            "Tuesday": 0,
            "Wednesday": 0,
            "Thursday": 0,
            "Friday": 0,
            "Saturday": 0,
            "Sunday": 0,
        }

        weekdays_count = self._summarize_days(
            start_date, end_date, weekdays_count, self.weekdays_map
        )[0]

        return weekdays_count

    @staticmethod
    def _get_later_date(
            start_date: datetime, end_date: datetime
    ) -> Tuple[datetime, datetime]:
        if start_date < end_date:
            return start_date, end_date
        return end_date, start_date

    @staticmethod
    def _summarize_days(
            start_date: datetime,
            end_date: datetime,
            weekdays_count: WeekDaysStatistic,
            weekdays_map: Dict[int, str],
    ) -> Tuple[WeekDaysStatistic, float]:
        start_time = time.perf_counter()
        day_diff = (end_date - start_date).days
        day_equal_num = day_diff // 7
        division_reminder = day_diff % 7
        start_week_number = start_date.weekday()
        start_week_name = weekdays_map[start_week_number]

        for key in weekdays_count:
            weekdays_count[key] += day_equal_num

        current_day_name = start_week_name
        weekday_keys = list(weekdays_map.values())
        for _ in range(division_reminder + 1):
            weekdays_count[current_day_name] += 1
            current_day_index = weekday_keys.index(current_day_name)
            current_day_name = weekday_keys[(current_day_index + 1) % 7]

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Performance: {execution_time} (s)")

        return weekdays_count, execution_time


import random
from dataclasses import dataclass
from typing import Dict

from ..types import DateOption


@dataclass
class DateRandomizer:
    MIN_DAY_VALUE: int = 1
    MIN_MONTH_VALUE: int = 1
    MAX_ALLOWED_DAY_VALUE: int = 28
    MAX_MONTH_VALUE: int = 12
    MIN_ALLOWED_YEAR_VALUE: int = 1000
    MAX_ALLOWED_YEAR_VALUE: int = 9999

    def randomize(self) -> Dict[DateOption, int]:
        option_dict = {
            DateOption.DAY: random.randint(
                self.MIN_DAY_VALUE, self.MAX_ALLOWED_DAY_VALUE
            ),
            DateOption.MONTH: random.randint(
                self.MIN_MONTH_VALUE, self.MAX_MONTH_VALUE
            ),
            DateOption.YEAR: random.randint(
                self.MIN_ALLOWED_YEAR_VALUE, self.MAX_ALLOWED_YEAR_VALUE
            ),
        }

        return option_dict
