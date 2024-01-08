# Bibliotecas

import tkinter as tk
from tkinter.font import Font
from datetime import datetime
import requests
from tkinter import messagebox

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

def obter_horario_brasilia():
    try:
        # Especifica o fuso horário para Brasília
        response = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
        dados = response.json()
        horario_brasilia = dados['datetime']

        objeto_datetime = datetime.strptime(horario_brasilia,"%Y-%m-%dT%H:%M:%S.%f%z")

        return objeto_datetime
    
    except:
        return messagebox.showerror('Erro','Erro ao consultar o horário de Brasília, Verifique sua Internet!')

def buscar_horario():
    horario_completo = obter_horario_brasilia()

    hora = horario_completo.hour
    minutos = horario_completo.minute
    segundos = horario_completo.second

    horario = f'{hora}:{minutos}:{segundos}'

    return horario

def buscar_data():
    horario_completo = obter_horario_brasilia()

    meses_dict = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}
    dia_semana_list = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    dia_semana_numero = horario_completo.weekday()
    dia_semana_escrito = dia_semana_list[dia_semana_numero]

    dia = str(horario_completo.day)
    
    mes_numero = str(horario_completo.month)
    mes_escrito = meses_dict[mes_numero]
    
    ano = str(horario_completo.year)

    # Formatação final
    data = f'{dia_semana_escrito}, {dia} de {mes_escrito} de {ano}'

    return data


# Janela Principal do Relógio
janela = tk.Tk()

# Titulo da janela
janela.title('Relógio Simples')
ajustar_janela_ao_conteudo(janela)

janela.mainloop()