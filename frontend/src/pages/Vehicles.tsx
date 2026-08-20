import {
  useEffect,
  useState,
} from "react";

import type {
  ChangeEvent,
  FormEvent,
} from "react";

import PageHeader from "../components/common/PageHeader";

import {
  vehicleService,
} from "../services/vehicleService";

import {
  fleetService,
} from "../services/fleetService";

import type {
  Vehicle,
  VehicleCreate,
} from "../types/vehicle";

import type {
  Fleet,
} from "../types/fleet";


function Vehicles() {

  const [vehicles, setVehicles] =
    useState<Vehicle[]>([]);

  const [fleets, setFleets] =
    useState<Fleet[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState<string | null>(null);

  const [showForm, setShowForm] =
    useState(false);

  const [saving, setSaving] =
    useState(false);


  const [form, setForm] =
    useState<VehicleCreate>({
      fleet_id: "",
      make: "",
      model: "",
      year: new Date().getFullYear(),
      registration_number: "",
      vin: "",
      fuel_type: "",
      color: "",
    });


  // ============================================================
  // LOAD VEHICLES
  // ============================================================

  const loadVehicles =
    async () => {

      try {

        setLoading(true);

        setError(null);

        const data =
          await vehicleService.getVehicles();

        setVehicles(data);

      } catch (err) {

        console.error(
          "Failed to load vehicles:",
          err
        );

        setError(
          "Unable to load vehicles."
        );

      } finally {

        setLoading(false);

      }
    };


  // ============================================================
  // LOAD FLEETS
  // ============================================================

  const loadFleets =
    async () => {

      try {

        const data =
          await fleetService.getFleets();

        setFleets(data);

      } catch (err) {

        console.error(
          "Failed to load fleets:",
          err
        );

      }

    };


  // ============================================================
  // INITIAL LOAD
  // ============================================================

  useEffect(() => {

    loadVehicles();

    loadFleets();

  }, []);


  // ============================================================
  // FORM INPUT
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
  // FLEET SELECT
  // ============================================================

  const handleFleetChange =
    (
      event:
        ChangeEvent<HTMLSelectElement>
    ) => {

      setForm(
        previous => ({
          ...previous,

          fleet_id:
            event.target.value,
        })
      );

    };


  // ============================================================
  // CREATE VEHICLE
  // ============================================================

  const handleCreate =
    async (
      event:
        FormEvent
    ) => {

      event.preventDefault();

      if (!form.fleet_id) {

        alert(
          "Please select a fleet."
        );

        return;

      }

      try {

        setSaving(true);

        await vehicleService.createVehicle(
          form
        );

        alert(
          "Vehicle created successfully."
        );

        setShowForm(false);

        setForm({
          fleet_id: "",
          make: "",
          model: "",
          year: new Date().getFullYear(),
          registration_number: "",
          vin: "",
          fuel_type: "",
          color: "",
        });

        await loadVehicles();

      } catch (err) {

        console.error(
          "Failed to create vehicle:",
          err
        );

        alert(
          "Failed to create vehicle."
        );

      } finally {

        setSaving(false);

      }

    };


  // ============================================================
  // DELETE VEHICLE
  // ============================================================

  const handleDelete =
    async (
      vehicleId: string
    ) => {

      const confirmed =
        window.confirm(
          "Are you sure you want to delete this vehicle?"
        );

      if (!confirmed) {
        return;
      }

      try {

        await vehicleService.deleteVehicle(
          vehicleId
        );

        await loadVehicles();

      } catch (err) {

        console.error(
          "Failed to delete vehicle:",
          err
        );

        alert(
          "Failed to delete vehicle."
        );

      }

    };


  return (

    <div>

      <PageHeader
        title="Vehicles"
        description="Monitor and manage fleet vehicles."
      />


      {/* ======================================================
          HEADER ACTIONS
      ====================================================== */}

      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          marginBottom: "20px",
        }}
      >

        <button
          onClick={() =>
            setShowForm(
              previous => !previous
            )
          }
        >

          {showForm
            ? "Cancel"
            : "+ Add Vehicle"}

        </button>

      </div>


      {/* ======================================================
          CREATE FORM
      ====================================================== */}

      {showForm && (

        <div
          className="placeholder-card"
          style={{
            marginBottom: "24px",
          }}
        >

          <h2>
            Add Vehicle
          </h2>


          <form
            onSubmit={handleCreate}
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


              {/* FLEET */}

              <select
                name="fleet_id"
                value={
                  form.fleet_id
                }
                onChange={
                  handleFleetChange
                }
                required
              >

                <option value="">
                  Select Fleet
                </option>

                {fleets.map(
                  fleet => (

                    <option
                      key={fleet.id}
                      value={fleet.id}
                    >

                      {fleet.name}

                    </option>

                  )
                )}

              </select>


              {/* MAKE */}

              <input
                name="make"
                placeholder="Make"
                value={
                  form.make
                }
                onChange={
                  handleChange
                }
                required
              />


              {/* MODEL */}

              <input
                name="model"
                placeholder="Model"
                value={
                  form.model
                }
                onChange={
                  handleChange
                }
                required
              />


              {/* YEAR */}

              <input
                name="year"
                type="number"
                placeholder="Year"
                value={
                  form.year
                }
                onChange={
                  handleChange
                }
                min="1980"
                max="2100"
                required
              />


              {/* REGISTRATION */}

              <input
                name="registration_number"
                placeholder="Registration Number"
                value={
                  form.registration_number
                }
                onChange={
                  handleChange
                }
                required
              />


              {/* VIN */}

              <input
                name="vin"
                placeholder="VIN"
                value={
                  form.vin
                }
                onChange={
                  handleChange
                }
                minLength={17}
                maxLength={17}
                required
              />


              {/* FUEL */}

              <input
                name="fuel_type"
                placeholder="Fuel Type"
                value={
                  form.fuel_type
                }
                onChange={
                  handleChange
                }
                required
              />


              {/* COLOR */}

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

            </div>


            <div
              style={{
                marginTop: "20px",
              }}
            >

              <button
                type="submit"
                disabled={
                  saving ||
                  fleets.length === 0
                }
              >

                {saving
                  ? "Creating..."
                  : "Create Vehicle"}

              </button>

            </div>

          </form>

        </div>

      )}


      {/* ======================================================
          ERROR
      ====================================================== */}

      {error && (

        <div
          className="placeholder-card"
        >

          <p>
            {error}
          </p>

        </div>

      )}


      {/* ======================================================
          LOADING
      ====================================================== */}

      {loading && (

        <div
          className="placeholder-card"
        >

          <p>
            Loading vehicles...
          </p>

        </div>

      )}


      {/* ======================================================
          TABLE
      ====================================================== */}

      {!loading &&
        !error && (

          <div
            className="placeholder-card"
          >

            <h2>
              Fleet Vehicles
            </h2>


            {vehicles.length === 0 ? (

              <p>
                No vehicles found.
              </p>

            ) : (

              <div
                style={{
                  overflowX: "auto",
                  marginTop: "20px",
                }}
              >

                <table
                  style={{
                    width: "100%",
                    borderCollapse:
                      "collapse",
                  }}
                >

                  <thead>

                    <tr>

                      <th>
                        Registration
                      </th>

                      <th>
                        Make
                      </th>

                      <th>
                        Model
                      </th>

                      <th>
                        Year
                      </th>

                      <th>
                        Status
                      </th>

                      <th>
                        Actions
                      </th>

                    </tr>

                  </thead>


                  <tbody>

                    {vehicles.map(
                      vehicle => (

                        <tr
                          key={
                            vehicle.id
                          }
                        >

                          <td>
                            {
                              vehicle.registration_number
                            }
                          </td>

                          <td>
                            {
                              vehicle.make
                            }
                          </td>

                          <td>
                            {
                              vehicle.model
                            }
                          </td>

                          <td>
                            {
                              vehicle.year
                            }
                          </td>

                          <td>
                            {
                              vehicle.is_active
                                ? "Active"
                                : "Inactive"
                            }
                          </td>

                          <td>

                            {/* VIEW */}

                            <button
                              onClick={() =>
                                window.location.href =
                                  `/vehicles/${vehicle.id}`
                              }
                            >
                              View
                            </button>


                            {/* EDIT */}

                            <button
                              style={{
                                marginLeft:
                                  "8px",
                              }}
                              onClick={() =>
                                window.location.href =
                                  `/vehicles/${vehicle.id}/edit`
                              }
                            >
                              Edit
                            </button>


                            {/* DELETE */}

                            <button
                              style={{
                                marginLeft:
                                  "8px",
                              }}
                              onClick={() =>
                                handleDelete(
                                  vehicle.id
                                )
                              }
                            >
                              Delete
                            </button>

                          </td>

                        </tr>

                      )
                    )}

                  </tbody>

                </table>

              </div>

            )}

          </div>

        )}

    </div>

  );
}

export default Vehicles;