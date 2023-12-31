from sqlalchemy import Column, DateTime, create_engine, func
from sqlalchemy.orm import declarative_base, registry, sessionmaker

from core.infra.database.database import DatabaseConnection


class BaseMixin:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in dir(self):
                exec(f"self.{key} = {value}")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class SQLAlchemyConnection(DatabaseConnection):
    base = declarative_base()
    base_mixin = BaseMixin

    def __init__(self, db_uri):
        self.engine = create_engine(db_uri, pool_size=10, max_overflow=20)
        self.mapper_registry = registry()
        self.db_session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def init_session(self):
        self.session = self.db_session()

    def remove_session(self):
        self.session.close()
