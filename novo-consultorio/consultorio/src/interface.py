import tkinter as tk
from tkinter import messagebox
from src.consultas import tela_consultas
from src.medicos import tela_medicos
from src.pacientes import tela_pacientes
from src.funcionarios import tela_funcionarios
from src.db import conectar

def iniciar_interface():
    root = tk.Tk()
    root.title("Sistema de Consultório")
    root.geometry("900x500")

    # Menu suspenso
    def abrir_cadastro():
        tipo = var_opcao.get()
        if tipo == "Médico":
            tela_medicos()
        elif tipo == "Paciente":
            tela_pacientes()
        elif tipo == "Funcionário":
            tela_funcionarios()

    tk.Label(root, text="Cadastro de Pessoas").pack(pady=10)

    var_opcao = tk.StringVar(root)
    var_opcao.set("Médico")  # valor padrão
    menu_opcoes = tk.OptionMenu(root, var_opcao, "Médico", "Paciente", "Funcionário")
    menu_opcoes.pack()

    tk.Button(root, text="Abrir Cadastro", command=abrir_cadastro).pack(pady=5)
    tk.Button(root, text="Cadastrar Consultas", command=tela_consultas).pack(pady=10)

    # Frame fixo para exibir consultas (tamanho 400x200)
    frame_consultas = tk.Frame(root, width=400, height=200, bg="white", relief="sunken", borderwidth=1)
    frame_consultas.pack(pady=20)
    frame_consultas.pack_propagate(False)  # impede redimensionamento automático

    text_area = tk.Text(frame_consultas, wrap="word")
    text_area.pack(expand=True, fill="both")

    def carregar_consultas():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, medico_id, data, motivo FROM consultas")
            consultas = cursor.fetchall()

            text_area.delete("1.0", tk.END)  # limpa antes de carregar

            if consultas:
                for c in consultas:
                    texto = f"ID: {c[0]} | Médico ID: {c[1]} | Data: {c[2]} | Motivo: {c[3]}\n"
                    text_area.insert(tk.END, texto)
            else:
                text_area.insert(tk.END, "Nenhuma consulta cadastrada.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Carrega automaticamente ao abrir
    carregar_consultas()

    # Botão para recarregar
    tk.Button(root, text="Recarregar Consultas", command=carregar_consultas).pack()

    # Sair
    tk.Button(root, text="Sair", command=root.quit).pack(side="bottom", pady=10)

    root.mainloop()
