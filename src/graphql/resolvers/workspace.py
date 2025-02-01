from ariadne import MutationType, QueryType
from src.services.workspace_service import create_workspace

query = QueryType()
mutation = MutationType()

@mutation.field("createWorkspace")
def resolve_create_workspace(_, info, input):
    return create_workspace(input)

resolvers = [query, mutation]
