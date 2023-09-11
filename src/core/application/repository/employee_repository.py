from abc import ABC, abstractmethod


class EmployeeRepositoryInterface(ABC):
    @abstractmethod
    def get_employees(self):
        pass
