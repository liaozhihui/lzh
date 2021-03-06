"""empty message

Revision ID: 65c556318b43
Revises: 
Create Date: 2019-04-10 18:35:52.357195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c556318b43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cname', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_cname'), 'course', ['cname'], unique=True)
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sname', sa.String(length=30), nullable=False),
    sa.Column('sage', sa.Integer(), nullable=False),
    sa.Column('isActive', sa.Boolean(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    op.drop_index(op.f('ix_course_cname'), table_name='course')
    op.drop_table('course')
    # ### end Alembic commands ###
