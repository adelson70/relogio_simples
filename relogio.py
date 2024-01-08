# Bibliotecas

import tkinter as tk
from tkinter.font import Font
from datetime import datetime

# Função para ajustar a janela principal conforme o conteudo que estiver nela
def ajustar_janela_ao_conteudo(root):
    root.update_idletasks()  # Atualiza a geometria da janela
    largura = root.winfo_reqwidth()  # Largura requisitada pelo conteúdo
    altura = root.winfo_reqheight()  # Altura requisitada pelo conteúdo

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula a posição para centralizar a janela
    x_pos = (largura_tela - largura) // 2
    y_pos = (altura_tela - altura) // 2

    # Define a geometria da janela
    root.geometry(f"{largura+200}x{altura}+{x_pos-50}+{y_pos-120}")

def buscar_horario():
    ...

def buscar_data():
    ...


# Janela Principal do Relógio
janela = tk.Tk()

# Titulo da janela
janela.title('Relógio Simples')
ajustar_janela_ao_conteudo(janela)

janela.mainloop()