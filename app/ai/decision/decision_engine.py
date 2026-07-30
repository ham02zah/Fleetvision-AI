from app.ai.decision.decision_types import (
    DecisionPriority,
    VehicleDecision,
)
from datetime import datetime

class AIDecisionEngine:
    """
    Enterprise AI decision engine.

    Consumes every AI module and produces one final
    operational decision.
    """

    @staticmethod
    def decide(
        *,
        risk_level,
        maintenance_level,
        health_status,
        driver_grade,
        anomalies,
    ):

        reasons = []

        priority = DecisionPriority.LOW
        action = VehicleDecision.CONTINUE

        ####################################################
        # Risk
        ####################################################

        if risk_level == "HIGH":
            priority = DecisionPriority.HIGH
            action = VehicleDecision.REDUCE_SPEED

            reasons.append(
                "High driving risk detected."
            )

        ####################################################
        # Maintenance
        ####################################################

        if maintenance_level == "HIGH":

            priority = DecisionPriority.HIGH

            action = VehicleDecision.SCHEDULE_SERVICE

            reasons.append(
                "Vehicle requires maintenance."
            )

        ####################################################
        # Health
        ####################################################

        if health_status == "POOR":

            priority = DecisionPriority.CRITICAL

            action = VehicleDecision.STOP_IMMEDIATELY

            reasons.append(
                "Vehicle health is critical."
            )

        ####################################################
        # Driver
        ####################################################

        if driver_grade in ["D", "F"]:

            reasons.append(
                "Unsafe driving behaviour."
            )

        ####################################################
        # Anomalies
        ####################################################

        if anomalies:

            priority = DecisionPriority.CRITICAL

            action = VehicleDecision.STOP_IMMEDIATELY

            reasons.append(
                "Critical anomaly detected."
            )

        ####################################################
        # Confidence
        ####################################################

        if priority == DecisionPriority.CRITICAL:
            confidence = 0.98

        elif priority == DecisionPriority.HIGH:
            confidence = 0.92

        elif priority == DecisionPriority.MEDIUM:
            confidence = 0.84

        else:
            confidence = 0.76

        ####################################################
        # Final response
        ####################################################

        return {

            "overall_status": priority.value,

            "priority": priority.value,

            "action": action.value,

            "confidence": confidence,

            "reasons": reasons,

            "generated_at": datetime.utcnow().isoformat(),

        }