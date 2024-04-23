import json
import flet as ft

class Router:
    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": Home(page),
        }
        self.page.add(self.routes['/'])

    def route_change(self, route):
        self.page.controls.pop()
        self.page.add(self.routes[route.route])
        self.page.update()


def main(page: ft.Page):
    page.title = "Lista de Compras"
    page.window_width = 450
    page.window_height = 700
    page.window_max_width = 600
    page.window_max_height = 700
    page.window_min_width = 300
    page.window_min_height = 400
    page.window_always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.appbar = ft.AppBar(
        toolbar_height= 20,
        center_title=False,
        bgcolor=ft.colors.PINK_200,
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.LIST, label="Lista"),
            ft.NavigationDestination(icon=ft.icons.HELP, label="Ajuda"),
        ]
    )
    

    def remove(item):
        columnTela.controls.remove(item)
        page.update()  
        with open('itens.json', 'w') as f:
            itens = [str.capitalize(item.content.value) for item in columnTela.controls]
            json.dump(itens, f)


    def itemlista():
        item = ft.Container(            
            padding=ft.padding.only(left=10),
            on_click=lambda e: remove(item),
            alignment=ft.alignment.center_left,
            width=600,
            height=80,
            bgcolor=ft.colors.RED_100,
            border_radius=10,
            content=ft.Text(value=str.capitalize(TextField.value), size=20, text_align= ft.TextAlign.START),
            )
        return item

    def add(p):
        item = itemlista()
        if TextField.value != "":
            TextField.value = ""
            columnTela.controls.append(item)
            page.update()
            with open('itens.json', 'w') as f:
                itens = [str.capitalize(item.content.value) for item in columnTela.controls]
                json.dump(itens, f)
    
    
    TextField = ft.TextField(
        label="Digite o Items",
        bgcolor= "gray",
        border= ft.InputBorder.OUTLINE,
        border_radius= 20,
        border_color= ft.colors.GREY_100,
        on_submit=lambda p: add(p)
    )


    Btnadicionar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                on_click= lambda p: add(p),
                text="ADICIONAR",
                icon=ft.icons.ADD,
                color= ft.colors.PINK_200,
                width= 200,
                height= 50,
                ),
        ])
    
    
    ContainerTextField = ft.Container(content=TextField, padding= ft.padding.only(top=20), width=350)
    
    ContainerBtnAdd = ft.Container(content=Btnadicionar,padding= ft.padding.only(top=20,bottom=20) )

    columnTela = ft.Column(height= 300,expand= True, scroll= ft.ScrollMode.AUTO, width=400)

    
    page.add(ContainerTextField,ContainerBtnAdd,columnTela)

    try:
        with open('itens.json', 'r') as f:
            itens = json.load(f)
            for valor in itens:
                TextField.value = valor
                item = itemlista()
                columnTela.controls.append(item)
                TextField.value = ""
                page.update()
    except FileNotFoundError:
        pass

ft.app(main)
