import api from "./api";

export const analyticsService = {

  async getSummary() {

    const response =
      await api.get(
        "/analytics/summary"
      );

    return response.data;
  },

  async getRiskDistribution() {

    const response =
      await api.get(
        "/analytics/risk-distribution"
      );

    return response.data;
  },

  async getVehicleHealth() {

    const response =
      await api.get(
        "/analytics/vehicle-health"
      );

    return response.data;
  },

};