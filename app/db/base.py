from sqlalchemy.orm import Session


class DBSessionContext():
    def __init__(self, db: Session):
        self.db = db


class AppCRUD(DBSessionContext):
    pass