"""empty message

Revision ID: cb7d71fe3c92
Revises: 843126f75f69
Create Date: 2023-12-10 22:53:30.824035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7d71fe3c92'
down_revision = '843126f75f69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('astra_users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=300), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('astra_users', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
