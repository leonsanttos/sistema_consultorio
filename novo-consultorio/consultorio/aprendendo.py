import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Exemplo Layout")

# Fundo da janela
root.configure(bg="#f0f0f0")

# Label alinhado à esquerda com cor
tk.Label(root, text="Nome:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Idade:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

# Botão centralizado em 2 colunas
tk.Button(root, text="Enviar", bg="green", fg="white").grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
