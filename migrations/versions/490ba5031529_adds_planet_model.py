"""adds Planet model

Revision ID: 490ba5031529
Revises: 
Create Date: 2023-04-28 11:20:33.332170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490ba5031529'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True, not_null=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
