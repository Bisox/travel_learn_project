"""Initial migration

Revision ID: 9c8f3fb84770
Revises: 
Create Date: 2024-09-06 03:51:00.397367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c8f3fb84770'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'hotels',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('services', sa.JSON),
        sa.Column('rooms_quantity', sa.Integer(), nullable=False),
        sa.Column('image_id', sa.Integer())
    )



def downgrade() -> None:
    pass
