from dataclasses import dataclass

from core.domain.utils.CPF import CPF

# from exceptions import EmployeeTableException


@dataclass
class Employee:
    """Class that represents employee domain object"""

    id: int
    name: str
    CPF: str
    # phone: str
    # email: str
    # gender: str
    # CEP: str
    # address: str
    # address_number: int
