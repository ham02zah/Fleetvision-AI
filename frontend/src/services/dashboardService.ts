import api from "./api";

import type {
  DashboardOverview,
} from "../types/dashboard";

export const dashboardService = {

  async getOverview(): Promise<DashboardOverview> {

    const response =
      await api.get<DashboardOverview>(
        "/dashboard/overview"
      );

    return response.data;
  },

  async getKPI() {

    const response =
      await api.get(
        "/dashboard/kpi"
      );

    return response.data;
  },

  async getAnalytics() {

    const response =
      await api.get(
        "/dashboard/analytics"
      );

    return response.data;
  },

};