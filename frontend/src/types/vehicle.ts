export interface Vehicle {
  id: string;

  fleet_id: string;

  make: string;

  model: string;

  year: number;

  registration_number: string;

  vin: string;

  fuel_type: string;

  color?: string | null;

  is_active: boolean;

  created_at?: string;

  updated_at?: string;

  [key: string]: unknown;
}


// ============================================================
// CREATE VEHICLE
// ============================================================

export interface VehicleCreate {
  fleet_id: string;

  make: string;

  model: string;

  year: number;

  registration_number: string;

  vin: string;

  fuel_type: string;

  color?: string | null;
}


// ============================================================
// UPDATE VEHICLE
// ============================================================

export interface VehicleUpdate {
  make?: string | null;

  model?: string | null;

  year?: number | null;

  registration_number?: string | null;

  vin?: string | null;

  fuel_type?: string | null;

  color?: string | null;

  is_active?: boolean | null;
}


// ============================================================
// LIST RESPONSE
// ============================================================

export interface VehicleListResponse {
  total: number;

  skip: number;

  limit: number;

  vehicles: Vehicle[];
}