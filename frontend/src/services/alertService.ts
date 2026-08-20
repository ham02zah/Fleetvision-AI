import api from "./api";

import type {
  Alert,
} from "../types/alert";

export const alertService = {

  async getAlerts(): Promise<Alert[]> {

    const response =
      await api.get(
        "/alerts"
      );

    const data = response.data;

    if (Array.isArray(data)) {
      return data;
    }

    if (Array.isArray(data?.items)) {
      return data.items;
    }

    if (Array.isArray(data?.alerts)) {
      return data.alerts;
    }

    return [];
  },

  async getActiveAlerts(): Promise<Alert[]> {

    const response =
      await api.get(
        "/alerts/status/active"
      );

    const data = response.data;

    if (Array.isArray(data)) {
      return data;
    }

    if (Array.isArray(data?.items)) {
      return data.items;
    }

    if (Array.isArray(data?.alerts)) {
      return data.alerts;
    }

    return [];
  },

};