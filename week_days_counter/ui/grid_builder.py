import flet as ft


class GridBuilder:
    ROW_SPACING = 20
    COLUMN_SPACING = 50

    def build_row(self, *controls: ft.Control) -> ft.Row:
        return ft.Row(
            controls=[*controls],
            spacing=self.ROW_SPACING,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def build_column(self, *controls: ft.Control) -> ft.Column:
        return ft.Column(
            controls=[*controls],
            spacing=self.COLUMN_SPACING,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
