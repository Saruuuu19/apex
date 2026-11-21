"""Create auth sessions.

Revision ID: 3d90b14f765c
Revises: 1454210192a8
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "3d90b14f765c"
down_revision: str | Sequence[str] | None = "1454210192a8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "auth_sessions",
        sa.Column("token_hash", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("token_hash"),
    )


def downgrade() -> None:
    op.drop_table("auth_sessions")
