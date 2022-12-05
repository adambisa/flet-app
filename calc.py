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
    #no init cause inheritance

    def build(self):
        textcol=colors.WHITE
        self.textcol=textcol
        result=Text(value=0,color=self.textcol, size=20)
        
        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                [
                    Row(controls=[ElevatedButton(text='AC'), ElevatedButton(text='+/-'), ElevatedButton(text='%'), ElevatedButton(text='/')])
                ]
                
            )
        )
def main(page:Page):
    page.title = "Calc App"
    # create application instance
    calc = CalcApp()

    # add application's root control to the page
    page.add(calc)


flet.app(target=main)