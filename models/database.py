# https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    "mysql+pymysql://{user}:{psw}@{host}:{port}/{db}".format(
        user=os.getenv("DB_USER"),
        psw=os.getenv("DB_PSW"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        db=os.getenv("DB_NAME"),
    ),
    pool_pre_ping=True,
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models

    Base.metadata.create_all(bind=engine)
