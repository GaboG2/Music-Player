import flet as ft
import flet_audio as fta

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.run(main = main, assets_dir = "assets")