from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class UnsupportedDatabaseEngine(Exception):
    pass


def generate_db_url(db_name=None, db_engine='sqlite'):
    engines = {'sqlite', 'postgres'}
    if db_name is None:
        db_string = 'sqlite:///:memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        if db_engine == 'sqlite':
            db_string = 'sqlite:///{}.db'.format(db_name)
            print('New connection to SQLite DB...')
        elif db_engine == 'postgres':
            db_string = \
                'postgresql://test_user:test_password@localhost:5432/{}'.format(db_name)
            print('New connection to PostgreSQL DB...')
        else:
            raise UnsupportedDatabaseEngine(
                'No database engine with this name. '
                'Choose one of the following: {}'.format(engines))

    return db_string

engine = create_engine(
    generate_db_url(db_name=None),
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)