import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-troque-em-producao")
    DATABASE = os.environ.get("DATABASE", str(BASE_DIR / "data" / "consultorio.db"))
