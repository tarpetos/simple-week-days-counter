import flet as ft


class ToplevelDialog(ft.AlertDialog):
    def __init__(self, page: ft.Page, dialog_title: str, dialog_content: str) -> None:
        super().__init__()
        self.page = page
        self.dialog_title = dialog_title
        self.dialog_content = dialog_content
        self._build_dialog()

    def _build_dialog(self) -> None:
        dialog = ft.AlertDialog(
            title=ft.Text(self.dialog_title),
            content=ft.Text(self.dialog_content),
            actions=[
                ft.TextButton(
                    "Ok",
                    on_click=lambda _: (
                        setattr(dialog, "open", False),
                        self.page.update(),
                    ),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
