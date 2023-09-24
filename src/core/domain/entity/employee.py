from dataclasses import asdict, dataclass
from typing import Optional

from core.shared.CPF import validate_cpf
from core.shared.exceptions import InvalidCPF


@dataclass
class Employee:
    """Class that represents employee domain object"""

    id: int
    name: str
    cpf: str
    gender_id: int
    phone: str
    email: str
    CEP: str
    address: str
    address_number: int
    gender: Optional[str] = None

    def __post_init__(self):
        if not validate_cpf(self.cpf):
            raise InvalidCPF("Invalid CPF")

    def to_dict(self):
        return asdict(self)
