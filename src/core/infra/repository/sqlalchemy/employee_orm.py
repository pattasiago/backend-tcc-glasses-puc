from sqlalchemy import Column, Integer, String

from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection


class EmployeeORMCreator:
    def __new__(cls, sql_alchemy_conn: SQLAlchemyConnection):
        class_base = sql_alchemy_conn.base

        class EmployeeORM(class_base):
            __tablename__ = "employees"

            id = Column(Integer, primary_key=True)
            name = Column(String)
            cpf = Column(String)

            def to_entity(self):
                return Employee(name=self.name, id=self.id, CPF=self.cpf)

            def to_dict(self):
                return {"id": self.id, "name": self.name}

        return EmployeeORM
