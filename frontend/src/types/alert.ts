export interface Alert {
  id: string;
  vehicle_id?: string;

  title: string;
  description?: string;

  alert_type?: string;
  severity?: string;
  status?: string;

  is_resolved?: boolean;

  created_at?: string;
  updated_at?: string;

  [key: string]: unknown;
}

export interface AlertListResponse {
  items?: Alert[];
  total?: number;

  [key: string]: unknown;
}