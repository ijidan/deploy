"""empty message

Revision ID: 033dbdd16291
Revises: 95b759e6cf22
Create Date: 2016-05-29 13:39:50.221000

"""

# revision identifiers, used by Alembic.
revision = '033dbdd16291'
down_revision = '95b759e6cf22'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('server_no', sa.VARCHAR(length=20), nullable=True),
    sa.Column('server_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('server_ip', sa.VARCHAR(length=20), nullable=True),
    sa.Column('env_id', sa.INTEGER(), nullable=True),
    sa.Column('project_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_server_env_id'), 'server', ['env_id'], unique=False)
    op.create_index(op.f('ix_server_project_id'), 'server', ['project_id'], unique=False)
    op.create_index(op.f('ix_server_server_no'), 'server', ['server_no'], unique=False)
    op.add_column(u'environ', sa.Column('env_no', sa.VARCHAR(length=20), nullable=True))
    op.create_index(op.f('ix_environ_env_no'), 'environ', ['env_no'], unique=False)
    op.drop_index('ix_environ_env_id', table_name='environ')
    op.drop_column(u'environ', 'env_id')
    op.add_column(u'project', sa.Column('project_no', sa.VARCHAR(length=50), nullable=True))
    op.create_index(op.f('ix_project_project_no'), 'project', ['project_no'], unique=False)
    op.drop_index('ix_project_project_id', table_name='project')
    op.drop_column(u'project', 'project_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'project', sa.Column('project_id', mysql.VARCHAR(length=50), nullable=True))
    op.create_index('ix_project_project_id', 'project', ['project_id'], unique=True)
    op.drop_index(op.f('ix_project_project_no'), table_name='project')
    op.drop_column(u'project', 'project_no')
    op.add_column(u'environ', sa.Column('env_id', mysql.VARCHAR(length=20), nullable=True))
    op.create_index('ix_environ_env_id', 'environ', ['env_id'], unique=True)
    op.drop_index(op.f('ix_environ_env_no'), table_name='environ')
    op.drop_column(u'environ', 'env_no')
    op.drop_index(op.f('ix_server_server_no'), table_name='server')
    op.drop_index(op.f('ix_server_project_id'), table_name='server')
    op.drop_index(op.f('ix_server_env_id'), table_name='server')
    op.drop_table('server')
    ### end Alembic commands ###
