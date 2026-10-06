from app.repositories.consultas import ConsultaRepository
from app.repositories.funcionarios import FuncionarioRepository
from app.repositories.medicos import MedicoRepository
from app.repositories.pacientes import PacienteRepository

medicos = MedicoRepository()
pacientes = PacienteRepository()
funcionarios = FuncionarioRepository()
consultas = ConsultaRepository()
