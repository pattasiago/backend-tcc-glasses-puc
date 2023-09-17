from core.application.repository.employee_repository import EmployeeRepositoryInterface


class GetEmployeeByIdService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, id):
        return self.employee_repository.get_employee_by_id(id)
