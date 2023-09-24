from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.domain.entity.employee import Employee
from core.shared.exceptions import CPFAlreadyExists


class CreateEmployeeService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, body):
        body["id"] = None
        employee = Employee(**body)
        cpf_exists = self.employee_repository.get_employee_by_cpf(employee.cpf)
        if cpf_exists:
            raise CPFAlreadyExists("CPF Already Exists")
        return self.employee_repository.create_employee(employee)
