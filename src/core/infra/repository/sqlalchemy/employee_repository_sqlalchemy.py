from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.database.sqlalchemy_tables import EmployeeTable


class SQLAlchemyEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, sqlalchemy_conn: SQLAlchemyConnection):
        self.database_conn = sqlalchemy_conn

    def get_employees(self) -> list[Employee]:
        employees = self.database_conn.session.query(EmployeeTable).all()
        return list(map(lambda x: x.to_entity(), employees))

    def get_employee_by_id(self, id: int) -> Employee | None:
        employee = self.database_conn.session.query(EmployeeTable).get(id)
        if employee:
            return employee.to_entity()
        else:
            return None

    def get_employee_by_cpf(self, cpf: str) -> Employee | None:
        employee = (
            self.database_conn.session.query(EmployeeTable)
            .filter(EmployeeTable.cpf == cpf)
            .one()
        )
        if employee:
            return employee.to_entity()
        else:
            return None

    def create_employee(self, employee: dict) -> None:
        employee_table = EmployeeTable(**employee)
        self.database_conn.session.add(employee_table)
        self.database_conn.session.commit()
