import type {
  FleetAlert,
} from "../types/alert";


// ============================================================
// MOCK FLEET ALERTS
// ============================================================

export const fleetAlerts: FleetAlert[] = [

  {
    id: "AL001",

    vehicleId: "1",

    vehicleRegistration: "FV-001",

    title:
      "Engine Temperature Spike",

    description:
      "Engine temperature exceeded the expected operating range.",

    severity:
      "Critical",

    status:
      "Active",

    category:
      "Maintenance",

    timestamp:
      "12 minutes ago",

    recommendation:
      "Stop the vehicle when safe and perform an engine cooling-system inspection.",

    component:
      "Engine",
  },


  {
    id: "AL002",

    vehicleId: "4",

    vehicleRegistration: "FV-004",

    title:
      "Brake Pressure Drop",

    description:
      "Brake pressure dropped below the learned fleet baseline.",

    severity:
      "High",

    status:
      "Investigating",

    category:
      "Safety",

    timestamp:
      "28 minutes ago",

    recommendation:
      "Inspect brake pads, discs and hydraulic pressure before the next trip.",

    component:
      "Brake System",
  },


  {
    id: "AL003",

    vehicleId: "7",

    vehicleRegistration: "FV-007",

    title:
      "Transmission Vibration",

    description:
      "Unusual vibration pattern detected during acceleration.",

    severity:
      "High",

    status:
      "Active",

    category:
      "Maintenance",

    timestamp:
      "1 hour ago",

    recommendation:
      "Schedule transmission diagnostics within the next 7 days.",

    component:
      "Transmission",
  },


  {
    id: "AL004",

    vehicleId: "2",

    vehicleRegistration: "FV-002",

    title:
      "Fuel Consumption Spike",

    description:
      "Fuel consumption increased above the historical vehicle baseline.",

    severity:
      "Medium",

    status:
      "Investigating",

    category:
      "Performance",

    timestamp:
      "2 hours ago",

    recommendation:
      "Review driving patterns and engine efficiency.",

    component:
      "Fuel System",
  },


  {
    id: "AL005",

    vehicleId: "1",

    vehicleRegistration: "FV-001",

    title:
      "Driver Fatigue Warning",

    description:
      "AI detected an elevated probability of driver fatigue.",

    severity:
      "High",

    status:
      "Active",

    category:
      "Driver",

    timestamp:
      "2 hours ago",

    recommendation:
      "Consider a driver rest break and review current driving hours.",

    component:
      "Driver Monitoring",
  },


  {
    id: "AL006",

    vehicleId: "3",

    vehicleRegistration: "FV-003",

    title:
      "Battery Voltage Variation",

    description:
      "Minor voltage fluctuations were detected.",

    severity:
      "Low",

    status:
      "Active",

    category:
      "Vehicle",

    timestamp:
      "4 hours ago",

    recommendation:
      "Continue monitoring battery voltage.",

    component:
      "Battery",
  },


  {
    id: "AL007",

    vehicleId: "4",

    vehicleRegistration: "FV-004",

    title:
      "Driver Fatigue Risk",

    description:
      "Driver fatigue probability has increased during the current shift.",

    severity:
      "High",

    status:
      "Active",

    category:
      "Driver",

    timestamp:
      "5 hours ago",

    recommendation:
      "Review driving hours and consider a scheduled rest period.",

    component:
      "Driver Monitoring",
  },


  {
    id: "AL008",

    vehicleId: "7",

    vehicleRegistration: "FV-007",

    title:
      "Maintenance Due Soon",

    description:
      "Predictive model indicates elevated transmission maintenance risk.",

    severity:
      "Medium",

    status:
      "Active",

    category:
      "Maintenance",

    timestamp:
      "7 hours ago",

    recommendation:
      "Schedule preventive maintenance within 7 days.",

    component:
      "Transmission",
  },


  {
    id: "AL009",

    vehicleId: "2",

    vehicleRegistration: "FV-002",

    title:
      "Extended Driving Hours",

    description:
      "Driver has exceeded the preferred continuous driving duration.",

    severity:
      "Medium",

    status:
      "Resolved",

    category:
      "Driver",

    timestamp:
      "Yesterday",

    recommendation:
      "Maintain scheduled driver rest periods.",

    component:
      "Driver Monitoring",
  },


  {
    id: "AL010",

    vehicleId: "5",

    vehicleRegistration: "FV-005",

    title:
      "Routine Maintenance Reminder",

    description:
      "Vehicle is approaching its scheduled maintenance interval.",

    severity:
      "Low",

    status:
      "Resolved",

    category:
      "Maintenance",

    timestamp:
      "Yesterday",

    recommendation:
      "Schedule routine maintenance at the next convenient opportunity.",

    component:
      "General Maintenance",
  },

];