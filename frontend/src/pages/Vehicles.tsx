import {
  useEffect,
  useState,
} from "react";

import type {
  ChangeEvent,
  FormEvent,
} from "react";

import {
  Search,
  Plus,
  Eye,
  Pencil,
  Trash2,
  Car,
  Fuel,
  X,
} from "lucide-react";

import {
  useNavigate,
} from "react-router-dom";

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

import "../components/fleet/fleet.css";


function Vehicles() {

  const navigate = useNavigate();

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

  const [search, setSearch] =
    useState("");

  const [statusFilter, setStatusFilter] =
    useState("all");


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
  // FORM CHANGE
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
  // FLEET CHANGE
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
      event: FormEvent
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
  // DELETE
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


  // ============================================================
  // FLEET NAME
  // ============================================================

  const getFleetName =
    (
      fleetId: string
    ) => {

      const fleet =
        fleets.find(
          item => item.id === fleetId
        );

      return fleet?.name || "Unknown Fleet";

    };


  // ============================================================
  // FILTER VEHICLES
  // ============================================================

  const filteredVehicles =
    vehicles.filter(
      vehicle => {

        const query =
          search
            .toLowerCase()
            .trim();

        const matchesSearch =
          !query ||
          vehicle.make
            .toLowerCase()
            .includes(query) ||
          vehicle.model
            .toLowerCase()
            .includes(query) ||
          vehicle.registration_number
            .toLowerCase()
            .includes(query) ||
          vehicle.vin
            .toLowerCase()
            .includes(query) ||
          getFleetName(
            vehicle.fleet_id
          )
            .toLowerCase()
            .includes(query);

        const matchesStatus =
          statusFilter === "all" ||
          (
            statusFilter === "active" &&
            vehicle.is_active
          ) ||
          (
            statusFilter === "inactive" &&
            !vehicle.is_active
          );

        return (
          matchesSearch &&
          matchesStatus
        );

      }
    );


  const activeVehicles =
    vehicles.filter(
      vehicle => vehicle.is_active
    ).length;


  const inactiveVehicles =
    vehicles.length -
    activeVehicles;


  return (

    <div className="vehicles-page">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <PageHeader
        title="Vehicles"
        description="Monitor and manage all vehicles across your fleets."
      />


      {/* ======================================================
          SUMMARY
      ====================================================== */}

      <div className="vehicle-summary-grid">

        <div className="vehicle-summary-card">

          <div className="vehicle-summary-icon">
            <Car size={20} />
          </div>

          <div>
            <span>Total Vehicles</span>
            <strong>
              {vehicles.length}
            </strong>
          </div>

        </div>


        <div className="vehicle-summary-card">

          <div className="vehicle-summary-icon active">
            <Car size={20} />
          </div>

          <div>
            <span>Active Vehicles</span>
            <strong>
              {activeVehicles}
            </strong>
          </div>

        </div>


        <div className="vehicle-summary-card">

          <div className="vehicle-summary-icon inactive">
            <Car size={20} />
          </div>

          <div>
            <span>Inactive Vehicles</span>
            <strong>
              {inactiveVehicles}
            </strong>
          </div>

        </div>


        <div className="vehicle-summary-card">

          <div className="vehicle-summary-icon">
            <Fuel size={20} />
          </div>

          <div>
            <span>Fleets</span>
            <strong>
              {fleets.length}
            </strong>
          </div>

        </div>

      </div>


      {/* ======================================================
          TOOLBAR
      ====================================================== */}

      <div className="vehicles-toolbar">

        <div className="vehicle-search">

          <Search size={18} />

          <input
            type="text"
            placeholder="Search vehicles, registration, VIN or fleet..."
            value={search}
            onChange={
              event =>
                setSearch(
                  event.target.value
                )
            }
          />

          {search && (

            <button
              className="search-clear"
              onClick={() =>
                setSearch("")
              }
            >

              <X size={16} />

            </button>

          )}

        </div>


        <div className="vehicle-toolbar-actions">

          <select
            value={statusFilter}
            onChange={
              event =>
                setStatusFilter(
                  event.target.value
                )
            }
          >

            <option value="all">
              All Status
            </option>

            <option value="active">
              Active
            </option>

            <option value="inactive">
              Inactive
            </option>

          </select>


          <button
            className="vehicle-add-button"
            onClick={() =>
              setShowForm(true)
            }
          >

            <Plus size={18} />

            Add Vehicle

          </button>

        </div>

      </div>


      {/* ======================================================
          CREATE MODAL
      ====================================================== */}

      {showForm && (

        <div className="vehicle-modal-overlay">

          <div className="vehicle-modal">

            <div className="vehicle-modal-header">

              <div>

                <h2>
                  Add Vehicle
                </h2>

                <p>
                  Register a new vehicle in your fleet.
                </p>

              </div>


              <button
                className="modal-close"
                onClick={() =>
                  setShowForm(false)
                }
              >

                <X size={20} />

              </button>

            </div>


            <form
              onSubmit={handleCreate}
            >

              <div className="vehicle-form-grid">

                <div className="form-field">

                  <label>
                    Fleet
                  </label>

                  <select
                    value={form.fleet_id}
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

                </div>


                <div className="form-field">

                  <label>
                    Make
                  </label>

                  <input
                    name="make"
                    placeholder="e.g. Toyota"
                    value={form.make}
                    onChange={
                      handleChange
                    }
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    Model
                  </label>

                  <input
                    name="model"
                    placeholder="e.g. Corolla"
                    value={form.model}
                    onChange={
                      handleChange
                    }
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    Year
                  </label>

                  <input
                    name="year"
                    type="number"
                    min="1980"
                    max="2100"
                    value={form.year}
                    onChange={
                      handleChange
                    }
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    Registration Number
                  </label>

                  <input
                    name="registration_number"
                    placeholder="e.g. ABC-123"
                    value={
                      form.registration_number
                    }
                    onChange={
                      handleChange
                    }
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    VIN
                  </label>

                  <input
                    name="vin"
                    placeholder="17-character VIN"
                    value={form.vin}
                    onChange={
                      handleChange
                    }
                    minLength={17}
                    maxLength={17}
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    Fuel Type
                  </label>

                  <input
                    name="fuel_type"
                    placeholder="e.g. Diesel"
                    value={
                      form.fuel_type
                    }
                    onChange={
                      handleChange
                    }
                    required
                  />

                </div>


                <div className="form-field">

                  <label>
                    Color
                  </label>

                  <input
                    name="color"
                    placeholder="e.g. White"
                    value={
                      form.color ?? ""
                    }
                    onChange={
                      handleChange
                    }
                  />

                </div>

              </div>


              <div className="vehicle-modal-footer">

                <button
                  type="button"
                  className="secondary-button"
                  onClick={() =>
                    setShowForm(false)
                  }
                >
                  Cancel
                </button>


                <button
                  type="submit"
                  className="vehicle-add-button"
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

        </div>

      )}


      {/* ======================================================
          ERROR
      ====================================================== */}

      {error && (

        <div className="vehicle-state error">

          <h3>
            Unable to load vehicles
          </h3>

          <p>
            {error}
          </p>

          <button
            onClick={loadVehicles}
          >
            Try Again
          </button>

        </div>

      )}


      {/* ======================================================
          LOADING
      ====================================================== */}

      {loading && !error && (

        <div className="vehicle-state">

          <Car size={32} />

          <h3>
            Loading vehicles...
          </h3>

          <p>
            Fetching your fleet vehicles.
          </p>

        </div>

      )}


      {/* ======================================================
          VEHICLE TABLE
      ====================================================== */}

      {!loading &&
        !error && (

          <div className="vehicle-table-card">

            <div className="vehicle-table-header">

              <div>

                <h2>
                  Fleet Vehicles
                </h2>

                <p>
                  {filteredVehicles.length}
                  {" "}
                  vehicle
                  {filteredVehicles.length !== 1
                    ? "s"
                    : ""}
                  {" "}
                  displayed
                </p>

              </div>

            </div>


            {filteredVehicles.length === 0 ? (

              <div className="vehicle-empty">

                <Car size={42} />

                <h3>
                  No vehicles found
                </h3>

                <p>
                  Try changing your search or add a new vehicle.
                </p>

              </div>

            ) : (

              <div className="vehicle-table-wrapper">

                <table className="vehicle-table">

                  <thead>

                    <tr>

                      <th>
                        Vehicle
                      </th>

                      <th>
                        Registration
                      </th>

                      <th>
                        Fleet
                      </th>

                      <th>
                        Fuel
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

                    {filteredVehicles.map(
                      vehicle => (

                        <tr
                          key={
                            vehicle.id
                          }
                        >

                          <td>

                            <div className="vehicle-name-cell">

                              <div className="vehicle-avatar">

                                <Car size={19} />

                              </div>

                              <div>

                                <strong>
                                  {vehicle.make}
                                  {" "}
                                  {vehicle.model}
                                </strong>

                                <span>
                                  VIN: {vehicle.vin}
                                </span>

                              </div>

                            </div>

                          </td>


                          <td>

                            <span className="registration-badge">

                              {
                                vehicle.registration_number
                              }

                            </span>

                          </td>


                          <td>

                            <span className="fleet-name">

                              {
                                getFleetName(
                                  vehicle.fleet_id
                                )
                              }

                            </span>

                          </td>


                          <td>
                            {vehicle.fuel_type}
                          </td>


                          <td>
                            {vehicle.year}
                          </td>


                          <td>

                            <span
                              className={
                                vehicle.is_active
                                  ? "status-badge active"
                                  : "status-badge inactive"
                              }
                            >

                              <span className="status-dot" />

                              {vehicle.is_active
                                ? "Active"
                                : "Inactive"}

                            </span>

                          </td>


                          <td>

                            <div className="vehicle-actions">

                              {/* VIEW ONLY */}

                              <button
                                className="icon-button view"
                                title="View vehicle"
                                onClick={() =>
                                  navigate(
                                    `/vehicles/${vehicle.id}`
                                  )
                                }
                              >

                                <Eye size={17} />

                              </button>


                              {/* EDIT */}

                              <button
                                className="icon-button edit"
                                title="Edit vehicle"
                                onClick={() =>
                                  navigate(
                                    `/vehicles/${vehicle.id}/edit`
                                  )
                                }
                              >

                                <Pencil size={17} />

                              </button>


                              {/* DELETE */}

                              <button
                                className="icon-button delete"
                                title="Delete vehicle"
                                onClick={() =>
                                  handleDelete(
                                    vehicle.id
                                  )
                                }
                              >

                                <Trash2 size={17} />

                              </button>

                            </div>

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