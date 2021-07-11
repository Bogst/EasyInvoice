from sqlalchemy import Column, Integer, String

from database.entities.ORM.base import Base


class SettingsORM(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)
    invoice_nr = Column(Integer)
    name = Column(String)
    address_line_i = Column(String)
    address_line_ii = Column(String)
    post_code = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"<Settings>(name={self.id})"

