from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.application.service.employee import (
    CreateEmployeeService,
    DeleteEmployeeByIdService,
    GetEmployeeByIdService,
    GetEmployeeService,
    UpdateEmployeeInfoService,
)
from core.shared.exceptions import (
    CPFException,
    EmployeeNotFound,
    EmployeeUpdateException,
)


class EmployeeController:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.create_employee_svc = CreateEmployeeService(employee_repository)
        self.get_employees_svc = GetEmployeeService(employee_repository)
        self.get_employee_by_id_svc = GetEmployeeByIdService(employee_repository)
        self.delete_employee_by_id_svc = DeleteEmployeeByIdService(employee_repository)
        self.update_employee_svc = UpdateEmployeeInfoService(employee_repository)

    def get_employees(self):
        return self.get_employees_svc.execute(), 200

    def get_employee_by_id(self, id):
        try:
            return self.get_employee_by_id_svc.execute(id), 200
        except EmployeeNotFound as enf:
            return {"message": str(enf)}, 400

    def create_employee(self, body):
        try:
            return self.create_employee_svc.execute(body), 201
        except CPFException as cpfe:
            return {"message": str(cpfe)}, 400

    def delete_employee_by_id(self, id):
        try:
            return self.delete_employee_by_id_svc.execute(id), 200
        except EmployeeNotFound as enf:
            return {"message": str(enf)}, 400

    def update_employee(self, id, body):
        try:
            return self.update_employee_svc.execute(id, body), 201
        except (EmployeeUpdateException, EmployeeNotFound) as employ_update_exc:
            return {"message": str(employ_update_exc)}, 400
