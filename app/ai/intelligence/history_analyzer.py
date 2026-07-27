from app.models.telemetry import Telemetry


class HistoryAnalyzer:
    """
    Analyze historical telemetry trends.
    """

    @staticmethod
    def analyze(records: list[Telemetry]):
        if not records:
            return {
                "average_speed": 0,
                "max_speed": 0,
                "average_engine_temp": 0,
                "average_fuel": 0,
                "total_records": 0,
                "overspeed_events": 0,
            }

        avg_speed = (
            sum(r.speed for r in records)
            / len(records)
        )

        max_speed = max(
            r.speed for r in records
        )

        avg_temp = (
            sum(r.engine_temp for r in records)
            / len(records)
        )

        avg_fuel = (
            sum(r.fuel for r in records)
            / len(records)
        )

        overspeed_events = len(
            [
                r
                for r in records
                if r.speed >= 100
            ]
        )

        return {
            "average_speed": round(avg_speed, 2),
            "max_speed": round(max_speed, 2),
            "average_engine_temp": round(avg_temp, 2),
            "average_fuel": round(avg_fuel, 2),
            "total_records": len(records),
            "overspeed_events": overspeed_events,
        }