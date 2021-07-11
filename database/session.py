from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.entities.ORM.base import Base
import os.path


def get_session():
    engine = create_engine('sqlite:///clients.sqlite')
    if os.path.isfile("clients.sqlite"):
        Base.metadata.create_all(engine)
    else:
        Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    _session = DBSession()
    return _session


