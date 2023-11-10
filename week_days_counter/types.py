import tkinter as tk
from enum import Enum

from typing import Type, Union, Literal, Dict, List, Tuple

Window: Type = Union[tk.Tk, tk.Frame]


class DateOption(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


DateOptionString: Type = Literal[DateOption.DAY, DateOption.MONTH, DateOption.YEAR]

DateLimitOption: Type = Literal["day", "month", "year"]
DateLimits: Type = Dict[DateLimitOption, Tuple[int, int]]
EntryFrameOption: Type = Literal["start", "end"]
DateFrame: Type = Dict[str, Union[tk.Frame, tk.Label, List[tk.Label], List[tk.Entry]]]
LabelFramePadding: Type = Tuple[int, int]
