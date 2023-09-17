from core.application.repository.employee_repository import EmployeeRepositoryInterface


class GetEmployeeByIdService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def execute(self, id, asdict=True):
        if asdict:
            return self.employee_repository.get_employee_by_id(id).to_dict()
        else:
            return self.employee_repository.get_employee_by_id(id)
