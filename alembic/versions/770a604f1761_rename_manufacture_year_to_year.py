"""rename manufacture_year to year

Revision ID: 770a604f1761
Revises: 70580ad3c424
Create Date: 2026-07-21 11:52:54.959975
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "770a604f1761"
down_revision: Union[str, Sequence[str], None] = "70580ad3c424"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "vehicles",
        "manufacture_year",
        new_column_name="year",
    )


def downgrade() -> None:
    op.alter_column(
        "vehicles",
        "year",
        new_column_name="manufacture_year",
    )