from flask_restx import Namespace, Resource

from config import employee_repository
from web.controllers.employee_controller import EmployeeController
from web.models.employee_models import employee_model_creation

employee_ns = Namespace("employee", description="Employee Related Operations")

employee_controller = EmployeeController(employee_repository)


@employee_ns.route("")
class Employee(Resource):
    def get(self):
        """Retrieves all employees."""
        employees = employee_controller.get_employees()
        return employees

    @employee_ns.expect(
        employee_ns.model(employee_model_creation.name, employee_model_creation.body),
        validate=True,
    )
    def post(self):
        """Creates a new employee."""
        body = employee_ns.payload
        employees = employee_controller.create_employee(body)
        return employees


@employee_ns.route("/<int:id>")
class EmployeeById(Resource):
    def get(self, id):
        """Retrieves an employee by id."""
        employees = employee_controller.get_employee_by_id(id)
        return employees
