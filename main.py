from tkinter import * 
import random
import pandas


fundo = '#B1DDC6'
file = pandas.read_csv('palavras.csv')
lista = file.to_dict(orient='records')
carta_atual = {}
carta_aprender = {}

def proxima_carta():
    global carta_atual
    canvas.itemconfig(imagem, image=card_back)
    carta_atual = random.choice(lista)
    canvas.itemconfig(titulo, text='English', fill='black')
    canvas.itemconfig(tradução, text=carta_atual['English'],fill='black')
    tela.after(3000, virar_carta)

def virar_carta():
    canvas.itemconfig(imagem, image=card_front)
    canvas.itemconfig(titulo, text='Português')
    canvas.itemconfig(tradução, text=carta_atual['Português'] )


# Tela
tela = Tk()
tela.title('Flash Card')
tela.config(padx=50,pady=50, bg='#B1DDC6')

# Imagens/Textos
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=fundo)
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')

imagem = canvas.create_image(400, 263, image=card_back)
titulo = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
tradução = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=fundo, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Botões
botao1 = hotoImage(file='images/right.png')
botao_right = Button(image=botao1, highlightthickness=0, command=proxima_carta)
botao_right.config(padx=20, pady=20)
botao_right.grid(column=1, row=1)

botao2 = PhotoImage(file='images/wrong.png')
botao_wrong = Button(image=botao2, highlightthickness=0, command=proxima_carta)
botao_wrong.config(padx=20, pady=20)
botao_wrong.grid(column=0, row=1)

proxima_carta()

mainloop()
