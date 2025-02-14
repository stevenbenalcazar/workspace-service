from ariadne import make_executable_schema, load_schema_from_path
from src.graphql.resolvers.workspace import resolvers  # Importa los resolvers

# Cargar esquema desde un archivo .graphql
type_defs = load_schema_from_path("src/graphql/schema/schema.graphql")

# ✅ NO es necesario crear otro QueryType aquí, ya está en `resolvers`
schema = make_executable_schema(type_defs, *resolvers)  # Usa *resolvers para descomprimir la lista
