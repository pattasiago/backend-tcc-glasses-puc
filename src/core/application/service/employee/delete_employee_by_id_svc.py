from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.shared.exceptions import EmployeeNotFound


class DeleteEmployeeByIdService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, id):
        employee = self.employee_repository.delete_employee_by_id(id)
        if not employee:
            raise EmployeeNotFound("Employee Not Found!")
        else:
            return employee
