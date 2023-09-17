from dataclasses import asdict, dataclass

from core.shared.CPF import validate_cpf
from core.shared.exceptions import InvalidCPF

# from exceptions import EmployeeTableException


@dataclass
class Employee:
    """Class that represents employee domain object"""

    id: int
    name: str
    cpf: str
    # phone: str
    # email: str
    # gender: str
    # CEP: str
    # address: str
    # address_number: int

    def __post_init__(self):
        if not validate_cpf(self.cpf):
            raise InvalidCPF("CPF Inválido")

    def to_dict(self):
        return asdict(self)
