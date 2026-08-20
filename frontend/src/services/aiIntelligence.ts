// ============================================================
// FLEETVISION AI — FRONTEND INTELLIGENCE ENGINE
// ============================================================
//
// This module provides frontend AI intelligence for the
// FleetVision dashboard.
//
// It intentionally does NOT call the backend.
//
// The purpose is to provide:
// - vehicle health scoring
// - fatigue risk
// - maintenance risk
// - anomaly risk
// - overall vehicle risk
// - risk classification
// - recommendations
//
// Later, these calculations can be replaced or supplemented
// by real ML/API predictions without changing the UI.
// ============================================================

import type {
  RiskLevel,
  AIRecommendationPriority,
} from "../types/ai";


// ============================================================
// INPUT TYPES
// ============================================================

export interface VehicleIntelligenceInput {

  vehicleId: string;

  registration: string;

  make: string;

  model: string;

  year: number;

  fuelType?: string;

  isActive?: boolean;

  healthScore?: number;

  fatigueProbability?: number;

  maintenanceProbability?: number;

  anomalyCount?: number;

  engineTemperature?: number;

  harshBrakingEvents?: number;

  harshAccelerationEvents?: number;

  mileage?: number;

  serviceDueDays?: number;
}


// ============================================================
// RESULT TYPE
// ============================================================

export interface VehicleIntelligenceResult {

  vehicleId: string;

  registration: string;

  vehicleName: string;

  riskScore: number;

  riskLevel: RiskLevel;

  healthScore: number;

  fatigueProbability: number;

  maintenanceProbability: number;

  anomalyCount: number;

  anomalyRisk: number;

  driverRisk: number;

  maintenanceRisk: number;

  overallStatus:
    | "Healthy"
    | "Attention Required"
    | "Critical";

  confidence: number;

  recommendations: AIRecommendationResult[];

  summary: string;
}


// ============================================================
// RECOMMENDATION
// ============================================================

export interface AIRecommendationResult {

  id: string;

  priority: AIRecommendationPriority;

  category:
    | "Safety"
    | "Maintenance"
    | "Performance"
    | "Driver";

  title: string;

  description: string;

  recommendation: string;
}


// ============================================================
// HELPERS
// ============================================================

function clamp(
  value: number,
  min = 0,
  max = 100
): number {

  return Math.min(
    Math.max(value, min),
    max
  );
}


function round(
  value: number
): number {

  return Math.round(value);
}


// ============================================================
// RISK LEVEL
// ============================================================

export function getRiskLevel(
  score: number
): RiskLevel {

  if (score >= 80) {
    return "Critical";
  }

  if (score >= 60) {
    return "High";
  }

  if (score >= 35) {
    return "Medium";
  }

  return "Low";
}


// ============================================================
// OVERALL STATUS
// ============================================================

function getOverallStatus(
  score: number
): VehicleIntelligenceResult["overallStatus"] {

  if (score >= 80) {
    return "Critical";
  }

  if (score >= 60) {
    return "Attention Required";
  }

  return "Healthy";
}


// ============================================================
// ANOMALY RISK
// ============================================================

export function calculateAnomalyRisk(
  anomalyCount = 0
): number {

  if (anomalyCount <= 0) {
    return 0;
  }

  if (anomalyCount === 1) {
    return 25;
  }

  if (anomalyCount === 2) {
    return 45;
  }

  if (anomalyCount === 3) {
    return 65;
  }

  if (anomalyCount === 4) {
    return 80;
  }

  return 95;
}


// ============================================================
// DRIVER RISK
// ============================================================

export function calculateDriverRisk(
  fatigueProbability = 0,
  harshBrakingEvents = 0,
  harshAccelerationEvents = 0
): number {

  const fatigueRisk =
    clamp(
      fatigueProbability
    );

  const brakingRisk =
    clamp(
      harshBrakingEvents * 8
    );

  const accelerationRisk =
    clamp(
      harshAccelerationEvents * 5
    );

  const result =
    (
      fatigueRisk * 0.70
    ) +
    (
      brakingRisk * 0.20
    ) +
    (
      accelerationRisk * 0.10
    );

  return round(
    clamp(result)
  );
}


// ============================================================
// MAINTENANCE RISK
// ============================================================

export function calculateMaintenanceRisk(
  maintenanceProbability = 0,
  serviceDueDays = 999
): number {

  const predictionRisk =
    clamp(
      maintenanceProbability
    );

  let serviceRisk = 0;

  if (serviceDueDays <= 0) {

    serviceRisk = 100;

  } else if (serviceDueDays <= 7) {

    serviceRisk = 85;

  } else if (serviceDueDays <= 14) {

    serviceRisk = 65;

  } else if (serviceDueDays <= 30) {

    serviceRisk = 40;

  } else {

    serviceRisk = 10;

  }

  const result =
    (
      predictionRisk * 0.75
    ) +
    (
      serviceRisk * 0.25
    );

  return round(
    clamp(result)
  );
}


// ============================================================
// HEALTH SCORE
// ============================================================

export function calculateHealthScore(
  input: VehicleIntelligenceInput
): number {

  if (
    input.healthScore !== undefined
  ) {

    return round(
      clamp(
        input.healthScore
      )
    );

  }

  let health = 100;

  const anomalyCount =
    input.anomalyCount ?? 0;

  const maintenanceProbability =
    input.maintenanceProbability ?? 0;

  const fatigueProbability =
    input.fatigueProbability ?? 0;

  const temperature =
    input.engineTemperature ?? 90;


  // ----------------------------------------------------------
  // ANOMALIES
  // ----------------------------------------------------------

  health -=
    Math.min(
      anomalyCount * 7,
      30
    );


  // ----------------------------------------------------------
  // MAINTENANCE
  // ----------------------------------------------------------

  health -=
    maintenanceProbability * 0.20;


  // ----------------------------------------------------------
  // DRIVER FATIGUE
  // ----------------------------------------------------------

  health -=
    fatigueProbability * 0.10;


  // ----------------------------------------------------------
  // ENGINE TEMPERATURE
  // ----------------------------------------------------------

  if (temperature > 105) {

    health -= 20;

  } else if (temperature > 100) {

    health -= 10;

  } else if (temperature > 95) {

    health -= 5;

  }


  return round(
    clamp(health)
  );
}


// ============================================================
// OVERALL RISK SCORE
// ============================================================
//
// Risk score is intentionally weighted:
//
// Maintenance       30%
// Driver/Fatigue    25%
// Vehicle health    25%
// Anomalies         20%
// ============================================================

export function calculateRiskScore(
  healthScore: number,
  driverRisk: number,
  maintenanceRisk: number,
  anomalyRisk: number
): number {

  const healthRisk =
    100 - healthScore;

  const score =
    (
      healthRisk * 0.25
    ) +
    (
      driverRisk * 0.25
    ) +
    (
      maintenanceRisk * 0.30
    ) +
    (
      anomalyRisk * 0.20
    );

  return round(
    clamp(score)
  );
}


// ============================================================
// RECOMMENDATIONS
// ============================================================

export function generateRecommendations(
  input: VehicleIntelligenceInput,
  result: {
    riskScore: number;
    riskLevel: RiskLevel;
    driverRisk: number;
    maintenanceRisk: number;
    anomalyRisk: number;
    healthScore: number;
  }
): AIRecommendationResult[] {

  const recommendations:
    AIRecommendationResult[] = [];


  // ----------------------------------------------------------
  // DRIVER FATIGUE
  // ----------------------------------------------------------

  if (
    (input.fatigueProbability ?? 0) >= 70
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-fatigue-critical`,

      priority:
        "Critical",

      category:
        "Driver",

      title:
        "High driver fatigue detected",

      description:
        "Driver fatigue probability is significantly above the recommended operating threshold.",

      recommendation:
        "Schedule a driver break or replacement and review recent driving-hour patterns.",

    });

  } else if (
    (input.fatigueProbability ?? 0) >= 50
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-fatigue-warning`,

      priority:
        "High",

      category:
        "Driver",

      title:
        "Elevated fatigue probability",

      description:
        "Fatigue indicators are above the normal operating range.",

      recommendation:
        "Monitor driver workload and schedule an appropriate rest period.",

    });

  }


  // ----------------------------------------------------------
  // MAINTENANCE
  // ----------------------------------------------------------

  if (
    (input.maintenanceProbability ?? 0) >= 80
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-maintenance-critical`,

      priority:
        "Critical",

      category:
        "Maintenance",

      title:
        "Preventive maintenance required",

      description:
        "The predicted maintenance risk is significantly elevated.",

      recommendation:
        "Schedule an immediate vehicle inspection before continued operation.",

    });

  } else if (
    (input.maintenanceProbability ?? 0) >= 60
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-maintenance-high`,

      priority:
        "High",

      category:
        "Maintenance",

      title:
        "Maintenance inspection recommended",

      description:
        "AI indicators suggest an increased probability of component failure.",

      recommendation:
        "Schedule preventive maintenance within the next 7 days.",

    });

  }


  // ----------------------------------------------------------
  // ANOMALIES
  // ----------------------------------------------------------

  if (
    (input.anomalyCount ?? 0) >= 4
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-anomaly-critical`,

      priority:
        "Critical",

      category:
        "Safety",

      title:
        "Multiple vehicle anomalies detected",

      description:
        "Several abnormal vehicle signals have been detected.",

      recommendation:
        "Perform a complete diagnostic inspection before returning the vehicle to normal operation.",

    });

  } else if (
    (input.anomalyCount ?? 0) >= 2
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-anomaly-warning`,

      priority:
        "High",

      category:
        "Safety",

      title:
        "Repeated anomalies detected",

      description:
        "The vehicle has generated multiple abnormal operating signals.",

      recommendation:
        "Review recent telemetry and inspect the affected vehicle systems.",

    });

  }


  // ----------------------------------------------------------
  // ENGINE TEMPERATURE
  // ----------------------------------------------------------

  if (
    (input.engineTemperature ?? 0) >= 105
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-temperature-critical`,

      priority:
        "Critical",

      category:
        "Maintenance",

      title:
        "Engine temperature anomaly",

      description:
        "Engine temperature is significantly above the normal operating range.",

      recommendation:
        "Stop the vehicle when safe and inspect the cooling system immediately.",

    });

  }


  // ----------------------------------------------------------
  // LOW HEALTH
  // ----------------------------------------------------------

  if (
    result.healthScore < 40
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-health-critical`,

      priority:
        "Critical",

      category:
        "Safety",

      title:
        "Vehicle health is critically low",

      description:
        "Combined AI indicators show significant deterioration in vehicle health.",

      recommendation:
        "Remove the vehicle from normal operation until a diagnostic inspection is completed.",

    });

  } else if (
    result.healthScore < 60
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-health-warning`,

      priority:
        "High",

      category:
        "Maintenance",

      title:
        "Vehicle health requires attention",

      description:
        "The overall vehicle health score is below the preferred operating range.",

      recommendation:
        "Review recent maintenance and telemetry history.",

    });

  }


  // ----------------------------------------------------------
  // DEFAULT RECOMMENDATION
  // ----------------------------------------------------------

  if (
    recommendations.length === 0
  ) {

    recommendations.push({

      id:
        `${input.vehicleId}-healthy`,

      priority:
        "Low",

      category:
        "Performance",

      title:
        "Vehicle operating normally",

      description:
        "No significant AI risk indicators were detected.",

      recommendation:
        "Continue routine monitoring and scheduled maintenance.",

    });

  }


  return recommendations;
}


// ============================================================
// SUMMARY GENERATOR
// ============================================================

function generateSummary(
  result: {
    riskScore: number;
    riskLevel: RiskLevel;
    healthScore: number;
    driverRisk: number;
    maintenanceRisk: number;
    anomalyRisk: number;
  }
): string {

  if (
    result.riskLevel ===
    "Critical"
  ) {

    return (
      "AI analysis indicates a critical vehicle risk level. " +
      "Immediate attention is recommended based on combined " +
      "vehicle health, driver, maintenance and anomaly signals."
    );

  }

  if (
    result.riskLevel ===
    "High"
  ) {

    return (
      "AI analysis indicates elevated vehicle risk. " +
      "Preventive intervention is recommended before " +
      "current indicators develop into a larger operational issue."
    );

  }

  if (
    result.riskLevel ===
    "Medium"
  ) {

    return (
      "AI analysis indicates moderate vehicle risk. " +
      "The vehicle should remain under increased monitoring."
    );

  }

  return (
    "AI analysis indicates low vehicle risk. " +
    "The vehicle appears to be operating within normal parameters."
  );
}


// ============================================================
// MAIN ANALYSIS FUNCTION
// ============================================================

export function analyzeVehicle(
  input: VehicleIntelligenceInput
): VehicleIntelligenceResult {

  const healthScore =
    calculateHealthScore(
      input
    );


  const driverRisk =
    calculateDriverRisk(
      input.fatigueProbability ?? 0,
      input.harshBrakingEvents ?? 0,
      input.harshAccelerationEvents ?? 0
    );


  const maintenanceRisk =
    calculateMaintenanceRisk(
      input.maintenanceProbability ?? 0,
      input.serviceDueDays ?? 999
    );


  const anomalyRisk =
    calculateAnomalyRisk(
      input.anomalyCount ?? 0
    );


  const riskScore =
    calculateRiskScore(
      healthScore,
      driverRisk,
      maintenanceRisk,
      anomalyRisk
    );


  const riskLevel =
    getRiskLevel(
      riskScore
    );


  const overallStatus =
    getOverallStatus(
      riskScore
    );


  const recommendations =
    generateRecommendations(
      input,
      {
        riskScore,
        riskLevel,
        driverRisk,
        maintenanceRisk,
        anomalyRisk,
        healthScore,
      }
    );


  const confidence =
    round(
      clamp(
        70 +
        Math.min(
          recommendations.length * 4,
          20
        )
      )
    );


  const resultWithoutSummary = {

    riskScore,

    riskLevel,

    healthScore,

    driverRisk,

    maintenanceRisk,

    anomalyRisk,

  };


  return {

    vehicleId:
      input.vehicleId,

    registration:
      input.registration,

    vehicleName:
      `${input.make} ${input.model}`,

    riskScore,

    riskLevel,

    healthScore,

    fatigueProbability:
      clamp(
        input.fatigueProbability ?? 0
      ),

    maintenanceProbability:
      clamp(
        input.maintenanceProbability ?? 0
      ),

    anomalyCount:
      input.anomalyCount ?? 0,

    anomalyRisk,

    driverRisk,

    maintenanceRisk,

    overallStatus,

    confidence,

    recommendations,

    summary:
      generateSummary(
        resultWithoutSummary
      ),

  };
}


// ============================================================
// FLEET ANALYSIS
// ============================================================

export function analyzeFleet(
  vehicles: VehicleIntelligenceInput[]
): VehicleIntelligenceResult[] {

  return vehicles.map(
    vehicle =>
      analyzeVehicle(
        vehicle
      )
  );

}


// ============================================================
// FLEET SUMMARY
// ============================================================

export interface FleetIntelligenceSummary {

  totalVehicles: number;

  criticalVehicles: number;

  highRiskVehicles: number;

  mediumRiskVehicles: number;

  lowRiskVehicles: number;

  averageRiskScore: number;

  averageHealthScore: number;

  averageFatigueProbability: number;

  averageMaintenanceProbability: number;

  totalAnomalies: number;

}


export function analyzeFleetSummary(
  results: VehicleIntelligenceResult[]
): FleetIntelligenceSummary {

  if (
    results.length === 0
  ) {

    return {

      totalVehicles: 0,

      criticalVehicles: 0,

      highRiskVehicles: 0,

      mediumRiskVehicles: 0,

      lowRiskVehicles: 0,

      averageRiskScore: 0,

      averageHealthScore: 0,

      averageFatigueProbability: 0,

      averageMaintenanceProbability: 0,

      totalAnomalies: 0,

    };

  }


  const total =
    results.length;


  const sum = (
    values: number[]
  ) =>
    values.reduce(
      (
        accumulator,
        value
      ) =>
        accumulator + value,
      0
    );


  return {

    totalVehicles:
      total,

    criticalVehicles:
      results.filter(
        result =>
          result.riskLevel ===
          "Critical"
      ).length,

    highRiskVehicles:
      results.filter(
        result =>
          result.riskLevel ===
          "High"
      ).length,

    mediumRiskVehicles:
      results.filter(
        result =>
          result.riskLevel ===
          "Medium"
      ).length,

    lowRiskVehicles:
      results.filter(
        result =>
          result.riskLevel ===
          "Low"
      ).length,

    averageRiskScore:
      round(
        sum(
          results.map(
            result =>
              result.riskScore
          )
        ) / total
      ),

    averageHealthScore:
      round(
        sum(
          results.map(
            result =>
              result.healthScore
          )
        ) / total
      ),

    averageFatigueProbability:
      round(
        sum(
          results.map(
            result =>
              result.fatigueProbability
          )
        ) / total
      ),

    averageMaintenanceProbability:
      round(
        sum(
          results.map(
            result =>
              result.maintenanceProbability
          )
        ) / total
      ),

    totalAnomalies:
      sum(
        results.map(
          result =>
            result.anomalyCount
        )
      ),

  };

}