export interface AIAnalysis {
  risk_analysis?: {
    risk_level?: string;
    reason?: string;

    [key: string]: unknown;
  };

  maintenance_analysis?: {
    maintenance_level?: string;
    reason?: string;

    [key: string]: unknown;
  };

  prediction?: unknown;

  [key: string]: unknown;
}