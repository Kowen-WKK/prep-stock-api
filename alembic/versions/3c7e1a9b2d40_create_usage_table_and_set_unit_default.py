"""create usage table and set unit default

Revision ID: 3c7e1a9b2d40
Revises: fd2b7ae564e3
Create Date: 2026-11-04 17:25:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c7e1a9b2d40'
down_revision: Union[str, Sequence[str], None] = 'fd2b7ae564e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'usage',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_id', sa.Integer(), sa.ForeignKey('items.id'), nullable=False),
        sa.Column('used_on', sa.Date(), server_default=sa.func.current_date(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.CheckConstraint('quantity > 0', name='usage_quantity_positive'),
    )
    op.alter_column('items', 'unit', existing_type=sa.String(), server_default='bag')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('items', 'unit', existing_type=sa.String(), server_default=None)
    op.drop_table('usage')
