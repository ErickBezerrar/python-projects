import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkthemes as tkthemes


class InvestimentoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cálculo de Juros Compostos")
        self.master.geometry("800x600")
        self.master.resizable(True, True)

        style = ttk.Style(self.master)
        style.configure(".", anchor="w")
        style.configure("TEntry", padding=5, relief="flat")
        style.configure("TLabel", padding=5)

        style.theme_use("clam")

        frame = ttk.Frame(self.master, padding=10)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="Valor Inicial():").grid(column=0, row=0, sticky="w")
        self.valor_presente = ttk.Entry(frame)
        self.valor_presente.grid(column=1, row=0)

        ttk.Label(frame, text="Taxa de Juros (%):").grid(column=0, row=1, sticky="w")
        self.taxa_juros = ttk.Entry(frame)
        self.taxa_juros.grid(column=1, row=1)

        ttk.Label(frame, text="Período (anos):").grid(column=0, row=2, sticky="w")
        self.periodo_anos = ttk.Entry(frame)
        self.periodo_anos.grid(column=1, row=2)

        ttk.Label(frame, text="Aporte Mensal:").grid(column=0, row=3, sticky="w")
        self.aporte_mensal = ttk.Entry(frame)
        self.aporte_mensal.grid(column=1, row=3)

        ttk.Label(frame, text="Aumento Anual (%):").grid(column=0, row=4, sticky="w")
        self.aumento_mensal = ttk.Entry(frame)
        self.aumento_mensal.grid(column=1, row=4)


        ttk.Label(frame, text="Valor Futuro:").grid(column=0, row=5, sticky="w")
        self.valor_futuro = ttk.Label(frame, text="")
        self.valor_futuro.grid(column=1, row=5)

        ttk.Button(frame, text="Calcular", command=self.calcular).grid(column=1, row=6, pady=10)

        columns = ("Ano", "Valor Inicial", "Aportes", "Juros", "Valor Final")
        self.tree = ttk.Treeview(frame, show="headings", columns=columns)
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=120, anchor="w")
        self.tree.grid(column=0, row=7, columnspan=2)

    def calcular(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        try:
            valor_presente = float(self.valor_presente.get().replace(",", "."))
            taxa_juros = float(self.taxa_juros.get().replace(",", "."))
            periodo_anos = int(self.periodo_anos.get())
            aporte_mensal = float(self.aporte_mensal.get().replace(",", "."))
            aumento_mensal = float(self.aumento_mensal.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        if valor_presente <= 0 or taxa_juros <= 0 or periodo_anos <= 0 or aporte_mensal < 0 or aumento_mensal < 0:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
            return

        valores = []
        valor_atual = valor_presente
        for i in range(1, periodo_anos+1):
            juros_ano = 0
            for mes in range(12):
                juros_mes = (valor_atual + aporte_mensal * mes) * (taxa_juros / 100 / 12)
                juros_ano += juros_mes
                valor_atual += aporte_mensal + juros_mes
                aporte_mensal *= 1 + aumento_mensal / 100

            valores.append((i, "{:.2f}".format(valor_presente), "{:.2f}".format(aporte_mensal * 12), "{:.2f}".format(juros_ano), "{:.2f}".format(valor_atual)))
            valor_presente = valor_atual

        self.valor_futuro.config(text="{:.2f}".format(valor_atual))

        for valor in valores:
            self.tree.insert("", "end", values=valor)



root = tk.Tk()
app = InvestimentoGUI(root)
root.mainloop()