import sqlalchemy as db

engine = db.create_engine("mysql://scott:tiger@localhost/foo")
connection = engine.connect()
metadata = db.MetaData()
census = db.Table("teste", metadata, autoload=True, autoload_with=engine)
