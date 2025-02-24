"""followers

Revision ID: 265bbe0c7758
Revises: 1bd3f0ce944c
Create Date: 2025-02-24 16:12:45.680212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265bbe0c7758'
down_revision = '1bd3f0ce944c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
