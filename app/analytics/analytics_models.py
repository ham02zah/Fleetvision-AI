from dataclasses import dataclass


@dataclass
class FleetStatistics:

    total_vehicles: int

    active_vehicles: int

    idle_vehicles: int

    average_speed: float

    average_fuel: float

    average_engine_temperature: float

    total_distance: float


@dataclass
class FleetHealth:

    score: float

    status: str


@dataclass
class FleetRisk:

    score: float

    level: str


@dataclass
class FleetAnalytics:

    statistics: FleetStatistics

    health: FleetHealth

    risk: FleetRisk