"""empty message

Revision ID: 84d5aea46a84
Revises: 
Create Date: 2019-04-24 11:53:36.497514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84d5aea46a84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    # ### end Alembic commands ###
