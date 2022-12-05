import flet as ft


def main(page: ft.Page):
    page.title = 'CALCULATORATOR 3000'
    result = ft.Text(value=0)
    column = ft.Column(
        [
            ft.Row(controls=[result], alignment='end'),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="AC"),
                    ft.ElevatedButton(text="+/-"),
                    ft.ElevatedButton(text="%"),
                    ft.ElevatedButton(text="/"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="7"),
                    ft.ElevatedButton(text="8"),
                    ft.ElevatedButton(text="9"),
                    ft.ElevatedButton(text="*"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="4"),
                    ft.ElevatedButton(text="5"),
                    ft.ElevatedButton(text="6"),
                    ft.ElevatedButton(text="-"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="1"),
                    ft.ElevatedButton(text="2"),
                    ft.ElevatedButton(text="3"),
                    ft.ElevatedButton(text="+"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="0"),
                    ft.ElevatedButton(text="."),
                    ft.ElevatedButton(text="="),
                ]
            ),
        ]
    )
    cont = ft.Container(
        content=column,
        width=300,
        height=280,
        bgcolor=ft.colors.BLACK,

    )

    page.add(cont)


ft.app(target=main)
