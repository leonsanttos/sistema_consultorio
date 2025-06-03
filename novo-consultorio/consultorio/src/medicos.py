import tkinter as tk
from tkinter import messagebox
from src.db import conectar

def tela_medicos():
    conn = conectar()
    cursor = conn.cursor()
    janela = tk.Toplevel()
    janela.geometry("500x300")
    janela.title("Cadastro de Médicos")

    # Campos
    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Especialidade:").grid(row=1, column=0, padx=5, pady=5)
    entry_especialidade = tk.Entry(janela)
    entry_especialidade.grid(row=1, column=1)

    tk.Label(janela, text="CRM:").grid(row=2, column=0, padx=5, pady=5)
    entry_crm = tk.Entry(janela)
    entry_crm.grid(row=2, column=1)

    def salvar():
        nome = entry_nome.get()
        esp = entry_especialidade.get()
        crm = entry_crm.get()
        if nome and crm:
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS medicos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        especialidade TEXT,
                        crm TEXT UNIQUE NOT NULL
                    )
                """)
                cursor.execute("INSERT INTO medicos (nome, especialidade, crm) VALUES (?, ?, ?)",
                               (nome, esp, crm))
                conn.commit()
                messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso.")
                entry_nome.delete(0, tk.END)
                entry_especialidade.delete(0, tk.END)
                entry_crm.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Preencha os campos obrigatórios.")

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)
