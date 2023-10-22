from core.application.repository.employee_repository import EmployeeRepositoryInterface
from core.shared.exceptions import EmployeeNotFound, EmployeeUpdateException


class UpdateEmployeeInfoService:
    def __init__(self, employee_repository: EmployeeRepositoryInterface):
        self.employee_repository = employee_repository

    # This is temporary only to keep consistency
    def _filter_editable_fields(self, fields):
        editable_fields = dict()
        editable_fields["name"] = fields["name"]
        editable_fields["gender_id"] = fields["gender_id"]
        return editable_fields

    def execute(self, id, body):
        body["id"] = id
        employee_record = self.employee_repository.get_employee_by_cpf(body["cpf"])
        if not employee_record:
            raise EmployeeNotFound("Employee Not Found!")
        elif employee_record["id"] != id:
            raise EmployeeUpdateException("User ID and CPF Mismatch")

        return self.employee_repository.update_employee(
            id, self._filter_editable_fields(body)
        )
