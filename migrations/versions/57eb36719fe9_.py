"""empty message

Revision ID: 57eb36719fe9
Revises: 5b7fdb9b5dce
Create Date: 2020-03-29 22:15:12.004749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57eb36719fe9'
down_revision = '5b7fdb9b5dce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('location', sa.String(length=60), nullable=True))
    op.add_column('contacts', sa.Column('organization', sa.String(length=60), nullable=True))
    op.add_column('contacts', sa.Column('title', sa.String(length=60), nullable=True))
    op.add_column('contacts', sa.Column('website', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_contacts_organization'), 'contacts', ['organization'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_organization'), table_name='contacts')
    op.drop_column('contacts', 'website')
    op.drop_column('contacts', 'title')
    op.drop_column('contacts', 'organization')
    op.drop_column('contacts', 'location')
    # ### end Alembic commands ###