from sqlalchemy import Column, Integer, String

from database.entities.ORM.base import Base


class ClientORM(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address_line_i = Column(String)
    address_line_ii = Column(String)

    usual_quantity = Column(Integer)
    usual_price = Column(Integer)

    post_code = Column(String)
    phone = Column(String)
    terms = Column(Integer)

    def __repr__(self):
        return f"<Client>(name={self.name})"

