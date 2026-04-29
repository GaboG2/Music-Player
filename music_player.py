import flet as ft
import flet_audio as fta

builtin_tracks = [
    {"name": "Ifertehno", "src": "assets/audio/Ifertehno.mp3"},
    {"name": "Operation Evolution", "src": "assets/audio/Operation Evolution.mp3"},
    {"name": "Sphere", "src": "assets/audio/Sphere.mp3"},
    {"name": "These Mistakes are Mine Alone", "src": "assets/audio/These Mistakes are Mine Alone.mp3"},
]
def main(page: ft.Page):
    track_number = 0

    async def play(e):
        await music.play()
    
    async def pause(e):
        await music.pause()
    
    async def resume(e):
        await music.resume()
    
    def next_song(e):
        nonlocal track_number

        if track_number == len(builtin_tracks) - 1:
            track_number = 0
        else:
            track_number += 1
        
        music.src = builtin_tracks[track_number]["src"]
        track_info_text.value = f"Track {track_number + 1}: {builtin_tracks[track_number]["name"]}"

    def previous_song(e):
        nonlocal track_number

        if track_number == 0:
            track_number = len(builtin_tracks) - 1
        else:
            track_number -= 1
        
        music.src = builtin_tracks[track_number]["src"]
        track_info_text.value = f"Track {track_number + 1}: {builtin_tracks[track_number]["name"]}"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    music = fta.Audio(src = builtin_tracks[track_number]["src"])

    play_button = ft.Button(content = "▶", on_click = play)
    pause_button = ft.Button(content = "II", on_click = pause)
    resume_button = ft.Button(content = "Resume", on_click = resume)
    next_song_button = ft.Button(content = "▶I", on_click = next_song)
    previous_song_button = ft.Button(content = "I◀", on_click = previous_song)

    track_info_text = ft.Text(f"Track {track_number + 1}: {builtin_tracks[track_number]["name"]}")

    page.add(
        track_info_text,
        ft.Row(
            controls = [previous_song_button, play_button, resume_button, pause_button, next_song_button],
            alignment = page.horizontal_alignment
        )
    )

ft.run(main = main, assets_dir = "assets")