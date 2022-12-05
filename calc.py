import flet
from flet import (
    ElevatedButton,
    Row,
    Column,
    Container,
    Page,
    Text,
    UserControl,
    colors,
    border_radius
)


class CalcApp(UserControl):
    # no init cause inheritance

    def build(self):
        textcol = colors.WHITE
        btextcol = colors.BLACK
        contrcol = colors.ORANGE_500
        topcol = colors.WHITE30
        result = Text(value=0, color=textcol, size=20)
        self.result = result

        return Container(
            width=315,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                [
                    Row(controls=[result], alignment='end'),
                    Row(controls=[ElevatedButton(text='AC', bgcolor=topcol, color=textcol), ElevatedButton(text='+/-', bgcolor=topcol, color=textcol),
                        ElevatedButton(text='%', bgcolor=topcol, color=textcol), ElevatedButton(text='/', bgcolor=contrcol, color=textcol)]),
                    Row(controls=[ElevatedButton(text='7', color=btextcol), ElevatedButton(text='8', color=btextcol), ElevatedButton(
                        text='9', color=btextcol), ElevatedButton(text='*', bgcolor=contrcol, color=textcol)]),
                    Row(controls=[ElevatedButton(text='4', color=btextcol), ElevatedButton(text='5', color=btextcol), ElevatedButton(
                        text='6', color=btextcol), ElevatedButton(text='-', bgcolor=contrcol, color=textcol)]),
                    Row(controls=[ElevatedButton(text='1', color=btextcol), ElevatedButton(text='2', color=btextcol), ElevatedButton(
                        text='3', color=btextcol), ElevatedButton(text='+', bgcolor=contrcol, color=textcol)]),
                    Row(controls=[ElevatedButton(text='0', color=btextcol, expand=2), ElevatedButton(
                        text='.', color=btextcol), ElevatedButton(text='=', color=btextcol)])
                ]
            )
        )

    def button_clicked():
        pass


def main(page: Page):
    page.title = "Calc App"
    # create application instance
    calc = CalcApp()

    # add application's root control to the page
    page.add(calc)


flet.app(target=main)
