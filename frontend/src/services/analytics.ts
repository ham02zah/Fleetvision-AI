import api from "./api";

export const getAnalyticsSummary = async () => {
  const response = await api.get("/analytics/summary");
  return response.data;
};

export const getRiskDistribution = async () => {
  const response = await api.get("/analytics/risk-distribution");
  return response.data;
};

export const getVehicleHealth = async () => {
  const response = await api.get("/analytics/vehicle-health");
  return response.data;
};