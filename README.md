# Sistema de Consultório

Aplicação web em Python (Flask) com banco SQLite para gerenciar médicos, pacientes, funcionários e consultas.

## Estrutura

```
app/
  __init__.py        # fábrica da aplicação (create_app)
  config.py          # configurações
  database.py        # conexão SQLite e criação do schema
  schema.sql         # tabelas
  repositories/      # acesso ao banco (SQL), um arquivo por entidade
  routes/            # rotas (blueprints): um arquivo por entidade, crud.py (CRUD genérico) e main.py (painel)
  templates/         # HTML (Jinja2)
  static/css/        # estilos
tests/               # testes automatizados (pytest)
data/                # banco consultorio.db (criado automaticamente)
run.py               # ponto de entrada
```

Fluxo: `rota -> repositório -> SQLite`; a rota renderiza o template.

## Como rodar

```
pip install -r requirements.txt
python run.py
```

Acesse http://127.0.0.1:5000. Testes: `python -m pytest`.
