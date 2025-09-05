"""Add FAQ table

Revision ID: 01337065af93
Revises: <previous_revision_id>
Create Date: 2025-09-05 12:34:56.789012
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '01337065af93'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'faqs',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('question', sa.String, nullable=False),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('business_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.func.now())
    )

def downgrade():
    op.drop_table('faqs')
