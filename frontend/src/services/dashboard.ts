import api from "./api";

export const getDashboardOverview = async () => {
  const response = await api.get("/dashboard/overview");
  return response.data;
};

export const getDashboardKPI = async () => {
  const response = await api.get("/dashboard/kpi");
  return response.data;
};

export const getDashboardAnalytics = async () => {
  const response = await api.get("/dashboard/analytics");
  return response.data;
};