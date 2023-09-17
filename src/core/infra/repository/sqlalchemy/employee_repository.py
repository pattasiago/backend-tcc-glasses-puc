from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.repository.sqlalchemy.employee_orm import EmployeeORMCreator


class SQLAlchemyEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, sqlalchemy_conn: SQLAlchemyConnection):
        self.database_conn = sqlalchemy_conn
        self.orm = EmployeeORMCreator(sqlalchemy_conn)

    def get_employees(self) -> list[Employee]:
        employees = self.database_conn.session.query(self.orm).all()
        return list(map(lambda x: x.to_entity(), employees))

    def get_employee_by_id(self, id: int) -> Employee:
        employee = self.database_conn.session.query(self.orm).get(id)
        if employee:
            return employee.to_entity()
        else:
            return None

    def get_employee_by_cpf(self, cpf: str) -> Employee:
        employee = (
            self.database_conn.session.query(self.orm).filter(self.orm.cpf == cpf).one()
        )
        if employee:
            return employee.to_entity()
        else:
            return None

    def create_employee(self, employee: dict) -> None:
        employee_orm = self.orm(**employee)
        self.database_conn.session.add(employee_orm)
        self.database_conn.session.commit()
