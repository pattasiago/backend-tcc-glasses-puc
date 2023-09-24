import os

from dotenv import load_dotenv

from core.infra.database.fake_adapter import FakeConnection
from core.infra.database.init_database_tables import init_database_tables
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.employee_repository import EmployeeRepositoryFactory

load_dotenv()

db_uri = None
database_connection = None
employee_repository = None


def create_app_config(app_mode="PROD"):
    global db_uri, database_connection, employee_repository
    if app_mode == "PROD":
        db_uri = os.getenv("DATABASE_URI")
        database_connection = SQLAlchemyConnection(db_uri)
        init_database_tables(database_connection)
    elif app_mode == "TESTING":
        database_connection = FakeConnection()

    employee_repository = EmployeeRepositoryFactory(database_connection)


create_app_config(app_mode=os.getenv("APP_MODE", "PROD"))
