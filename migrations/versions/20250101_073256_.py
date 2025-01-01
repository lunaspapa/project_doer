"""empty message

Revision ID: 6519d92e7de0
Revises: 
Create Date: 2025-01-01 07:32:56.806739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6519d92e7de0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('goals_met', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###