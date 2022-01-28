from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

sqlite_file_name = "userdatabase.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_users():
    user_1 = User(username="admin", password="admin")
    user_2 = User(username="user12", password="user12")

    with Session(engine) as session:
        session.add(user_1)
        session.add(user_2)
        session.commit()

def select_users():
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)
        for user in results:
            print(user)

def delete_user():
    with Session(engine) as session:
        statement = select(User).where(User.username=="admin")
        results = session.exec(statement)
        user = results.first()

        session.delete(user)
        session.commit()

def update_user():
    with Session(engine) as session:
        statement = select(User).where(User.username=="user12")
        results = session.exec(statement)
        user = results.first()

        user.password = "user21"
        session.add(user)
        session.commit()
        session.refresh(user)

if __name__ == "__main__":
    create_db_and_tables()
    # create_users()
    # delete_user()
    update_user()
    select_users()
