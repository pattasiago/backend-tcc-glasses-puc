from flask import jsonify

from core.application.repository.employee_repository import EmployeeRepositoryInterface


class EmployeeController:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    def get_employees(self):
        # TODO usar um service
        return self.employee_repository.get_employees(), 200
