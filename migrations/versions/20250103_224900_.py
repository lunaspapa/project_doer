"""empty message

Revision ID: cf9fba03cf2c
Revises: 900b3d95f4f9
Create Date: 2025-01-03 22:49:00.062811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf9fba03cf2c'
down_revision = '900b3d95f4f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('meetline', sa.Date(), nullable=True),
    sa.Column('is_daily', sa.Boolean(), nullable=False),
    sa.Column('streak', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('minigoals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('objective', sa.String(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subgoals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('meet_by', sa.Date(), nullable=True),
    sa.Column('is_daily', sa.Boolean(), nullable=False),
    sa.Column('streak', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subgoals')
    op.drop_table('posties')
    op.drop_table('minigoals')
    op.drop_table('goals')
    # ### end Alembic commands ###