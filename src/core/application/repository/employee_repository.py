from abc import ABC, abstractmethod


class EmployeeRepositoryInterface(ABC):
    @abstractmethod
    def get_employees(self):
        pass

    @abstractmethod
    def get_employee_by_id(self, id):
        pass

    @abstractmethod
    def create_employee(self, body):
        pass
