"""empty message

Revision ID: 7d903cd6ad0b
Revises: 1f2866ab5d14
Create Date: 2017-12-14 14:29:42.755596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7d903cd6ad0b'
down_revision = '1f2866ab5d14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('article', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('article', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###