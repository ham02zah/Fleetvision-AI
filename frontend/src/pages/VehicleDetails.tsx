import {
  useEffect,
  useState,
} from "react";

import {
  useParams,
  useNavigate,
} from "react-router-dom";

import type {
  Vehicle,
  VehicleUpdate,
} from "../types/vehicle";

import {
  vehicleService,
} from "../services/vehicleService";

export default function VehicleDetails() {

  const { vehicleId } = useParams();

  const navigate = useNavigate();

  const [vehicle, setVehicle] =
    useState<Vehicle | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [saving, setSaving] =
    useState(false);

  const [form, setForm] =
    useState<VehicleUpdate>({});

  useEffect(() => {

    if (!vehicleId) return;

    loadVehicle();

  }, [vehicleId]);

  const loadVehicle =
    async () => {

      try {

        const data =
          await vehicleService.getVehicle(vehicleId!);

        setVehicle(data);

        setForm({
          make: data.make,
          model: data.model,
          year: data.year,
          registration_number:
            data.registration_number,
          fuel_type:
            data.fuel_type,
          color:
            data.color,
          is_active:
            data.is_active,
        });

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    };

  const handleChange =
    (
      e: React.ChangeEvent<HTMLInputElement>
    ) => {

      const {
        name,
        value,
      } = e.target;

      setForm({
        ...form,
        [name]:
          name === "year"
            ? Number(value)
            : value,
      });
    };

  const handleSave =
    async () => {

      if (!vehicleId) return;

      try {

        setSaving(true);

        await vehicleService.updateVehicle(
          vehicleId,
          form
        );

        alert(
          "Vehicle updated successfully"
        );

      } catch {

        alert(
          "Update failed"
        );

      } finally {

        setSaving(false);

      }
    };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (!vehicle) {
    return <p>Vehicle not found</p>;
  }

  return (

    <div className="placeholder-card">

      <h2>
        Vehicle Details
      </h2>

      <div
        style={{
          display: "grid",
          gap: "12px",
          marginTop: "20px",
        }}
      >

        <input
          name="make"
          value={form.make || ""}
          onChange={handleChange}
        />

        <input
          name="model"
          value={form.model || ""}
          onChange={handleChange}
        />

        <input
          name="year"
          type="number"
          value={form.year || ""}
          onChange={handleChange}
        />

        <input
          name="registration_number"
          value={
            form.registration_number || ""
          }
          onChange={handleChange}
        />

        <input
          name="fuel_type"
          value={
            form.fuel_type || ""
          }
          onChange={handleChange}
        />

        <input
          name="color"
          value={
            form.color || ""
          }
          onChange={handleChange}
        />

      </div>

      <div
        style={{
          marginTop: "20px",
          display: "flex",
          gap: "10px",
        }}
      >

        <button
          onClick={handleSave}
        >
          {
            saving
              ? "Saving..."
              : "Save"
          }
        </button>

        <button
          onClick={() =>
            navigate("/vehicles")
          }
        >
          Back
        </button>

      </div>

    </div>
  );
}