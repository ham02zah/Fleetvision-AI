import api from "./api";

import type {
  FleetAlert,
} from "../types/alert";


export const alertService = {

  // ============================================================
  // GET ALL ALERTS
  // ============================================================

  async getAlerts(): Promise<FleetAlert[]> {

    const response =
      await api.get<
        FleetAlert[]
      >("/alerts");

    return response.data;
  },


  // ============================================================
  // GET ACTIVE ALERTS
  // ============================================================

  async getActiveAlerts(): Promise<FleetAlert[]> {

    const response =
      await api.get<
        FleetAlert[]
      >("/alerts/active");

    return response.data;
  },


  // ============================================================
  // GET SINGLE ALERT
  // ============================================================

  async getAlert(
    alertId: string
  ): Promise<FleetAlert> {

    const response =
      await api.get<FleetAlert>(
        `/alerts/${alertId}`
      );

    return response.data;
  },


  // ============================================================
  // UPDATE ALERT STATUS
  // ============================================================

  async updateAlertStatus(
    alertId: string,
    status: string
  ): Promise<FleetAlert> {

    const response =
      await api.patch<FleetAlert>(
        `/alerts/${alertId}`,
        {
          status,
        }
      );

    return response.data;
  },

};
