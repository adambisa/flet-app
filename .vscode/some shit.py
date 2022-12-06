import flet as ft
import requests

def main(page: ft.Page):
    page.title = "TATEOSTERONE"

    def get_qoute(e):
        t.value = requests.get('https://hacker1.pythonanywhere.com/').json()['qoute']
        page.update()
    myimg=ft.Image(src=f'tate.jpg', fit=ft.ImageFit.FILL)
    b = ft.OutlinedButton("GET", on_click=get_qoute)
    t = ft.Text()

    page.add(b, t, myimg)
ft.app(target=main)