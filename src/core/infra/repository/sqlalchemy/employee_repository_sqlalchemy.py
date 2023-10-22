from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection
from core.infra.database.sqlalchemy_tables import EmployeeTable


class SQLAlchemyEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, sqlalchemy_conn: SQLAlchemyConnection):
        self.database_conn = sqlalchemy_conn

    def get_employees(self) -> list[dict]:
        employees = self.database_conn.session.query(EmployeeTable).all()
        return list(map(lambda x: x.to_dict(), employees))

    def get_employee_by_id(self, id: int) -> dict | None:
        employee = self.database_conn.session.query(EmployeeTable).get(id)
        if employee:
            return employee.to_dict()
        else:
            return None

    def get_employee_by_cpf(self, cpf: str) -> dict | None:
        employee = (
            self.database_conn.session.query(EmployeeTable)
            .filter(EmployeeTable.cpf == cpf)
            .one_or_none()
        )
        if employee:
            return employee.to_dict()
        else:
            return None

    def create_employee(self, employee: Employee) -> None:
        employee_table = EmployeeTable(employee)
        self.database_conn.session.add(employee_table)
        self.database_conn.session.commit()

    def delete_employee_by_id(self, employee_id) -> bool:
        employee = (
            self.database_conn.session.query(EmployeeTable)
            .filter(EmployeeTable.id == employee_id)
            .one_or_none()
        )
        if employee:
            self.database_conn.session.delete(employee)
            self.database_conn.session.commit()
            return True
        else:
            return False

    def update_employee(self, id, employee_editable_fields: dict) -> None:
        employee_id = id
        self.database_conn.session.query(EmployeeTable).filter(
            EmployeeTable.id == employee_id
        ).update(employee_editable_fields)
        self.database_conn.session.commit()
