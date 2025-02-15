"""Criando tabela notas

Revision ID: b9275e825712
Revises: f2406adf822f
Create Date: 2024-11-29 18:05:50.761420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9275e825712'
down_revision: Union[str, None] = 'f2406adf822f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_aluno', sa.String(length=50), nullable=False),
    sa.Column('email_aluno', sa.String(length=50), nullable=False),
    sa.Column('nota', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notas')
    # ### end Alembic commands ###
