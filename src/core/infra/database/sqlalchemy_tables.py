from sqlalchemy import Column, Integer, String

from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection

class_base = SQLAlchemyConnection.base
base_mixin = SQLAlchemyConnection.base_mixin


class GenderTable(class_base, base_mixin):
    __tablename__ = "gender"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class EmployeeTable(class_base, base_mixin):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)

    def to_entity(self):
        return Employee(name=self.name, id=self.id, cpf=self.cpf)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
        }


def init_tables_sqlalchemy(sqlalchemy_conn: SQLAlchemyConnection):
    database_conn = sqlalchemy_conn
    session = database_conn.db_session()

    gender_options = [
        GenderTable(id=1, name="Masculino"),
        GenderTable(id=2, name="Feminino"),
        GenderTable(id=3, name="Outro"),
    ]

    for gender in gender_options:
        session.merge(gender)

    session.commit()
    session.close()
