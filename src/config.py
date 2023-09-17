import os

from dotenv import load_dotenv

from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.employee_repository import EmployeeRepositoryFactory

load_dotenv()

db_uri = os.getenv("DATABASE_URI")
database_connection = SQLAlchemyConnection(db_uri)
employee_repository = EmployeeRepositoryFactory(database_connection)
