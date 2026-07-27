from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from app.core.config import settings


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)


OUTPUT_DIR = Path("datasets/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_vehicle_status():
    """
    Export vehicle_status table to CSV.
    """

    query = """
    SELECT *
    FROM vehicle_status
    ORDER BY last_seen DESC;
    """

    df = pd.read_sql(query, engine)

    output_file = OUTPUT_DIR / "vehicle_status.csv"

    df.to_csv(
        output_file,
        index=False,
    )

    print(f"Dataset saved to {output_file}")


if __name__ == "__main__":
    export_vehicle_status()