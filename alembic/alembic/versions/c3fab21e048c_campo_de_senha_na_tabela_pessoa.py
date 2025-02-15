"""campo de senha na tabela pessoa

Revision ID: c3fab21e048c
Revises: c358c987ac4e
Create Date: 2024-11-29 17:12:14.231373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3fab21e048c'
down_revision: Union[str, None] = 'c358c987ac4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa', sa.Column('senha', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa', 'senha')
    # ### end Alembic commands ###
