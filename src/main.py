from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from ariadne.asgi import GraphQL
from src.graphql.schema import schema
from src.config.database import init_db

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar DB
init_db()

# Configurar GraphQL
app.add_route("/graphql", GraphQL(schema, debug=True))
