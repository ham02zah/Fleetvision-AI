import api from "./api";

import type {
  Vehicle,
  VehicleCreate,
  VehicleUpdate,
} from "../types/vehicle";


export const vehicleService = {

  // ============================================================
  // GET VEHICLES
  // ============================================================

  async getVehicles(): Promise<Vehicle[]> {

    const response =
      await api.get("/vehicles");

    const data = response.data;

    if (Array.isArray(data)) {
      return data;
    }

    if (Array.isArray(data?.vehicles)) {
      return data.vehicles;
    }

    if (Array.isArray(data?.items)) {
      return data.items;
    }

    return [];
  },


  // ============================================================
  // GET SINGLE VEHICLE
  // ============================================================

  async getVehicle(
    vehicleId: string
  ): Promise<Vehicle> {

    const response =
      await api.get<Vehicle>(
        `/vehicles/${vehicleId}`
      );

    return response.data;
  },


  // ============================================================
  // CREATE VEHICLE
  // ============================================================

  async createVehicle(
    vehicle: VehicleCreate
  ): Promise<Vehicle> {

    const response =
      await api.post<Vehicle>(
        "/vehicles",
        vehicle
      );

    return response.data;
  },


  // ============================================================
  // UPDATE VEHICLE
  // ============================================================

  async updateVehicle(
    vehicleId: string,
    vehicle: VehicleUpdate
  ): Promise<Vehicle> {

    const response =
      await api.put<Vehicle>(
        `/vehicles/${vehicleId}`,
        vehicle
      );

    return response.data;
  },


  // ============================================================
  // DELETE VEHICLE
  // ============================================================

  async deleteVehicle(
    vehicleId: string
  ): Promise<void> {

    await api.delete(
      `/vehicles/${vehicleId}`
    );
  },

};