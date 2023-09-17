from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.application.service.employee import (
    CreateEmployeeService,
    GetEmployeeByIdService,
    GetEmployeeService,
)


class EmployeeController:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.create_employee_svc = CreateEmployeeService(employee_repository)
        self.get_employees_svc = GetEmployeeService(employee_repository)
        self.get_employee_by_id_svc = GetEmployeeByIdService(employee_repository)

    def get_employees(self):
        return self.get_employees_svc.execute(), 200

    def get_employee_by_id(self, id):
        return self.get_employee_by_id_svc.execute(id), 200

    def create_employee(self, body):
        return self.create_employee_svc.execute(body), 200
