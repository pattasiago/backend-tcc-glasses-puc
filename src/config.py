import os

from dotenv import load_dotenv

from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.sqlalchemy.employee_repository import (
    SQLAlchemyEmployeeRepository,
)

load_dotenv()

db_uri = os.getenv("DATABASE_URI")
database_connection = SQLAlchemyConnection(db_uri)
employee_repository = SQLAlchemyEmployeeRepository(database_connection)
