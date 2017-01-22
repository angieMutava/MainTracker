"""empty message

Revision ID: 286096ae17e9
Revises: 6c4dc0dda055
Create Date: 2017-01-22 03:10:10.869000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '286096ae17e9'
down_revision = '6c4dc0dda055'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assigns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=64), nullable=True),
    sa.Column('issue', sa.String(length=64), nullable=True),
    sa.Column('department', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assigns')
    # ### end Alembic commands ###