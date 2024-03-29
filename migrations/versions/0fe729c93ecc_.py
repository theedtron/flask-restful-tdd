"""empty message

Revision ID: 0fe729c93ecc
Revises: a6a242f43d1c
Create Date: 2019-06-10 21:10:03.971504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fe729c93ecc'
down_revision = 'a6a242f43d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('bucketlists', sa.Column('created_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bucketlists', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bucketlists', type_='foreignkey')
    op.drop_column('bucketlists', 'created_by')
    op.drop_table('users')
    # ### end Alembic commands ###
