from app.routes import consultas, funcionarios, main, medicos, pacientes


def register_blueprints(app):
    for modulo in (main, medicos, pacientes, funcionarios, consultas):
        app.register_blueprint(modulo.bp)
