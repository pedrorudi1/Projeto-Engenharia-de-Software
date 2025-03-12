from tkinter import Tk, Canvas, Button, PhotoImage


App = Tk()
App.title("GFF Propagandas e Eventos")
App.geometry("1200x740")
App.iconbitmap(r"icon.ico")

FotoBG = PhotoImage(file=r"logo1.png")


canvas = Canvas(App, width=1200, height=740)
canvas.pack(fill="both", expand=True)
canvas.configure(bg='#3F3F64')

# Calcula as coordenadas para centralizar a imagem
canvas_width = 1200
canvas_height = 740
image_width = FotoBG.width()
image_height = FotoBG.height()
x = (canvas_width - image_width) // 2
y = (canvas_height - image_height) // 2

canvas.create_image(x, y, image=FotoBG, anchor="nw")

BtnClientes = Button(App, text='Cadastro de Clientes', font=("Arial", 12))
BtnClientes.place(x=52.0, y=60.0)
BtnControleFrota = Button(App, text='Controle de Frota', font=("Arial", 12))
BtnControleFrota.place(x=52.0, y=160.0)
BtnEventos = Button(App, text='Agenda de Eventos', font=("Arial", 12))
BtnEventos.place(x=52.0, y=260.0)
BtnManutencao = Button(App, text='Manutenção da Frota', font=("Arial", 12))
BtnManutencao.place(x=52.0, y=360.0)
BtnProdutosTerceiros = Button(App, text='Produtos de Terceiros', font=("Arial", 12))
BtnProdutosTerceiros.place(x=52.0, y=460.0)
BtnFuncionarios = Button(App, text='Cadastro de Funcionários', font=("Arial", 12))
BtnFuncionarios.place(x=52.0, y=560.0)
BtnEstoqueEquipamentos = Button(App, text='Estoque de Equipamentos', font=("Arial", 12))
BtnEstoqueEquipamentos.place(x=52.0, y=660.0)

App.resizable(False, False)

App.mainloop()