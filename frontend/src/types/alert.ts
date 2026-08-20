// ============================================================
// ALERT TYPES
// ============================================================

export type AlertSeverity =
  | "Critical"
  | "High"
  | "Medium"
  | "Low";

export type AlertStatus =
  | "Active"
  | "Investigating"
  | "Resolved";

export type AlertCategory =
  | "Safety"
  | "Maintenance"
  | "Driver"
  | "Vehicle"
  | "Performance";


// ============================================================
// ALERT
// ============================================================

export interface FleetAlert {

  id: string;

  vehicleId: string;

  vehicleRegistration: string;

  title: string;

  description: string;

  severity: AlertSeverity;

  status: AlertStatus;

  category: AlertCategory;

  timestamp: string;

  recommendation: string;

  component?: string;

}