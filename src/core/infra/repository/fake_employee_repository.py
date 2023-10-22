from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.domain.entity.employee import Employee


class FakeEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self):
        pass

    def get_employees(self) -> list[dict]:
        pass

    def get_employee_by_id(self, id: int) -> dict | None:
        pass

    def get_employee_by_cpf(self, cpf: str) -> dict | None:
        pass

    def create_employee(self, employee: Employee) -> None:
        pass

    def delete_employee_by_id(self, id: int) -> dict | None:
        pass

    def update_employee(self, id, employee_editable_fields: dict) -> None:
        pass
