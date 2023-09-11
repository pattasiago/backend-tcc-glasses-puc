from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, registry, scoped_session, sessionmaker

from core.infra.database.database import DatabaseConnection


class SQLAlchemyConnection(DatabaseConnection):
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.mapper_registry = registry()
        self.base = declarative_base()
        self.db_session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def init_session(self):
        self.session = self.db_session()

    def remove_session(self):
        print("removing", self.session)
        self.session.close()
