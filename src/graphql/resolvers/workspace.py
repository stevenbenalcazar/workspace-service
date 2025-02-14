from ariadne import MutationType, QueryType
from src.services.workspace_service import create_workspace

query = QueryType()
mutation = MutationType()

# ✅ Agregar una consulta de prueba
@query.field("hello")
def resolve_hello(_, info):
    return "Hello, GraphQL!"

@query.field("workspace")
def resolve_workspace(_, info, id):
    return {"id": id, "name": "Mi Workspace"}

# ✅ Resolver la mutación createWorkspace
@mutation.field("createWorkspace")
def resolve_create_workspace(_, info, input):
    return create_workspace(input)

# ✅ Asegurarse de que `query` tenga al menos un campo
resolvers = [query, mutation]
