"""add gender column

Revision ID: 04ffc2b257fe
Revises: a16983dd21c1
Create Date: 2023-09-17 10:05:03.269224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04ffc2b257fe'
down_revision: Union[str, None] = 'a16983dd21c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('gender_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employees', 'gender', ['gender_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.drop_column('employees', 'gender_id')
    # ### end Alembic commands ###
