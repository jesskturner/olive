"""empty message

Revision ID: 517f4c40983a
Revises: 1ea07dc58e7e
Create Date: 2019-03-11 22:48:02.409700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '517f4c40983a'
down_revision = '1ea07dc58e7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('user', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'task', 'user', ['user'], ['id'])
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'user')
    # ### end Alembic commands ###