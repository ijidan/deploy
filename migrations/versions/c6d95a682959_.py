"""empty message

Revision ID: c6d95a682959
Revises: 75fe4af92296
Create Date: 2016-06-04 09:56:33.785000

"""

# revision identifiers, used by Alembic.
revision = 'c6d95a682959'
down_revision = '75fe4af92296'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_name', sa.VARCHAR(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_name')
    ### end Alembic commands ###
