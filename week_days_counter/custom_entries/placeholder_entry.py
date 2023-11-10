import tkinter as tk
from typing import Optional

from ..types import Window


class PlaceholderEntry(tk.Entry):
    def __init__(
        self, master: Optional[Window] = None, placeholder: str = "", *args, **kwargs
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
