from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker



DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="password",   # your real password
    host="localhost",
    port=3306,
    database="todo_app",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
