import flet as ft
import requests

def main(page: ft.Page):
    def get_data():
        resp=requests.get('https://hacker1.pythonanywhere.com/')
        text=resp.json()['qoute']
        txt.value=text
    txt=ft.Text()
    
    btn=ft.FilledTonalButton(
            text="Get inspired",
            on_click=get_data)
    myimg=ft.Image(src='/tate.jpg', fit=ft.ImageFit.FILL)
    page.add(
        btn ,
        txt
        )

ft.app(target=main)