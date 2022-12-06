import flet as ft
import requests
#TODO spacing qoutes to be readable, footer strech, design better button, music


def main(page: ft.Page):
    def get_qoute(e):
        txt.value = requests.get(
            'https://hacker1.pythonanywhere.com/').json()['qoute']
        page.update()
    btn = ft.ElevatedButton(
        "GET INSPIRED", on_click=get_qoute, bgcolor=ft.colors.BLACK)
    txt = ft.Text(color=ft.colors.WHITE, weight='bold', size=26,
                  no_wrap=False, text_align=ft.TextAlign.JUSTIFY)
    st = ft.Stack(
        [
            ft.Image(
                src=f"https://fasterliving.com/wp-content/uploads/2022/06/Thumbnail@0.33x-1-scaled.jpg",
                fit=ft.ImageFit.FILL
            ),
            ft.Column(
                [ft.Row(
                    [
                        ft.Text(
                            "TATEOSTERONE",
                            color="white",
                            size=70,
                            weight="bold",
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                    ft.Row(
                    [ft.Column([btn]),],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                    ft.Container(content=ft.Row(
                        [ft.Column([txt]),],
                        alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END
                    ), bgcolor=ft.colors.BLACK87, height=200, width=1300, opacity=0.65, shape=ft.BoxShape.RECTANGLE),
                    ft.Container(content=ft.Row([ft.Text("made by a idiot inspired by other idiots", color=ft.colors.WHITE)], ), bgcolor=ft.colors.BLACK, margin=250, width=1300, height=50
                                 )

                ]

            ),

        ],

    )

    page.add(st)


ft.app(target=main)
