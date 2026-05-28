#importação das bibliotecas necessárias
#importação do customtkinter para a interface gráfica
#importação do messagebox para exibir mensagens de erro
import customtkinter as ctk
from tkinter import messagebox 

# configuração de aparência
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

# JANELA PRINCIPAL
window = ctk.CTk()
window.geometry("600x680") 

#TÍTULO PRINCIPAL
titulo = ctk.CTkLabel( 
    window,
    text="💰CALCULADORA FINANCEIRA💰",
    font=("Segoe UI", 24, "bold"),
    text_color="#D4AF37"
)
titulo.pack(pady=20)

# Abas para as diferentes funcionalidades
tabview = ctk.CTkTabview(window, width=450, text_color="#D4AF37")
tabview.pack(pady=10)

tab_porcentagem = tabview.add("Porcentagem")
tab_jurossimples = tabview.add("Juros Simples")
tab_juroscompostos = tabview.add("Juros Compostos")
tab_aumentodesalario = tabview.add("Aumento de Salário")
tab_descontos = tabview.add("Desconto de Salário")

# FUNÇÃO PARA CALCULAR PORCENTAGEM

label_valor = ctk.CTkLabel(tab_porcentagem, text="VALOR:", font=("Segoe UI", 15), text_color="#D4AF37")
label_valor.pack(pady=(10, 2))

entry_valor = ctk.CTkEntry(tab_porcentagem, width=200,)
entry_valor.pack(pady=(2, 10))

label_porcentagem_p = ctk.CTkLabel(tab_porcentagem, text="PORCENTAGEM (%):", font=("Segoe UI", 15), text_color="#D4AF37")
label_porcentagem_p.pack(pady=(10, 2))

entry_porcentagem_p = ctk.CTkEntry(tab_porcentagem, width=200, )
entry_porcentagem_p.pack(pady=(2, 10))

label_resultado_p = ctk.CTkLabel(tab_porcentagem, text="RESULTADO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_resultado_p.pack(pady=10) 

def calcular_porcentagem():
    try:
        valor = float(entry_valor.get())
        porcentagem = float(entry_porcentagem_p.get())

        resultado = valor * porcentagem / 100

        label_resultado_p.configure(
            text=f"RESULTADO: {resultado:.2f}", font=("Segoe UI", 15), text_color="#D4AF37"
        )
    except ValueError:  
        messagebox.showerror("Erro", "Digite valores válidos!")

botao_calcular = ctk.CTkButton(tab_porcentagem, text="Calcular", command=calcular_porcentagem)
botao_calcular.pack(pady=10) 


#FUNÇÃO PARA CALCULAR JUROS SIMPLES

label_capital_js = ctk.CTkLabel(tab_jurossimples, text="CAPITAL INICIAL:", font=("Segoe UI", 15), text_color="#D4AF37")
label_capital_js.pack(pady=(10, 2))

entry_capitalInicial = ctk.CTkEntry(tab_jurossimples, width=200,)
entry_capitalInicial.pack(pady=(2, 10))

label_taxa_js = ctk.CTkLabel(tab_jurossimples, text="TAXA:", font=("Segoe UI", 15), text_color="#D4AF37")
label_taxa_js.pack(pady=(10, 2))

entry_taxa = ctk.CTkEntry(tab_jurossimples, width=200)
entry_taxa.pack(pady=(2, 10))

label_tempo_js = ctk.CTkLabel(tab_jurossimples, text="TEMPO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_tempo_js.pack(pady=(10, 2))

entry_tempo = ctk.CTkEntry(tab_jurossimples, width=200)
entry_tempo.pack(pady=(2, 10))

opcao_tempo = ctk.CTkOptionMenu(
    tab_jurossimples,
    values=["Dias", "Meses", "Anos"]
)
opcao_tempo.pack(pady=8)
opcao_tempo.set("Anos")

label_resultado_js = ctk.CTkLabel(tab_jurossimples, text="")
label_resultado_js.pack(pady=10)

def calcular_juros_simples():
    try:
        capitalInicial = float(entry_capitalInicial.get())
        taxa = float(entry_taxa.get()) / 100
        tempo = float(entry_tempo.get())

        unidade = opcao_tempo.get()

        if unidade == "Meses":
            tempo = tempo / 12
        elif unidade == "Dias":
            tempo = tempo / 365 

        juros = capitalInicial * taxa * tempo
        montante = capitalInicial + juros

        label_resultado_js.configure(
            text=f"Juros:R$ {juros:.2f}\nMontante: R$ {montante:.2f}", text_color="#DAB007", font=("Segoe UI", 18, "bold")
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos!")

botao_jurossimples = ctk.CTkButton(
    tab_jurossimples,
    text="Calcular",
    command=calcular_juros_simples
) 
botao_jurossimples.pack(pady=10)



#FUNÇÃO PARA CALCULAR JUROS COMPOSTOS

label_capital_jc = ctk.CTkLabel(tab_juroscompostos, text="CAPITAL INICIAL:", font=("Segoe UI", 15), text_color="#D4AF37")
label_capital_jc.pack(pady=(10, 2))

entry_capitalInicialcompostos = ctk.CTkEntry(tab_juroscompostos, width=200)
entry_capitalInicialcompostos.pack(pady=(2, 10))

label_taxa_jc = ctk.CTkLabel(tab_juroscompostos, text="TAXA (% ao ano):", font=("Segoe UI", 15), text_color="#D4AF37")
label_taxa_jc.pack(pady=(10, 2))

entry_taxacompostos = ctk.CTkEntry(tab_juroscompostos, width=200)
entry_taxacompostos.pack(pady=(2, 10))

label_tempo_jc = ctk.CTkLabel(tab_juroscompostos, text="TEMPO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_tempo_jc.pack(pady=(10, 2))

entry_tempocompostos = ctk.CTkEntry(tab_juroscompostos, width=200)
entry_tempocompostos.pack(pady=(2, 10))

opcao_tempocompostos  = ctk.CTkOptionMenu(
    tab_juroscompostos,
    values=["Dias", "Meses", "Anos"]
)
opcao_tempocompostos.pack(pady=8)
opcao_tempocompostos.set("Anos")

label_resultado_jc = ctk.CTkLabel(tab_juroscompostos, text="", font=("Segoe UI", 15))
label_resultado_jc.pack(pady=(10, 2))
 
def calcular_juros_compostos():
    try:
        capitalInicial = float(entry_capitalInicialcompostos.get())
        taxa = float(entry_taxacompostos.get()) / 100
        tempo = float(entry_tempocompostos.get())

        unidade = opcao_tempocompostos.get()

        if unidade == "Meses":
            tempo = tempo / 12
        elif unidade == "Dias":
            tempo = tempo / 365

        montante = capitalInicial * (1 + taxa) ** tempo
        juros = montante - capitalInicial

        label_resultado_jc.configure(
            text=f"Juros: R$ {juros:.2f}\nMontante: R$ {montante:.2f}", text_color="#D4AF37"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos")

botao_juroscompostos = ctk.CTkButton(
    tab_juroscompostos,
    text="Calcular",
    command=calcular_juros_compostos
)
botao_juroscompostos.pack(pady=10)

def limpar_jc():
   entry_capitalInicialcompostos.delete(0, "end")
   entry_taxacompostos.delete(0, "end")
   entry_tempocompostos.delete(0, "end")
    
   label_resultado_jc.configure(text="")

botao_limpar_jc = ctk.CTkButton(
    tab_juroscompostos,
    text="Limpar",
    command=limpar_jc,
    fg_color="#8B0000",  # vermelho escuro
    hover_color="#A52A2A"
)
botao_limpar_jc.pack(pady=5)


# FUNÇÃO PARA CALCULAR AUMENTO SALARIAL  

label_salario = ctk.CTkLabel(tab_aumentodesalario, text="SALÁRIO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_salario.pack(pady=(10, 2))

entry_salario = ctk.CTkEntry(tab_aumentodesalario, width=200)
entry_salario.pack(pady=(2, 10))

label_porcentagem_salario = ctk.CTkLabel(tab_aumentodesalario, text="PORCENTAGEM (%):", font=("Segoe UI", 15), text_color="#D4AF37")
label_porcentagem_salario.pack(pady=(10, 2))

entry_porcentagem_salario = ctk.CTkEntry(tab_aumentodesalario, width=200)
entry_porcentagem_salario.pack(pady=(2, 10))

label_resultado_aumento = ctk.CTkLabel(tab_aumentodesalario, text="RESULTADO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_resultado_aumento.pack(pady=(10, 2))


def calcular_aumento_salarial():
    try:
        salario = float(entry_salario.get())
        porcentagem = float(entry_porcentagem_salario.get())

        aumento= salario * porcentagem / 100
        novo_salario= salario + aumento

        label_resultado_aumento.configure(text=f"Aumento de R$ {aumento:.2f}\nNovo Salário: R$ {novo_salario:.2f}")
    except ValueError:  
        messagebox.showerror("Erro", "Digite valores válidos!")

botao_calcular = ctk.CTkButton(tab_aumentodesalario, text="Calcular Aumento", command=calcular_aumento_salarial)
botao_calcular.pack(pady=10) 

def limpar_jc():
   entry_salario.delete(0, "end")
   entry_porcentagem_salario.delete(0, "end")
   label_resultado_aumento.configure(text="")

botao_limpar_jc = ctk.CTkButton(
    tab_aumentodesalario,
    text="Limpar",
    command=limpar_jc,
    fg_color="#8B0000",  # vermelho escuro
    hover_color="#A52A2A"
)
botao_limpar_jc.pack(pady=5)



    # FUNÇÃO PARA CALCULAR DESCONTO DE SALÁRIO

label_salariodes = ctk.CTkLabel(tab_descontos, text="SALÁRIO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_salariodes.pack(pady=(10, 2))

entry_Salariodes = ctk.CTkEntry(tab_descontos, width=200)
entry_Salariodes.pack(pady=(2, 10))

label_porcentagem_salariodes = ctk.CTkLabel(tab_descontos, text="PORCENTAGEM (%):", font=("Segoe UI", 15), text_color="#D4AF37")
label_porcentagem_salariodes.pack(pady=(10, 2))

entry_porcentagem_salariodes = ctk.CTkEntry(tab_descontos, width=200)
entry_porcentagem_salariodes.pack(pady=(2, 10))

label_resultado_descontos = ctk.CTkLabel(tab_descontos, text="RESULTADO:", font=("Segoe UI", 15), text_color="#D4AF37")
label_resultado_descontos.pack(pady=(10, 2))


def calcular_desconto_salarial():
    try:
        salario = float(entry_Salariodes.get())
        porcentagem = float(entry_porcentagem_salariodes.get())

        desconto = salario * porcentagem / 100
        novo_salario = salario - desconto

        label_resultado_descontos.configure(text=f"Desconto de R$ {desconto:.2f}\nNovo Salário: R$ {novo_salario:.2f}")
    except ValueError:  
        messagebox.showerror("Erro", "Digite valores válidos!")

botao_calcular = ctk.CTkButton(tab_descontos, text="Calcular Desconto", command=calcular_desconto_salarial)
botao_calcular.pack(pady=10) 

def limpar_jc():
   entry_Salariodes.delete(0, "end")
   entry_porcentagem_salariodes.delete(0, "end")
   label_resultado_descontos.configure(text="")

botao_limpar_jc = ctk.CTkButton(
    tab_descontos,
    text="Limpar",
    command=limpar_jc,
    fg_color="#8B0000",  # vermelho escuro
    hover_color="#A52A2A"
)
botao_limpar_jc.pack(pady=5)


# DEIXAR A JANELA A
window.mainloop()