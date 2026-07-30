"""create alerts table

Revision ID: e9273966f704
Revises: 7cde5d85bfd4
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision = "e9273966f704"
down_revision = "7cde5d85bfd4"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "alerts",

        sa.Column(
            "id",
            sa.UUID(),
            primary_key=True,
            nullable=False,
        ),

        sa.Column(
            "vehicle_id",
            sa.UUID(),
            nullable=False,
        ),

        sa.Column(
            "title",
            sa.String(255),
            nullable=False,
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "alert_type",
            sa.Enum(
                "SPEEDING",
                "FATIGUE",
                "COLLISION",
                "MAINTENANCE",
                "ENGINE",
                "FUEL",
                "BATTERY",
                "GEOFENCE",
                "AI_RISK",
                name="alert_type_enum",
            ),
            nullable=False,
        ),

        sa.Column(
            "severity",
            sa.Enum(
                "LOW",
                "MEDIUM",
                "HIGH",
                "CRITICAL",
                name="alert_severity_enum",
            ),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.Enum(
                "ACTIVE",
                "ACKNOWLEDGED",
                "RESOLVED",
                name="alert_status_enum",
            ),
            nullable=False,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["vehicle_id"],
            ["vehicles.id"],
            ondelete="CASCADE",
        ),
    )


def downgrade():

    op.drop_table("alerts")