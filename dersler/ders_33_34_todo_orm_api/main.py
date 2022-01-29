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

def create_todo():
    todo_1 = Todo(title="Alisveris", deadline="01.01.22")
    todo_2 = Todo(title="Alisveris2", deadline="01.01.21")

    with Session(engine) as session:
        session.add(todo_1)
        session.add(todo_2)
        session.commit()

def select_todos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        for todo in results:
            print(todo)

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

        todo.status = 1
        session.add(todo)
        session.commit()
        session.refresh(todo)

if __name__ == "__main__":
    create_db_and_tables()
    create_todo()
    select_todos()
    #delete_todo(12)
    update_todo(9)