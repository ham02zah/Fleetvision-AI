export type RiskLevel =
  | "Critical"
  | "High"
  | "Medium"
  | "Low";

export type AIRecommendationPriority =
  | "Critical"
  | "High"
  | "Medium"
  | "Low";


export interface AIRiskVehicle {
  id: string;

  registration: string;

  make: string;

  model: string;

  riskScore: number;

  riskLevel: RiskLevel;

  healthScore: number;

  fatigueProbability: number;

  anomalyCount: number;

  maintenanceProbability: number;
}


export interface DriverRisk {
  id: string;

  driverName: string;

  vehicleRegistration: string;

  fatigueProbability: number;

  riskScore: number;

  drivingHours: number;

  harshBrakingEvents: number;

  status:
    | "Normal"
    | "Warning"
    | "Critical";
}


export interface MaintenancePrediction {
  id: string;

  vehicleRegistration: string;

  component: string;

  failureProbability: number;

  estimatedDays: number;

  severity: RiskLevel;

  recommendation: string;
}


export interface VehicleAnomaly {
  id: string;

  vehicleRegistration: string;

  component: string;

  anomalyType: string;

  severity: RiskLevel;

  detectedAt: string;

  description: string;

  status:
    | "Detected"
    | "Investigating"
    | "Resolved";
}


export interface AIRecommendation {
  id: string;

  vehicleRegistration: string;

  priority: AIRecommendationPriority;

  title: string;

  description: string;

  recommendation: string;

  category:
    | "Safety"
    | "Maintenance"
    | "Performance"
    | "Driver";
}


/* ============================================================
   AI ANALYSIS
   ============================================================ */

export interface AIAnalysis {
  vehicleId?: string;

  registration?: string;

  riskScore: number;

  riskLevel: RiskLevel;

  healthScore: number;

  fatigueProbability: number;

  maintenanceProbability: number;

  anomalyCount: number;

  summary: string;

  recommendations: AIRecommendation[];

  driverRisk?: DriverRisk;

  maintenancePredictions?: MaintenancePrediction[];

  anomalies?: VehicleAnomaly[];

  analyzedAt?: string;
}
