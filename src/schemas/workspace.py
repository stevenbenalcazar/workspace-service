from pydantic import BaseModel

class WorkspaceCreate(BaseModel):
    name: str
    description: str

class WorkspaceResponse(BaseModel):
    id: int
    name: str
    description: str
