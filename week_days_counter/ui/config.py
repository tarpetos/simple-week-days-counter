import flet as ft


class WindowConfig:
    APP_TITLE = "Week Days Counter"
    WIDTH = 1200
    HEIGHT = 900
    PADDING = 20

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = self.APP_TITLE
        self.page.window_width = self.WIDTH
        self.page.window_height = self.HEIGHT
        self.page.window_min_width = self.WIDTH
        self.page.window_min_height = self.HEIGHT
        self.page.update()
        self.page.padding = self.PADDING
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.page.dark_theme = ft.Theme(color_scheme_seed=ft.colors.CYAN)
        self.page.update()
