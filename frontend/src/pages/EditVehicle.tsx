import {
  useEffect,
  useState,
} from "react";

import {
  useNavigate,
  useParams,
} from "react-router-dom";

import type {
  ChangeEvent,
  FormEvent,
} from "react";

import PageHeader from "../components/common/PageHeader";

import {
  vehicleService,
} from "../services/vehicleService";

import type {
  VehicleUpdate,
} from "../types/vehicle";


function EditVehicle() {

  const {
    id,
  } = useParams();

  const navigate =
    useNavigate();


  const [form, setForm] =
    useState<VehicleUpdate>({});

  const [loading, setLoading] =
    useState(true);

  const [saving, setSaving] =
    useState(false);

  const [error, setError] =
    useState<string | null>(null);


  // ============================================================
  // LOAD VEHICLE
  // ============================================================

  useEffect(() => {

    if (!id) return;

    const load =
      async () => {

        try {

          const vehicle =
            await vehicleService.getVehicle(
              id
            );

          setForm({
            make: vehicle.make,
            model: vehicle.model,
            year: vehicle.year,
            registration_number:
              vehicle.registration_number,
            vin: vehicle.vin,
            fuel_type:
              vehicle.fuel_type,
            color:
              vehicle.color,
            is_active:
              vehicle.is_active,
          });

        } catch (err) {

          console.error(err);

          setError(
            "Unable to load vehicle."
          );

        } finally {

          setLoading(false);

        }

      };

    load();

  }, [id]);


  // ============================================================
  // INPUT
  // ============================================================

  const handleChange =
    (
      event:
        ChangeEvent<HTMLInputElement>
    ) => {

      const {
        name,
        value,
      } = event.target;

      setForm(
        previous => ({
          ...previous,

          [name]:
            name === "year"
              ? Number(value)
              : value,
        })
      );

    };


  // ============================================================
  // ACTIVE STATUS
  // ============================================================

  const handleActiveChange =
    (
      event:
        ChangeEvent<HTMLInputElement>
    ) => {

      setForm(
        previous => ({
          ...previous,

          is_active:
            event.target.checked,
        })
      );

    };


  // ============================================================
  // SAVE
  // ============================================================

  const handleSubmit =
    async (
      event:
        FormEvent
    ) => {

      event.preventDefault();

      if (!id) return;

      try {

        setSaving(true);

        await vehicleService.updateVehicle(
          id,
          form
        );

        alert(
          "Vehicle updated successfully."
        );

        navigate(
          `/vehicles/${id}`
        );

      } catch (err) {

        console.error(err);

        alert(
          "Failed to update vehicle."
        );

      } finally {

        setSaving(false);

      }

    };


  if (loading) {

    return (
      <div>
        <p>
          Loading vehicle...
        </p>
      </div>
    );

  }


  if (error) {

    return (
      <div>
        <p>
          {error}
        </p>
      </div>
    );

  }


  return (

    <div>

      <PageHeader
        title="Edit Vehicle"
        description="Update vehicle information."
      />


      <div
        className="placeholder-card"
      >

        <form
          onSubmit={
            handleSubmit
          }
        >

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(2, 1fr)",
              gap: "16px",
              marginTop: "20px",
            }}
          >

            <input
              name="make"
              placeholder="Make"
              value={
                form.make ?? ""
              }
              onChange={
                handleChange
              }
              required
            />


            <input
              name="model"
              placeholder="Model"
              value={
                form.model ?? ""
              }
              onChange={
                handleChange
              }
              required
            />


            <input
              name="year"
              type="number"
              min="1980"
              max="2100"
              value={
                form.year ?? ""
              }
              onChange={
                handleChange
              }
              required
            />


            <input
              name="registration_number"
              placeholder="Registration Number"
              value={
                form.registration_number ??
                ""
              }
              onChange={
                handleChange
              }
              required
            />


            <input
              name="vin"
              placeholder="VIN"
              value={
                form.vin ?? ""
              }
              onChange={
                handleChange
              }
              minLength={17}
              maxLength={17}
              required
            />


            <input
              name="fuel_type"
              placeholder="Fuel Type"
              value={
                form.fuel_type ?? ""
              }
              onChange={
                handleChange
              }
              required
            />


            <input
              name="color"
              placeholder="Color"
              value={
                form.color ?? ""
              }
              onChange={
                handleChange
              }
            />


            <label
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >

              <input
                type="checkbox"
                checked={
                  form.is_active ??
                  false
                }
                onChange={
                  handleActiveChange
                }
              />

              Active Vehicle

            </label>

          </div>


          <div
            style={{
              marginTop: "24px",
              display: "flex",
              gap: "12px",
            }}
          >

            <button
              type="submit"
              disabled={saving}
            >

              {
                saving
                  ? "Saving..."
                  : "Save Changes"
              }

            </button>


            <button
              type="button"
              onClick={() =>
                navigate(
                  `/vehicles/${id}`
                )
              }
            >

              Cancel

            </button>

          </div>

        </form>

      </div>

    </div>

  );

}

export default EditVehicle;