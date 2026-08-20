export interface DashboardSummary {
  total_vehicles?: number;
  active_vehicles?: number;
  inactive_vehicles?: number;
  moving_vehicles?: number;
  parked_vehicles?: number;

  total_predictions?: number;
  total_alerts?: number;

  average_health_score?: number;
  average_driver_score?: number;
  average_speed?: number;

  [key: string]: unknown;
}

export interface SpeedTrendPoint {
  timestamp: string;
  speed: number;
}

export interface HealthTrendPoint {
  timestamp: string;
  health_score: number;
}

export interface LeaderboardItem {
  vehicle_id: string;
  driver_score?: number;
  health_score?: number;
  risk_level?: string;
}

export interface RiskyVehicle {
  vehicle_id: string;
  risk_level?: string;
  health_score?: number;
  maintenance_level?: string;
  predicted_speed?: number;
}

export interface DecisionHistoryItem {
  timestamp: string;
  decision?: string;
  risk_level?: string;
  health_score?: number;
}

export interface DashboardOverview {
  summary: DashboardSummary;

  speed_trend: SpeedTrendPoint[];

  health_trend: HealthTrendPoint[];

  leaderboard: LeaderboardItem[];

  risky_vehicles: RiskyVehicle[];

  decision_history: DecisionHistoryItem[];
}
