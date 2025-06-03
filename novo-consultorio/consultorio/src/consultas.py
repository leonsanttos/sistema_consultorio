import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from src.db import conectar

def tela_consultas():
    conn = conectar()
    cursor = conn.cursor()
    janela = tk.Toplevel()
    janela.title("Consultas")

    # Cria tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medico_id INTEGER,
            data TEXT,
            motivo TEXT,
            FOREIGN KEY (medico_id) REFERENCES medicos(id)
        )
    """)

    # Campos
    tk.Label(janela, text="ID Médico:").grid(row=0, column=0)
    entry_medico = tk.Entry(janela)
    entry_medico.grid(row=0, column=1)

    tk.Label(janela, text="Data (AAAA-MM-DD):").grid(row=1, column=0)
    entry_data = tk.Entry(janela)
    entry_data.grid(row=1, column=1)

    tk.Label(janela, text="Motivo:").grid(row=2, column=0)
    entry_motivo = tk.Entry(janela)
    entry_motivo.grid(row=2, column=1)

    def salvar():
        try:
            cursor.execute("INSERT INTO consultas (medico_id, data, motivo) VALUES (?, ?, ?)",
                           (entry_medico.get(), entry_data.get(), entry_motivo.get()))
            conn.commit()
            messagebox.showinfo("Sucesso", "Consulta cadastrada.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar():
        id_consulta = simpledialog.askinteger("Atualizar", "ID da consulta a atualizar:")
        if id_consulta:
            try:
                cursor.execute("""
                    UPDATE consultas SET medico_id=?, data=?, motivo=? WHERE id=?
                """, (entry_medico.get(), entry_data.get(), entry_motivo.get(), id_consulta))
                conn.commit()
                messagebox.showinfo("Sucesso", "Consulta atualizada.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def remover():
        id_consulta = simpledialog.askinteger("Remover", "ID da consulta a remover:")
        if id_consulta:
            cursor.execute("DELETE FROM consultas WHERE id=?", (id_consulta,))
            conn.commit()
            messagebox.showinfo("Removido", "Consulta excluída.")

    tk.Button(janela, text="Salvar", command=salvar).grid(row=3, column=0)
    tk.Button(janela, text="Atualizar", command=atualizar).grid(row=3, column=1)
    tk.Button(janela, text="Remover", command=remover).grid(row=4, column=0, columnspan=2)
