from enum import Enum

from typing import Type, Literal, Dict, Tuple


class DateOption(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


DateOptionString: Type = Literal[DateOption.DAY, DateOption.MONTH, DateOption.YEAR]

DateLimitOption: Type = Literal["day", "month", "year"]
DateLimits: Type = Dict[DateLimitOption, Tuple[int, int]]
EntryFrameOption: Type = Literal["start", "end"]
LabelFramePadding: Type = Tuple[int, int]
WeekDaysStatistic: Type = Dict[str, int]
