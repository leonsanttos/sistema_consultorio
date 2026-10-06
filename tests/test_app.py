import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app({"DATABASE": str(tmp_path / "teste.db"), "TESTING": True})
    return app.test_client()


@pytest.mark.parametrize("rota", ["/", "/medicos/", "/pacientes/", "/funcionarios/", "/consultas/"])
def test_paginas_abrem(client, rota):
    assert client.get(rota).status_code == 200


def test_fluxo_consulta(client):
    client.post("/medicos/novo", data={"nome": "Dr. João", "crm": "123-SP"})
    client.post("/pacientes/novo", data={"nome": "Maria"})
    r = client.post("/consultas/novo", data={
        "paciente_id": "1", "medico_id": "1",
        "data_consulta": "2026-10-07T10:30", "motivo": "Rotina",
    }, follow_redirects=True)
    assert "Maria" in r.get_data(as_text=True)
    assert "2026-10-07 10:30" in r.get_data(as_text=True)


def test_crm_duplicado(client):
    dados = {"nome": "Dr. A", "crm": "1"}
    client.post("/medicos/novo", data=dados)
    r = client.post("/medicos/novo", data=dados)
    assert "duplicados" in r.get_data(as_text=True)


def test_editar_e_excluir(client):
    client.post("/pacientes/novo", data={"nome": "Ana"})
    client.post("/pacientes/1/editar", data={"nome": "Ana Paula"})
    assert "Ana Paula" in client.get("/pacientes/").get_data(as_text=True)
    client.post("/pacientes/1/excluir")
    assert "Ana Paula" not in client.get("/pacientes/").get_data(as_text=True)


def test_nao_exclui_medico_com_consulta(client):
    client.post("/medicos/novo", data={"nome": "Dr. X", "crm": "9"})
    client.post("/pacientes/novo", data={"nome": "Zé"})
    client.post("/consultas/novo", data={
        "paciente_id": "1", "medico_id": "1", "data_consulta": "2026-10-07T09:00"})
    r = client.post("/medicos/1/excluir", follow_redirects=True)
    assert "consultas vinculadas" in r.get_data(as_text=True)
