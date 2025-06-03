import tkinter as tk
from tkinter import messagebox
from src.db import conectar

def tela_pacientes():
    conn = conectar()
    cursor = conn.cursor()
    janela = tk.Toplevel()
    janela.geometry("500x300")
    janela.title("Cadastro de Pacientes")

    # Campos
    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela, text="Data de Nasciento:").grid(row=1, column=0, padx=5, pady=5)
    entry_data_nascimento = tk.Entry(janela)
    entry_data_nascimento.grid(row=1, column=1)

    tk.Label(janela, text="Motivo:").grid(row=2, column=0, padx=5, pady=5)
    entry_motivo = tk.Entry(janela)
    entry_motivo.grid(row=2, column=1)

    def salvar():
        nome = entry_nome.get()
        data = entry_data_nascimento.get()
        motivo = entry_motivo.get()
        if nome :
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pacientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_nascimento TEXT,
                        motivo TEXT NOT NULL
                    )
                """)
                cursor.execute("INSERT INTO pacientes (nome, data_nascimento, motivo) VALUES (?, ?, ?)",
                               (nome, data, motivo))
                conn.commit()
                messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso.")
                entry_nome.delete(0, tk.END)
                entry_data_nascimento.delete(0, tk.END)
                entry_motivo.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Preencha os campos obrigatórios.")

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)
