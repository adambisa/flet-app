import flet as ft
import requests


def main(page: ft.Page):
    page.title = "TATEOSTERONE"
    page.theme_mode = ft.ThemeMode.DARK
    page.auto_scroll=True
    def get_qoute(e):
        txt.value = requests.get(
            'https://hacker1.pythonanywhere.com/').json()['qoute']
        page.update()
    btn = ft.OutlinedButton("GET", on_click=get_qoute, )
    txt = ft.Text()
    img = ft.Image(
        src=f"https://www.insidesport.in/wp-content/uploads/2022/11/la-Andrew-Tate-rise-to-infamy-OFF-PLAT.jpg",
        fit=ft.ImageFit.CONTAIN,
    )
    R1 = ft.Row(controls=[ft.Text(value='TATEOSTERONE',size=100, color=ft.colors.WHITE, text_align='center')])
    txtcol=ft.Column([txt])
    btncol=ft.Column([btn])
    R2 = ft.Row(controls=[btncol,txtcol])
    R3 = ft.Row(controls=[ft.Text(
        value='made by a singular idiot inspired by multiple idiots')])
    col = ft.Column(
        [
            R1,
            R2,
            ft.Divider(height=1),
            R3
        ]
    )
    cont=ft.Container(content=col)
    page.add(cont)
ft.app(target=main)
