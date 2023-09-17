from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.domain.entity.employee import Employee
from core.infra.database.sqlalchemy_adapter import SQLAlchemyConnection

class_base = SQLAlchemyConnection.base
base_mixin = SQLAlchemyConnection.base_mixin


class GenderTable(class_base, base_mixin):
    __tablename__ = "gender"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    employees = relationship("EmployeeTable", back_populates="gender", lazy=True)

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
    gender_id = Column(Integer, ForeignKey("gender.id"))

    gender = relationship("GenderTable", back_populates="employees", lazy=True)

    def __init__(self, name, cpf, gender_id, **kwargs):
        self.name = name
        self.gender_id = gender_id
        self.cpf = cpf

    def to_entity(self):
        return Employee(
            name=self.name,
            id=self.id,
            cpf=self.cpf,
            gender_id=self.gender_id,
            gender=self.gender,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "gender": self.gender.name,
            "gender_id": self.gender_id,
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
