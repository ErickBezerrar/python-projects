import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkthemes as tkthemes


class InvestimentoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Investimento")
        
        self.lbl_investimento = tk.Label(master, text="Investimento inicial:")
        self.lbl_investimento.pack()
        self.ent_investimento = tk.Entry(master)
        self.ent_investimento.pack()

        self.lbl_aporte_inicial = tk.Label(master, text="Aporte mensal inicial:")
        self.lbl_aporte_inicial.pack()
        self.ent_aporte_inicial = tk.Entry(master)
        self.ent_aporte_inicial.pack()

        self.lbl_aumento_aporte_anual = tk.Label(master, text="Aumento anual do aporte em porcentagem:")
        self.lbl_aumento_aporte_anual.pack()
        self.ent_aumento_aporte_anual = tk.Entry(master)
        self.ent_aumento_aporte_anual.pack()

        self.lbl_anos = tk.Label(master, text="Quantidade de anos do investimento:")
        self.lbl_anos.pack()
        self.ent_anos = tk.Entry(master)
        self.ent_anos.pack()
        
        self.btn_calcular = tk.Button(master, text="Calcular", command=self.calcular)
        self.btn_calcular.pack()
        
        self.tree = ttk.Treeview(master, columns=("Ano", "Valor Futuro"), style="Custom.Treeview")
        self.tree.heading("#0", text="")
        self.tree.heading("#1", text="Ano")
        self.tree.heading("#2", text="Valor Futuro")
        self.tree.pack()

        style = tkthemes.ThemedStyle(master)
        style.set_theme("arc")
        style.configure("Custom.Treeview", background=style.lookup("TFrame", "background"), fieldbackground=style.lookup("TFrame", "background"))

    def calcular(self):
        investimento_inicial = float(self.ent_investimento.get())
        aporte_mensal_inicial = float(self.ent_aporte_inicial.get())
        aumento_aporte_anual = float(self.ent_aumento_aporte_anual.get())
        taxa_juros = 0.1  # 10% ao ano.
        anos = int(self.ent_anos.get())

        valor_futuro = investimento_inicial
        dados = {"Ano": [], "Valor Futuro": []}
        aporte_mensal = aporte_mensal_inicial
        for i in range(anos):
            for j in range(12):
                valor_futuro = (valor_futuro + aporte_mensal) * (1 + taxa_juros / 12)
            dados["Ano"].append(i + 1)
            dados["Valor Futuro"].append(valor_futuro)
            aporte_mensal *= (1 + aumento_aporte_anual / 100)

        self.tree.delete(*self.tree.get_children())
        for i in range(anos):
            for j in range(12):
                valor_futuro = (valor_futuro + aporte_mensal) * (1 + taxa_juros / 12)
            dados["Ano"].append(i + 1)
            dados["Valor Futuro"].append(valor_futuro)
            aporte_mensal *= (1 + aumento_aporte_anual / 100)
            self.tree.insert("", "end", text="", values=(i + 1, valor_futuro))

        messagebox.showinfo("Investimento", "O investimento foi calculado e salvo com sucesso.")


root = tk.Tk()
gui = InvestimentoGUI(root)
root.mainloop()
