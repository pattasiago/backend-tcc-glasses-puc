from flask_restx import Api

from web.routes.employee_ns import employee_ns

api = Api(version="1.0", title="Glasses Sales")

api.add_namespace(employee_ns)
