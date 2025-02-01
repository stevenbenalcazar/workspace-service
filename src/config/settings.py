import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/workspacedb")
JWT_SECRET = os.getenv("JWT_SECRET", "clave_secreta")
