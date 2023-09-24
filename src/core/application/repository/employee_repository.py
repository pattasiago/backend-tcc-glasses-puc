from abc import ABC, abstractmethod

from core.domain.entity.employee import Employee


class EmployeeRepositoryInterface(ABC):
    @abstractmethod
    def get_employees(self):
        pass

    @abstractmethod
    def get_employee_by_id(self, id):
        pass

    @abstractmethod
    def create_employee(self, body: Employee):
        pass
