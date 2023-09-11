from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.sqlalchemy.employee_repository import (
    SQLAlchemyEmployeeRepository,
)

db_uri = "postgresql://postgres:admin@localhost:5432/glasses_sales"
database_connection = SQLAlchemyConnection(db_uri)
employee_repository = SQLAlchemyEmployeeRepository(database_connection)
