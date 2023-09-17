from core.application.repository.employee_repository import EmployeeRepositoryInterface


class CreateEmployeeService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, body):
        return self.employee_repository.create_employee(body)
