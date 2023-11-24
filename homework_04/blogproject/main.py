import os
from sqlalchemy import create_engine

from blogproject.database import Base

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+pg8000://user:password@localhost/postgres"

engine = create_engine(PG_CONN_URI, echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)