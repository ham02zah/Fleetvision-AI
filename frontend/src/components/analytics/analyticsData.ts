// ============================================================
// FLEETVISION ANALYTICS DEMO DATA
// ============================================================

export interface UtilizationData {
  day: string;
  utilization: number;
}

export interface FuelData {
  month: string;
  consumption: number;
}

export interface VehicleStatusData {
  name: string;
  value: number;
}

export interface MaintenanceData {
  month: string;
  events: number;
}

export interface FleetPerformance {
  fleet: string;
  vehicles: number;
  utilization: number;
  fuelEfficiency: number;
  maintenanceCost: number;
}


// ============================================================
// VEHICLE UTILIZATION
// ============================================================

export const utilizationData: UtilizationData[] = [
  {
    day: "Mon",
    utilization: 72,
  },
  {
    day: "Tue",
    utilization: 76,
  },
  {
    day: "Wed",
    utilization: 81,
  },
  {
    day: "Thu",
    utilization: 78,
  },
  {
    day: "Fri",
    utilization: 84,
  },
  {
    day: "Sat",
    utilization: 69,
  },
  {
    day: "Sun",
    utilization: 61,
  },
];


// ============================================================
// FUEL CONSUMPTION
// ============================================================

export const fuelData: FuelData[] = [
  {
    month: "Jan",
    consumption: 8420,
  },
  {
    month: "Feb",
    consumption: 7980,
  },
  {
    month: "Mar",
    consumption: 9150,
  },
  {
    month: "Apr",
    consumption: 8760,
  },
  {
    month: "May",
    consumption: 9340,
  },
  {
    month: "Jun",
    consumption: 8890,
  },
];


// ============================================================
// VEHICLE STATUS
// ============================================================

export const vehicleStatusData: VehicleStatusData[] = [
  {
    name: "Active",
    value: 42,
  },
  {
    name: "Maintenance",
    value: 4,
  },
  {
    name: "Inactive",
    value: 2,
  },
];


// ============================================================
// MAINTENANCE TREND
// ============================================================

export const maintenanceData: MaintenanceData[] = [
  {
    month: "Jan",
    events: 18,
  },
  {
    month: "Feb",
    events: 15,
  },
  {
    month: "Mar",
    events: 21,
  },
  {
    month: "Apr",
    events: 13,
  },
  {
    month: "May",
    events: 17,
  },
  {
    month: "Jun",
    events: 11,
  },
];


// ============================================================
// FLEET PERFORMANCE
// ============================================================

export const fleetPerformanceData: FleetPerformance[] = [
  {
    fleet: "Main Fleet",
    vehicles: 18,
    utilization: 84,
    fuelEfficiency: 7.8,
    maintenanceCost: 4820,
  },
  {
    fleet: "Delivery Fleet",
    vehicles: 22,
    utilization: 76,
    fuelEfficiency: 8.9,
    maintenanceCost: 5310,
  },
  {
    fleet: "Executive Fleet",
    vehicles: 8,
    utilization: 72,
    fuelEfficiency: 7.2,
    maintenanceCost: 2350,
  },
];