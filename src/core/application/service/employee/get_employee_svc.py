from core.application.repository.employee_repository import EmployeeRepositoryInterface


class GetEmployeeService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, asdict=True):
        if asdict:
            return [employee for employee in self.employee_repository.get_employees()]
        else:
            return self.employee_repository.get_employees()
