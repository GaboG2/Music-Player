import flet as ft
import flet_audio as fta

def main(page: ft.Page):
    def play_pause(e):
        pass
    
    def next_song(e):
        pass

    def previous_song(e):
        pass

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    play_pause_button = ft.Button(content = "Play", on_click = play_pause)
    next_song_button = ft.Button(content = "Next", on_click = next_song)
    previous_song_button = ft.Button(content = "Previous", on_click = previous_song)


ft.run(main = main, assets_dir = "assets")