import api from "./api";

export const getVehicles = async () => {
  const response = await api.get("/vehicles");
  return response.data;
};

export const getVehicle = async (vehicleId: string) => {
  const response = await api.get(`/vehicles/${vehicleId}`);
  return response.data;
};