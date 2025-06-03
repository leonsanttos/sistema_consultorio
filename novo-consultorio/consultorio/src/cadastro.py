import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexão com banco (se quiser, pode mover para um arquivo db.py separado)
conn = sqlite3.connect("consultorio.db")
cursor = conn.cursor()

# Criar a tabela (executa apenas se não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS medicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT,
    crm TEXT UNIQUE NOT NULL
)
""")
conn.commit()

def abrir_tela_medicos():
    janela_medicos = tk.Toplevel()
    janela_medicos.title("Gerenciar Médicos")
    janela_medicos.geometry("500x400")

    tk.Label(janela_medicos, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_nome = tk.Entry(janela_medicos, width=30)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_medicos, text="Especialidade:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_especialidade = tk.Entry(janela_medicos, width=30)
    entry_especialidade.grid(row=1, column=1)

    tk.Label(janela_medicos, text="CRM:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_crm = tk.Entry(janela_medicos, width=30)
    entry_crm.grid(row=2, column=1)

    def salvar_medico():
        nome = entry_nome.get()
        especialidade = entry_especialidade.get()
        crm = entry_crm.get()

        if nome and crm:
            try:
                cursor.execute("""
                    INSERT INTO medicos (nome, especialidade, crm)
                    VALUES (?, ?, ?)
                """, (nome, especialidade, crm))
                conn.commit()
                messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")
                entry_nome.delete(0, tk.END)
                entry_especialidade.delete(0, tk.END)
                entry_crm.delete(0, tk.END)
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "CRM já cadastrado.")
        else:
            messagebox.showwarning("Atenção", "Preencha os campos obrigatórios (Nome e CRM).")

    btn_salvar = tk.Button(janela_medicos, text="Salvar Médico", command=salvar_medico)
    btn_salvar.grid(row=3, column=0, columnspan=2, pady=20)
