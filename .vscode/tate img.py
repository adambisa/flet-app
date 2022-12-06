import flet as ft
import requests

def main(page: ft.Page):
    page.title = "TATEOSTERONE"
    page.theme_mode = ft.ThemeMode.DARK
    def get_qoute(e):
        t.value = requests.get('https://hacker1.pythonanywhere.com/').json()['qoute']
        page.update()
    b = ft.OutlinedButton("GET", on_click=get_qoute)
    t = ft.Text()
    img = ft.Image(
        src=f"https://www.insidesport.in/wp-content/uploads/2022/11/la-Andrew-Tate-rise-to-infamy-OFF-PLAT.jpg",
        fit=ft.ImageFit.FILL,
    )

    page.add(img, b,t)
ft.app(target=main)