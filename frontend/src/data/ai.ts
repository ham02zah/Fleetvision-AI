import type {
  AIRiskVehicle,
  DriverRisk,
  MaintenancePrediction,
  VehicleAnomaly,
  AIRecommendation,
} from "../types/ai";


// ============================================================
// VEHICLE AI RISK
// ============================================================

export const aiRiskVehicles: AIRiskVehicle[] = [

  {
    id: "1",
    registration: "FV-001",
    make: "Toyota",
    model: "Hilux",
    riskScore: 82,
    riskLevel: "Critical",
    healthScore: 61,
    fatigueProbability: 74,
    anomalyCount: 4,
    maintenanceProbability: 81,
  },

  {
    id: "2",
    registration: "FV-002",
    make: "Ford",
    model: "Transit",
    riskScore: 67,
    riskLevel: "High",
    healthScore: 72,
    fatigueProbability: 42,
    anomalyCount: 2,
    maintenanceProbability: 69,
  },

  {
    id: "3",
    registration: "FV-003",
    make: "Mercedes",
    model: "Sprinter",
    riskScore: 54,
    riskLevel: "Medium",
    healthScore: 79,
    fatigueProbability: 35,
    anomalyCount: 1,
    maintenanceProbability: 52,
  },

  {
    id: "4",
    registration: "FV-004",
    make: "Isuzu",
    model: "N-Series",
    riskScore: 76,
    riskLevel: "High",
    healthScore: 65,
    fatigueProbability: 61,
    anomalyCount: 3,
    maintenanceProbability: 74,
  },

  {
    id: "5",
    registration: "FV-005",
    make: "Volvo",
    model: "FH",
    riskScore: 31,
    riskLevel: "Low",
    healthScore: 94,
    fatigueProbability: 18,
    anomalyCount: 0,
    maintenanceProbability: 23,
  },

  {
    id: "6",
    registration: "FV-006",
    make: "MAN",
    model: "TGX",
    riskScore: 48,
    riskLevel: "Medium",
    healthScore: 83,
    fatigueProbability: 29,
    anomalyCount: 1,
    maintenanceProbability: 44,
  },

  {
    id: "7",
    registration: "FV-007",
    make: "Scania",
    model: "R-Series",
    riskScore: 72,
    riskLevel: "High",
    healthScore: 69,
    fatigueProbability: 58,
    anomalyCount: 3,
    maintenanceProbability: 71,
  },

  {
    id: "8",
    registration: "FV-008",
    make: "DAF",
    model: "XF",
    riskScore: 26,
    riskLevel: "Low",
    healthScore: 96,
    fatigueProbability: 12,
    anomalyCount: 0,
    maintenanceProbability: 19,
  },

];


// ============================================================
// DRIVER FATIGUE
// ============================================================

export const driverRisks: DriverRisk[] = [

  {
    id: "D001",
    driverName: "Driver 101",
    vehicleRegistration: "FV-001",
    fatigueProbability: 82,
    riskScore: 84,
    drivingHours: 9.4,
    harshBrakingEvents: 7,
    status: "Critical",
  },

  {
    id: "D002",
    driverName: "Driver 102",
    vehicleRegistration: "FV-002",
    fatigueProbability: 64,
    riskScore: 68,
    drivingHours: 8.1,
    harshBrakingEvents: 4,
    status: "Warning",
  },

  {
    id: "D003",
    driverName: "Driver 103",
    vehicleRegistration: "FV-003",
    fatigueProbability: 27,
    riskScore: 31,
    drivingHours: 5.8,
    harshBrakingEvents: 1,
    status: "Normal",
  },

  {
    id: "D004",
    driverName: "Driver 104",
    vehicleRegistration: "FV-004",
    fatigueProbability: 71,
    riskScore: 75,
    drivingHours: 8.9,
    harshBrakingEvents: 6,
    status: "Warning",
  },

  {
    id: "D005",
    driverName: "Driver 105",
    vehicleRegistration: "FV-005",
    fatigueProbability: 14,
    riskScore: 22,
    drivingHours: 4.6,
    harshBrakingEvents: 0,
    status: "Normal",
  },

];


// ============================================================
// PREDICTIVE MAINTENANCE
// ============================================================

export const maintenancePredictions: MaintenancePrediction[] = [

  {
    id: "M001",
    vehicleRegistration: "FV-001",
    component: "Engine",
    failureProbability: 81,
    estimatedDays: 12,
    severity: "Critical",
    recommendation:
      "Schedule engine inspection and diagnostic testing.",
  },

  {
    id: "M002",
    vehicleRegistration: "FV-004",
    component: "Brake System",
    failureProbability: 76,
    estimatedDays: 18,
    severity: "High",
    recommendation:
      "Inspect brake pads, discs and hydraulic pressure.",
  },

  {
    id: "M003",
    vehicleRegistration: "FV-007",
    component: "Transmission",
    failureProbability: 68,
    estimatedDays: 24,
    severity: "High",
    recommendation:
      "Schedule transmission inspection.",
  },

  {
    id: "M004",
    vehicleRegistration: "FV-002",
    component: "Battery",
    failureProbability: 54,
    estimatedDays: 37,
    severity: "Medium",
    recommendation:
      "Monitor battery voltage and charging performance.",
  },

  {
    id: "M005",
    vehicleRegistration: "FV-003",
    component: "Cooling System",
    failureProbability: 42,
    estimatedDays: 46,
    severity: "Medium",
    recommendation:
      "Inspect coolant level and radiator condition.",
  },

];


// ============================================================
// VEHICLE ANOMALIES
// ============================================================

export const vehicleAnomalies: VehicleAnomaly[] = [

  {
    id: "A001",
    vehicleRegistration: "FV-001",
    component: "Engine",
    anomalyType: "Temperature Spike",
    severity: "Critical",
    detectedAt: "12 minutes ago",
    description:
      "Engine temperature exceeded the expected operating range.",
    status: "Detected",
  },

  {
    id: "A002",
    vehicleRegistration: "FV-004",
    component: "Brake System",
    anomalyType: "Pressure Drop",
    severity: "High",
    detectedAt: "28 minutes ago",
    description:
      "Brake pressure dropped below the learned baseline.",
    status: "Investigating",
  },

  {
    id: "A003",
    vehicleRegistration: "FV-007",
    component: "Transmission",
    anomalyType: "Vibration Pattern",
    severity: "High",
    detectedAt: "1 hour ago",
    description:
      "Unusual vibration pattern detected during acceleration.",
    status: "Detected",
  },

  {
    id: "A004",
    vehicleRegistration: "FV-002",
    component: "Fuel System",
    anomalyType: "Consumption Spike",
    severity: "Medium",
    detectedAt: "2 hours ago",
    description:
      "Fuel consumption increased above the historical baseline.",
    status: "Investigating",
  },

  {
    id: "A005",
    vehicleRegistration: "FV-003",
    component: "Battery",
    anomalyType: "Voltage Variation",
    severity: "Low",
    detectedAt: "4 hours ago",
    description:
      "Minor voltage fluctuations detected.",
    status: "Detected",
  },

];


// ============================================================
// AI RECOMMENDATIONS
// ============================================================

export const aiRecommendations: AIRecommendation[] = [

  {
    id: "R001",
    vehicleRegistration: "FV-001",
    priority: "Critical",
    title: "Immediate engine inspection",
    description:
      "Engine temperature and maintenance indicators show elevated failure risk.",
    recommendation:
      "Schedule an inspection within the next 24 hours.",
    category: "Maintenance",
  },

  {
    id: "R002",
    vehicleRegistration: "FV-004",
    priority: "High",
    title: "Brake system inspection",
    description:
      "AI detected abnormal brake pressure behavior.",
    recommendation:
      "Inspect the braking system before the next long-distance trip.",
    category: "Safety",
  },

  {
    id: "R003",
    vehicleRegistration: "FV-007",
    priority: "High",
    title: "Transmission diagnostics",
    description:
      "Vehicle vibration patterns indicate a potential transmission issue.",
    recommendation:
      "Perform transmission diagnostics within 7 days.",
    category: "Maintenance",
  },

  {
    id: "R004",
    vehicleRegistration: "FV-002",
    priority: "Medium",
    title: "Review fuel efficiency",
    description:
      "Fuel consumption is trending above the vehicle baseline.",
    recommendation:
      "Review driving patterns and engine efficiency.",
    category: "Performance",
  },

  {
    id: "R005",
    vehicleRegistration: "FV-001",
    priority: "High",
    title: "Driver fatigue warning",
    description:
      "Fatigue probability has increased significantly.",
    recommendation:
      "Consider a driver rest break and review driving hours.",
    category: "Driver",
  },

];