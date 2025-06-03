import tkinter as tk
from tkinter import messagebox
from src.db import conectar

def tela_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    janela = tk.Toplevel()
    janela.geometry("500x300")
    janela.title("Cadastro de Funcionarios")

    # Campos
    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Cargo:").grid(row=1, column=0, padx=5, pady=5)
    entry_cargo = tk.Entry(janela)
    entry_cargo.grid(row=1, column=1)

    tk.Label(janela, text="data_contrato:").grid(row=2, column=0, padx=5, pady=5)
    entry_data_contrato = tk.Entry(janela)
    entry_data_contrato.grid(row=2, column=1)

    def salvar():
        nome = entry_nome.get()
        cargo = entry_cargo.get()
        data_contrato = entry_data_contrato.get()
        if nome :
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cargo TEXT NOT NULL,
                        data_contrato TEXT NOT NULL
                    )
                """)
                cursor.execute("INSERT INTO funcionarios (nome, cargo, data_contrato) VALUES (?, ?, ?)",
                               (nome, cargo, data_contrato))
                conn.commit()
                messagebox.showinfo("Sucesso", "Funcionario cadastrado com sucesso.")
                entry_nome.delete(0, tk.END)
                entry_cargo.delete(0, tk.END)
                entry_data_contrato.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Preencha os campos obrigatórios.")

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)
