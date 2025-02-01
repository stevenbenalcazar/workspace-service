from ariadne import make_executable_schema, load_schema_from_path
from src.graphql.resolvers.workspace import resolvers

type_defs = load_schema_from_path("src/graphql/schema/schema.graphql")

schema = make_executable_schema(type_defs, resolvers)
