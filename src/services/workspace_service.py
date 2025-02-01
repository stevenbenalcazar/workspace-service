from src.config.database import SessionLocal
from src.models.workspace import Workspace
from src.schemas.workspace import WorkspaceCreate

def create_workspace(input: WorkspaceCreate):
    db = SessionLocal()
    workspace = Workspace(name=input["name"], description=input["description"])
    db.add(workspace)
    db.commit()
    db.refresh(workspace)
    return workspace
