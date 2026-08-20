export interface Fleet {
  id: string;

  name: string;

  description?: string | null;

  company_name: string;

  contact_email?: string | null;

  contact_phone?: string | null;

  address?: string | null;

  country: string;

  city: string;

  timezone: string;

  is_active?: boolean;

  created_at?: string;

  updated_at?: string;

  [key: string]: unknown;
}


// ============================================================
// CREATE FLEET
// ============================================================

export interface FleetCreate {
  name: string;

  description?: string | null;

  company_name: string;

  contact_email?: string | null;

  contact_phone?: string | null;

  address?: string | null;

  country: string;

  city: string;

  timezone: string;
}


// ============================================================
// UPDATE FLEET
// ============================================================

export interface FleetUpdate {
  name?: string | null;

  description?: string | null;

  company_name?: string | null;

  contact_email?: string | null;

  contact_phone?: string | null;

  address?: string | null;

  country?: string | null;

  city?: string | null;

  timezone?: string | null;

  is_active?: boolean | null;
}


// ============================================================
// FLEET LIST RESPONSE
// ============================================================

export interface FleetListResponse {
  total: number;

  skip: number;

  limit: number;

  fleets: Fleet[];
}