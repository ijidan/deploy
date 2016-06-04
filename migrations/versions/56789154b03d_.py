"""empty message

Revision ID: 56789154b03d
Revises: 419696dc46c6
Create Date: 2016-05-29 09:48:28.568000

"""

# revision identifiers, used by Alembic.
revision = '56789154b03d'
down_revision = '419696dc46c6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('environ',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('env_id', sa.INTEGER(), nullable=True),
    sa.Column('env_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('env__description', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_environ_env_id'), 'environ', ['env_id'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_environ_env_id'), table_name='environ')
    op.drop_table('environ')
    ### end Alembic commands ###