from core.infra.database.database import DatabaseConnection
from core.infra.database.fake_adapter import FakeConnection
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.database.sqlalchemy_tables import init_tables_sqlalchemy
from core.shared.exceptions import DatabaseInstanceError


def init_database_tables(database_conn: DatabaseConnection):
    if isinstance(database_conn, SQLAlchemyConnection):
        init_tables_sqlalchemy(database_conn)
    elif isinstance(database_conn, FakeConnection):
        pass
    else:
        raise DatabaseInstanceError("Database adapter not found")
