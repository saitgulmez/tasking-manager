"""empty message

Revision ID: 068674f06b0f
Revises: 0eee8c1abd3a
Create Date: 2019-10-02 08:45:00.553060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "068674f06b0f"
down_revision = "0eee8c1abd3a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("picture_url", sa.String(), nullable=True))
    op.alter_column(
        "users",
        "expert_mode",
        existing_type=sa.BOOLEAN(),
        nullable=True,
        existing_server_default=sa.text("false"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "expert_mode",
        existing_type=sa.BOOLEAN(),
        nullable=False,
        existing_server_default=sa.text("false"),
    )
    op.drop_column("users", "picture_url")
    # ### end Alembic commands ###