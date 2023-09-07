"""remove unique constraint on table

Revision ID: 1981f9ac77ca
Revises: 5db28fa97e06
Create Date: 2023-09-07 10:55:51.377366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1981f9ac77ca'
down_revision: Union[str, None] = '5db28fa97e06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('museum_artists', schema=None) as batch_op:
        batch_op.alter_column('museum_id',
               existing_type=sa.INTEGER(),
               nullable=True, unique = False)
        batch_op.alter_column('artists_id',
               existing_type=sa.INTEGER(),
               nullable=True, unique = False)
    pass


def downgrade() -> None:
    pass
