from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
from model.todo import Todo


SQLALCHEMY_DATABASE_URL="postgresql://iamhaider072:iuYSL4wXG5xk@ep-aged-waterfall-a52my4g0.us-east-2.aws.neon.tech/test1?sslmode=require"

engine=create_engine(SQLALCHEMY_DATABASE_URL)
Base=declarative_base()


class TodoTable(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    description=Column(String,index=True)




async def create_table():
 Base.metadata.create_all(engine)


#Database Functions



async def  create_all(todo:Todo):
   Sessionlocal=sessionmaker(autocommit=True,autoflush=True,bind=engine)
   session=Sessionlocal()
   try:
      new_todo=TodoTable.insert().values(title=todo.title, description=todo.description ,id=todo.id)
      session.execute(new_todo)
      session.commit()

   finally:
      session.close()
      



async def get_all_todos(todo:Todo):
    Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
    session=Sessionlocal()
    try:
       query=TodoTable.select()
       result=session.execute(query)
       todos=result.fetchall
       return todos
    finally:
       session.close()




async def get_todo_by_id(todo_id:int):
    Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
    session=Sessionlocal()

    try:
       query=TodoTable.select().where(TodoTable.c.id==todo_id)
       result=session.execute(query)
       todo=result.fetchone()
       return todo
    finally:
       session.close()



async def update_todo(todo_id:int,updated_todo:Todo):
    Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
    session=Sessionlocal()

    try:
       query=TodoTable.update().where(TodoTable.c.id==todo_id).values(title=updated_todo.title,description=updated_todo.description,id=updated_todo.id)
       session.execute(query)
       session.commit()

    finally:
       session.close()




async def delete_todo(todo_id:int):
     Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
     session=Sessionlocal()
     try:
        query=TodoTable.delete().where().values(TodoTable.c.id==todo_id)
        session.execute(query)
        session.commit()

     finally:
      session.close()


    
      



