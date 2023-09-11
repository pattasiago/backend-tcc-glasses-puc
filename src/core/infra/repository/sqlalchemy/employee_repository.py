import time

from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.sqlalchemy.employee_orm import EmployeeORMCreator


class SQLAlchemyEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, sqlalchemy_conn: SQLAlchemyConnection):
        self.database_conn = sqlalchemy_conn
        self.orm = EmployeeORMCreator(sqlalchemy_conn)

    def get_employees(self, asEntity=False):
        employees = self.database_conn.session.query(self.orm).all()
        time.sleep(5)
        print(self.database_conn.session)
        if asEntity:
            return list(map(lambda x: x.to_entity(), employees))
        else:
            return list(map(lambda x: x.to_dict(), employees))
