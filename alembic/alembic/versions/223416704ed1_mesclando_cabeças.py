"""Mesclando cabeças

Revision ID: 223416704ed1
Revises: 0be4a1d1c164, 9035b8f9fc06, f1492786fa94
Create Date: 2024-11-29 17:58:06.592266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '223416704ed1'
down_revision: Union[str, None] = ('0be4a1d1c164', '9035b8f9fc06', 'f1492786fa94')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
