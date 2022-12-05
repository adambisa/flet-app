import flet as ft


def main(page: ft.Page):
    page.title = 'CALCULATORATOR 3000'
    txtcol=ft.colors.WHITE
    numblack=ft.colors.BLACK54
    result = ft.Text(value=0, color=txtcol)
    
    column = ft.Column(
        [
            ft.Row(controls=[result]),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="AC", bgcolor=ft.colors.WHITE30,color=txtcol),
                    ft.ElevatedButton(text="+/-", bgcolor=ft.colors.WHITE30,color=txtcol),
                    ft.ElevatedButton(text="%", bgcolor=ft.colors.WHITE30,color=txtcol),
                    ft.ElevatedButton(text="/",bgcolor=ft.colors.WHITE30,color=txtcol),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="7",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="8",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="9",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="*", bgcolor=ft.colors.YELLOW_800,color=txtcol),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="4",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="5",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="6",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="-", bgcolor=ft.colors.YELLOW_800,color=txtcol),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="1",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="2",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="3",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="+", bgcolor=ft.colors.YELLOW_800,color=txtcol),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="0",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text=".",color=txtcol,bgcolor=numblack),
                    ft.ElevatedButton(text="=", bgcolor=ft.colors.YELLOW_800,color=txtcol),
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
