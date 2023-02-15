from sqlalchemy import Column, Integer, String

from app.db.database import Base


class BaseOrm(Base):

    """
    A class of base ORM model
    """

    __abstract__ = True

    def to_dict(self) -> dict:
        """
        A funcion to dump data to dict format
        """
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

class TaskOrm(BaseOrm):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Integer, default=0)