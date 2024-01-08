# Bibliotecas

import tkinter as tk
from tkinter.font import Font
from datetime import datetime
import requests
from tkinter import messagebox
import time

# Função para ajustar a janela principal conforme o conteudo que estiver nela
def ajustar_janela_ao_conteudo():
    global janela
    root = janela

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
    root.geometry(f"{largura+20}x{altura}+{x_pos-50}+{y_pos-120}")

# Função que ira obter o horario completo de brasilia
# Com data e tudo
def obter_horario_brasilia():
    try:
        # Especifica o fuso horário para Brasília
        response = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
        dados = response.json()
        horario_brasilia = dados['datetime']

        objeto_datetime = datetime.strptime(horario_brasilia,"%Y-%m-%dT%H:%M:%S.%f%z")

        return objeto_datetime
    
    except:
        msg_erro = ('Erro ao consultar o horário de Brasília', 'Verifique sua Internet!')
        return msg_erro

# Ira buscar no retorno da função obter_horario_brasilia
# Apenas as horas, minutos e segundos
def buscar_horario():
    try:
        horario_completo = obter_horario_brasilia()

        hora = horario_completo.hour
        minutos = f'{horario_completo.minute:02d}'
        segundos = f'{horario_completo.second:02d}'

        horario = f'{hora}:{minutos}:{segundos}'

        return horario
    
    # Caso de errado é sinal de que esta sem internet
    except:
        return obter_horario_brasilia()[1]

# Assim como na função a cima, mas ira retornar a data
def buscar_data():
    try:
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
        dia_semana_numero = horario_completo.weekday() # retorna um indice
        dia_semana_escrito = dia_semana_list[dia_semana_numero] # busca pelo indice da lista onde contem os dias da semana

        dia = str(horario_completo.day)
        
        mes_numero = str(horario_completo.month)
        mes_escrito = meses_dict[mes_numero]
        
        ano = str(horario_completo.year)

        # Formatação final que ira aparecer na label
        data = f'{dia_semana_escrito}, {dia} de {mes_escrito} de {ano}'

        return data
    
    # Retorno da msg de erro
    except:
        return obter_horario_brasilia()[0]

# Função que ira atualizar a label a cada 1 segundo
def atualizar_label():
    global label_horario
    global label_data

    try:
        label_horario.config(text=buscar_horario())
        label_data.config(text=buscar_data())

        # Para que não fique pulando e ocasione Delay
        # Calcula o tempo restante até o próximo segundo
        milissegundos_restantes = 1000 - int(time.time() * 1000) % 1000

        # Agenda a próxima atualização após o tempo restante
        janela.after(milissegundos_restantes, atualizar_label)
        janela.after(900, ajustar_janela_ao_conteudo)
        
    except:
        janela.after(900, atualizar_label)
        janela.after(900, ajustar_janela_ao_conteudo)

# Janela Principal do Relógio
janela = tk.Tk()

# Titulo da janela
janela.title('Horário de Brasília')

# Fontes personalizadas
fonte_data = Font(size=16, weight="bold")
fonte_horario = Font(size=24, weight="bold")


# Label da data
label_data = tk.Label(janela, text='', font=fonte_data)
label_data.pack(pady=5)

# Label do horario
label_horario = tk.Label(janela, text='', font=fonte_horario)
label_horario.pack(pady=5)

# Chama as funções de atualização de label e de tamanho da janela
atualizar_label()
ajustar_janela_ao_conteudo()

janela.mainloop()