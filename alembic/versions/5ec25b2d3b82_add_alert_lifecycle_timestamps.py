
"""add alert lifecycle timestamps

Revision ID: 5ec25b2d3b82
Revises: 00fe235c1463
Create Date: 2026-08-11 00:25:12.523809

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# ==========================================================
# Revision identifiers
# ==========================================================

revision: str = "5ec25b2d3b82"

down_revision: Union[str, Sequence[str], None] = "00fe235c1463"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None


# ==========================================================
# Upgrade
# ==========================================================


def upgrade() -> None:
    """Add alert lifecycle timestamp columns."""

    op.add_column(
        "alerts",
        sa.Column(
            "acknowledged_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )

    op.add_column(
        "alerts",
        sa.Column(
            "resolved_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )


# ==========================================================
# Downgrade
# ==========================================================


def downgrade() -> None:
    """Remove alert lifecycle timestamp columns."""

    op.drop_column(
        "alerts",
        "resolved_at",
    )

    op.drop_column(
        "alerts",
        "acknowledged_at",
    )

