from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: Optional[int] = 0
    deadline: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_todo(title, deadline, description=None):
    todo = Todo(title=title, deadline=deadline, description=description)
  
    with Session(engine) as session:
        session.add(todo)
        session.commit()

def select_todos():
    res_dict = {}
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        
        for todo in results:
            res_dict[str(todo.id)] = {}
            res_dict[str(todo.id)]["title"] = todo.title
            res_dict[str(todo.id)]["description"] = todo.description
            res_dict[str(todo.id)]["status"] = todo.status
            res_dict[str(todo.id)]["deadline"] = todo.deadline
        return res_dict


def delete_todo(id):
    with Session(engine) as session:
        statement = select(Todo).where(Todo.id==id)
        results = session.exec(statement)
        todo = results.first()

        session.delete(todo)
        session.commit()

def update_todo(id):
    with Session(engine) as session:
        statement = select(Todo).where(Todo.id==id)
        results = session.exec(statement)
        todo = results.first()

        todo.status = not todo.status
        session.add(todo)
        session.commit()
        session.refresh(todo)
