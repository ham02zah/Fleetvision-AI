from pydantic import BaseModel


class GPSDistanceResponse(BaseModel):
    """
    GPS calculation response.
    """

    distance_km: float

    average_speed: float