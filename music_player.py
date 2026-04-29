import flet as ft
import flet_audio as fta

builtin_tracks = [
    {"name": "Ifertehno", "source": "assets/audio/Ifertehno.mp3"},
    {"name": "Operation Evolution", "source": "assets/audio/Operation Evolution.mp3"},
    {"name": "Sphere", "source": "assets/audio/Sphere.mp3"},
    {"name": "These Mistakes are Mine Alone", "source": "assets/audio/These Mistakes are Mine Alone.mp3"},
]

def main(page: ft.Page):
    async def play(e):
        await music.play()
    
    async def pause(e):
        await music.pause()
    
    async def resume(e):
        await music.resume()
    
    async def next_song(e):
        pass

    async def previous_song(e):
        pass

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    music = fta.Audio(src = "assets/audio/Sphere.mp3")
    play_button = ft.Button(content = "Play", on_click = play)
    pause_button = ft.Button(content = "Pause", on_click = pause)
    resume_button = ft.Button(content = "resume", on_click = resume)
    next_song_button = ft.Button(content = "Next", on_click = next_song)
    previous_song_button = ft.Button(content = "Previous", on_click = previous_song)

    page.add(
        ft.Row(
            controls = [play_button, pause_button, next_song_button, previous_song_button],
            alignment = page.horizontal_alignment
        )
    )

ft.run(main = main, assets_dir = "assets")