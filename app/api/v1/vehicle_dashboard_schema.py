from pydantic import BaseModel


class VehicleInfo(BaseModel):

    id: int

    plate: str

    status: str


class TelemetryInfo(BaseModel):

    speed: float

    fuel: float

    engine_temp: float


class VehicleDashboardResponse(BaseModel):

    vehicle: VehicleInfo

    telemetry: TelemetryInfo

    ai: dict