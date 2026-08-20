import api from "./api";

import type {
  Fleet,
  FleetCreate,
  FleetUpdate,
} from "../types/fleet";


export const fleetService = {

  // ============================================================
  // GET ALL FLEETS
  // ============================================================

  async getFleets(): Promise<Fleet[]> {

    const response =
      await api.get("/fleets");

    const data = response.data;

    if (Array.isArray(data)) {
      return data;
    }

    if (Array.isArray(data?.fleets)) {
      return data.fleets;
    }

    if (Array.isArray(data?.items)) {
      return data.items;
    }

    return [];
  },


  // ============================================================
  // GET SINGLE FLEET
  // ============================================================

  async getFleet(
    fleetId: string
  ): Promise<Fleet> {

    const response =
      await api.get<Fleet>(
        `/fleets/${fleetId}`
      );

    return response.data;
  },


  // ============================================================
  // CREATE FLEET
  // ============================================================

  async createFleet(
    fleet: FleetCreate
  ): Promise<Fleet> {

    const response =
      await api.post<Fleet>(
        "/fleets",
        fleet
      );

    return response.data;
  },


  // ============================================================
  // UPDATE FLEET
  // ============================================================

  async updateFleet(
    fleetId: string,
    fleet: FleetUpdate
  ): Promise<Fleet> {

    const response =
      await api.put<Fleet>(
        `/fleets/${fleetId}`,
        fleet
      );

    return response.data;
  },


  // ============================================================
  // DELETE FLEET
  // ============================================================

  async deleteFleet(
    fleetId: string
  ): Promise<void> {

    await api.delete(
      `/fleets/${fleetId}`
    );
  },

};