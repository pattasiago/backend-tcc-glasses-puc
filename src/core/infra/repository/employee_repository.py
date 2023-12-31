from core.infra.database.database import DatabaseConnection
from core.infra.database.fake_adapter import FakeConnection
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.fake_employee_repository import FakeEmployeeRepository
from core.infra.repository.sqlalchemy.employee_repository_sqlalchemy import (
    SQLAlchemyEmployeeRepository,
)
from core.shared.exceptions import DatabaseInstanceError


class EmployeeRepositoryFactory:
    def __new__(self, database_conn: DatabaseConnection):
        if isinstance(database_conn, SQLAlchemyConnection):
            return SQLAlchemyEmployeeRepository(database_conn)
        elif isinstance(database_conn, FakeConnection):
            return FakeEmployeeRepository()
        else:
            raise DatabaseInstanceError("Database adapter not found")
