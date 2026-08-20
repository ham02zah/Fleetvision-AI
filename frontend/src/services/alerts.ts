import api from "./api";

export const getAlerts = async () => {
  const response = await api.get("/alerts");
  return response.data;
};

export const getActiveAlerts = async () => {
  const response = await api.get("/alerts/status/active");
  return response.data;
};

export const getAlertStatistics = async () => {
  const response = await api.get("/alerts/statistics");
  return response.data;
};