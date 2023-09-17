from flask_restx import fields

from web.models.model import ApiModel

employee_model = ApiModel(
    "Employee",
    {
        "id": fields.Integer(required=False, description="employee id"),
        "name": fields.String(required=False, description="employee name"),
        "CPF": fields.String(required=False, description="employee CPF"),
    },
)

employee_model_creation = ApiModel(
    "EmployeeCreation",
    {
        "name": fields.String(required=True, description="employee name"),
        "cpf": fields.String(
            required=True,
            description="employee CPF",
            pattern=r"^\d{3}\d{3}\d{3}\d{2}$",
        ),
        "gender_id": fields.Integer(required=True, description="employee gender"),
    },
)
