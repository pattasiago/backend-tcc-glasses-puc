from flask_restx import Namespace, Resource

from config import employee_repository
from web.controllers.employee_controller import EmployeeController

employee_ns = Namespace("employee", description="Employee Related Operations")

employee_controller = EmployeeController(employee_repository)


@employee_ns.route("")
class Employee(Resource):
    def get(self):
        employee_ns.logger.debug("Entrou Endpoint")
        employees = employee_controller.get_employees()
        return employees
