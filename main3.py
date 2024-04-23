import flet as ft


class Item(ft.Container):
    def __init__(self, page, value):
        super().__init__(
            padding=ft.padding.only(left=10),
            alignment=ft.alignment.center_left,
            width=600,
            height=80,
            bgcolor=ft.colors.RED_100,
            border_radius=10,
            content=ft.Text(value=str.capitalize(value), size=20, text_align= ft.TextAlign.START)
        )
        self.page = page
        self.on_click = self.remove

    def remove(self, e):
        # Use self para acessar a lista itens_adicionados
        self.page.remove(self)
        itens_adicionados.remove(self)


def main(page: ft.Page):
    page.title = "Lista de Compras"
    page.window_width = 450
    page.window_height = 700
    page.window_max_width = 600
    page.window_max_height = 700
    page.window_min_width = 300
    page.window_min_height = 400
    page.window_always_on_top = True

    global itens_adicionados
    itens_adicionados = []
    
    page.appbar = ft.AppBar(
        toolbar_height= 20,
        center_title=False,
        bgcolor=ft.colors.PINK_200,
    )


    def add(p):
        if entrada.value != "":
            item = Item(page, entrada.value)
            entrada.value = ""
            itens_adicionados.append(item)
            page.add(item)

    entrada = ft.TextField(
        label="Digite o Item",
        bgcolor= "gray",
        on_submit=add,
        border= ft.InputBorder.OUTLINE,
        border_radius= 20,
        border_color= ft.colors.GREY_100

        
        )

    Btnadicionar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                on_click=add,
                text="ADICIONAR",
                icon=ft.icons.ADD,
                color= ft.colors.PINK_200,
                width= 200,
                height= 50,
                
                
                ),
        ])

    containerentrada = ft.Container(content=entrada, padding= ft.padding.only(top = 20, left=10, right=10, bottom= 20), alignment= ft.alignment.center, )
    container = ft.Container()
    tela = ft.Column(data=container)

    page.add(
        containerentrada,
        Btnadicionar,
        tela
    )


ft.app(main)
