"""create table

Revision ID: 11d260c8be89
Revises:
Create Date: 2018-04-17 20:38:05.345799

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID


# revision identifiers, used by Alembic.
revision = '11d260c8be89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', UUID, nullable=False, primary_key=True),
        sa.Column('email', sa.String(500)),
        sa.Column('password', sa.String(500)),
        sa.Column('name', sa.String(500)),
        sa.Column('email_verified_at', sa.DateTime),
        sa.Column('status', sa.String(50)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('deleted_at', sa.DateTime),
    )
    op.create_index('idx_user_email', 'user', ['email'])
    op.create_index('idx_user_created_at', 'user', ['created_at'])


def downgrade():
    op.drop_table('user')
