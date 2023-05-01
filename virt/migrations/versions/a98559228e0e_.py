"""empty message

Revision ID: a98559228e0e
Revises: 6e9705802b2a
Create Date: 2022-09-25 20:08:10.920251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a98559228e0e'
down_revision = '6e9705802b2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic')
    # ### end Alembic commands ###
