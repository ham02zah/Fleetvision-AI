from app.ai.inference.speed_predictor import predict_speed
from app.ai.inference.risk_detector import detect_speed_risk
from app.ai.services.maintenance_service import MaintenanceAIService
from app.ai.intelligence.health_score import VehicleHealthScore
from app.models.telemetry import Telemetry
from app.ai.intelligence.driver_behavior import DriverBehaviorAnalyzer
from app.ai.anomaly.anomaly_service import AnomalyService
from app.ai.recommendations.recommendation_engine import RecommendationEngine
from app.ai.anomaly.advanced_anomaly_detector import AdvancedAnomalyDetector
from app.ai.explainability.explanation_engine import ExplainabilityEngine
from app.ai.feature_engineering.feature_pipeline import FeaturePipeline
from app.ai.decision.decision_engine import AIDecisionEngine


class AIIntelligenceService:
    """
    Central AI orchestration service.
    """

    @staticmethod
    def analyze(
        telemetry: Telemetry,
        previous_speed: float = 0.0,
    ):

        print("\n" + "=" * 80)
        print("AIIntelligenceService.analyze() CALLED")
        print("=" * 80)

        ###################################################
        # Speed Prediction
        ###################################################

        speed_prediction = predict_speed(
            speed=telemetry.speed,
            previous_speed=previous_speed,
        )

        ###################################################
        # Risk Detection
        ###################################################

        risk_analysis = detect_speed_risk(
            speed=telemetry.speed,
            previous_speed=previous_speed,
        )

        ###################################################
        # Maintenance
        ###################################################

        maintenance_analysis = MaintenanceAIService.analyze(
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
            odometer=telemetry.odometer,
            speed=telemetry.speed,
        )

        ###################################################
        # Vehicle Health
        ###################################################

        health_analysis = VehicleHealthScore.calculate(
            speed=telemetry.speed,
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
            odometer=telemetry.odometer,
            risk_level=risk_analysis["risk_level"],
            maintenance_level=maintenance_analysis["maintenance_level"],
        )

        ###################################################
        # Anomaly Detection
        ###################################################

        anomaly_analysis = AnomalyService.analyze(
            speed=telemetry.speed,
            previous_speed=previous_speed,
            latitude=telemetry.latitude,
            longitude=telemetry.longitude,
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
            ignition=telemetry.ignition,
            engine_running=telemetry.engine_running,
        )

        ###################################################
        # Advanced Anomaly
        ###################################################

        advanced_anomaly_analysis = AdvancedAnomalyDetector.analyze(
            speed=telemetry.speed,
            previous_speed=previous_speed,
            latitude=telemetry.latitude,
            longitude=telemetry.longitude,
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
            ignition=telemetry.ignition,
            engine_running=telemetry.engine_running,
        )

        ###################################################
        # Driver Behaviour
        ###################################################

        driver_analysis = DriverBehaviorAnalyzer.analyze(
            speed=telemetry.speed,
            previous_speed=previous_speed,
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
        )

        ###################################################
        # Recommendations
        ###################################################

        recommendations = RecommendationEngine.generate(
            speed=telemetry.speed,
            fuel=telemetry.fuel,
            engine_temp=telemetry.engine_temp,
            risk_level=risk_analysis["risk_level"],
            maintenance_level=maintenance_analysis["maintenance_level"],
            health_status=health_analysis["status"],
            driver_grade=driver_analysis["grade"],
        )

        ###################################################
        # Decision Engine
        ###################################################

        decision = AIDecisionEngine.decide(
            risk_level=risk_analysis["risk_level"],
            maintenance_level=maintenance_analysis["maintenance_level"],
            health_status=health_analysis["status"],
            driver_grade=driver_analysis["grade"],
            anomalies=anomaly_analysis["anomalies"],
        )

        ###################################################
        # Explainability
        ###################################################

        explanations = ExplainabilityEngine.generate(
            telemetry=telemetry,
            risk_level=risk_analysis["risk_level"],
            maintenance_level=maintenance_analysis["maintenance_level"],
            health_score=health_analysis["health_score"],
            driver_grade=driver_analysis["grade"],
            anomalies=anomaly_analysis["anomalies"],
        )

        ###################################################
        # Feature Engineering
        ###################################################

        engineered_features = FeaturePipeline.process(
            telemetry=telemetry,
            previous_speed=previous_speed,
        )

        ###################################################
        # FINAL RESPONSE
        ###################################################

        response = {

            "prediction": speed_prediction,

            "risk_level": risk_analysis["risk_level"],

            "risk_score": risk_analysis.get(
                "risk_score",
                0,
            ),

            "speed_prediction": speed_prediction,

            "risk_analysis": risk_analysis,

            "maintenance_analysis": maintenance_analysis,

            "vehicle_health": health_analysis,

            "driver_score": driver_analysis,

            "anomaly_analysis": anomaly_analysis,

            "advanced_anomaly_analysis": advanced_anomaly_analysis,

            "recommendations": recommendations,

            "ai_decision": decision,

            "explanations": {
                "explanations": explanations,
            },

            "engineered_features": engineered_features,
        }

        print("\nFINAL RESPONSE KEYS:")
        print(list(response.keys()))

        print("\nFULL RESPONSE:")
        print(response)

        print("=" * 80)

        return response