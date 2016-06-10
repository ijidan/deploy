"""empty message

Revision ID: fd7877e31aa0
Revises: b1cacf9a265f
Create Date: 2016-06-04 10:03:12.790000

"""

# revision identifiers, used by Alembic.
revision = 'fd7877e31aa0'
down_revision = 'b1cacf9a265f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', mysql.ENUM(u'yes', u'no'), nullable=False))
    ### end Alembic commands ###
