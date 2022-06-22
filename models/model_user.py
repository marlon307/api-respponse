from warnings import catch_warnings
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, inspect
from models.database import Base


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    # name = Column(String, nullable=False)
    # password = Column(String, nullable=False)
    # gender_id = Column(Integer)
    # birthday = Column(Date)
    # cpf_cnph = Column(Integer)
    # seller = Column(Boolean)
    # created_date = Column(DateTime)
    # https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
    @property
    def serialize(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    def to_json(self):
        try:
            return [i.serialize for i in self]
        except:
            return self.serialize
