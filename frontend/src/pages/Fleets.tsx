import {
  useEffect,
  useState,
} from "react";

import PageHeader from "../components/common/PageHeader";

import {
  fleetService,
} from "../services/fleetService";

import type {
  Fleet,
  FleetCreate,
  FleetUpdate,
} from "../types/fleet";

import "../components/fleet/fleet.css";


const emptyForm: FleetCreate = {
  name: "",
  description: "",
  company_name: "",
  contact_email: "",
  contact_phone: "",
  address: "",
  country: "",
  city: "",
  timezone: "",
};


function Fleets() {

  const [fleets, setFleets] =
    useState<Fleet[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState<string | null>(null);

  const [showForm, setShowForm] =
    useState(false);

  const [editingFleet, setEditingFleet] =
    useState<Fleet | null>(null);

  const [form, setForm] =
    useState<FleetCreate>(emptyForm);

  const [saving, setSaving] =
    useState(false);


  // ============================================================
  // LOAD FLEETS
  // ============================================================

  const loadFleets =
    async () => {

      try {

        setLoading(true);

        setError(null);

        const data =
          await fleetService.getFleets();

        setFleets(data);

      } catch (err) {

        console.error(
          "Failed to load fleets:",
          err
        );

        setError(
          "Unable to load fleet data."
        );

      } finally {

        setLoading(false);

      }
    };


  // ============================================================
  // INITIAL LOAD
  // ============================================================

  useEffect(() => {

    loadFleets();

  }, []);


  // ============================================================
  // FORM CHANGE
  // ============================================================

  const handleChange =
    (
      event: React.ChangeEvent<
        HTMLInputElement | HTMLTextAreaElement
      >
    ) => {

      const {
        name,
        value,
      } = event.target;

      setForm(
        previous => ({
          ...previous,

          [name]: value,
        })
      );
    };


  // ============================================================
  // OPEN CREATE FORM
  // ============================================================

  const openCreateForm =
    () => {

      setEditingFleet(null);

      setForm({
        ...emptyForm,
      });

      setShowForm(true);
    };


  // ============================================================
  // OPEN EDIT FORM
  // ============================================================

  const openEditForm =
    (fleet: Fleet) => {

      setEditingFleet(fleet);

      setForm({
        name:
          fleet.name || "",

        description:
          fleet.description || "",

        company_name:
          fleet.company_name || "",

        contact_email:
          fleet.contact_email || "",

        contact_phone:
          fleet.contact_phone || "",

        address:
          fleet.address || "",

        country:
          fleet.country || "",

        city:
          fleet.city || "",

        timezone:
          fleet.timezone || "",
      });

      setShowForm(true);
    };


  // ============================================================
  // CLOSE FORM
  // ============================================================

  const closeForm =
    () => {

      if (saving) {
        return;
      }

      setShowForm(false);

      setEditingFleet(null);

      setForm({
        ...emptyForm,
      });
    };


  // ============================================================
  // SUBMIT FORM
  // ============================================================

  const handleSubmit =
    async (
      event: React.FormEvent
    ) => {

      event.preventDefault();

      try {

        setSaving(true);

        setError(null);


        // ------------------------------------------------------
        // UPDATE
        // ------------------------------------------------------

        if (editingFleet) {

          const updateData: FleetUpdate = {
            name: form.name,
            description:
              form.description || null,
            company_name:
              form.company_name,
            contact_email:
              form.contact_email || null,
            contact_phone:
              form.contact_phone || null,
            address:
              form.address || null,
            country:
              form.country,
            city:
              form.city,
            timezone:
              form.timezone,
          };

          await fleetService.updateFleet(
            editingFleet.id,
            updateData
          );

        }

        // ------------------------------------------------------
        // CREATE
        // ------------------------------------------------------

        else {

          await fleetService.createFleet(
            form
          );

        }


        // ------------------------------------------------------
        // REFRESH
        // ------------------------------------------------------

        await loadFleets();

        closeForm();

      } catch (err) {

        console.error(
          "Failed to save fleet:",
          err
        );

        setError(
          "Unable to save fleet. Please check the form and try again."
        );

      } finally {

        setSaving(false);

      }
    };


  // ============================================================
  // DELETE / DEACTIVATE FLEET
  // ============================================================

  const handleDelete =
    async (
      fleet: Fleet
    ) => {

      const confirmed =
        window.confirm(
          `Are you sure you want to delete "${fleet.name}"?`
        );

      if (!confirmed) {
        return;
      }

      try {

        setError(null);

        await fleetService.deleteFleet(
          fleet.id
        );

        await loadFleets();

      } catch (err) {

        console.error(
          "Failed to delete fleet:",
          err
        );

        setError(
          "Unable to delete fleet."
        );
      }
    };


  // ============================================================
  // RENDER
  // ============================================================

  return (
    <div className="fleets-page">

      <PageHeader
        title="Fleets"
        description="Manage fleet groups and organizations."
      />


      {/* ======================================================
          HEADER ACTIONS
      ====================================================== */}

      <div className="fleet-toolbar">

        <div>

          <h2>
            Fleet Management
          </h2>

          <p>
            {fleets.length} fleet
            {fleets.length !== 1
              ? "s"
              : ""}
          </p>

        </div>


        <button
          className="primary-button"
          onClick={openCreateForm}
        >
          + Add Fleet
        </button>

      </div>


      {/* ======================================================
          ERROR
      ====================================================== */}

      {error && (

        <div className="fleet-error">

          {error}

        </div>

      )}


      {/* ======================================================
          LOADING
      ====================================================== */}

      {loading && (

        <div className="fleet-state">

          <p>
            Loading fleets...
          </p>

        </div>

      )}


      {/* ======================================================
          EMPTY STATE
      ====================================================== */}

      {!loading &&
        fleets.length === 0 && (

          <div className="fleet-state">

            <h3>
              No fleets found
            </h3>

            <p>
              Create your first fleet to get started.
            </p>

            <button
              className="primary-button"
              onClick={openCreateForm}
            >
              Add Fleet
            </button>

          </div>

        )}


      {/* ======================================================
          FLEET GRID
      ====================================================== */}

      {!loading &&
        fleets.length > 0 && (

          <div className="fleet-grid">

            {fleets.map(
              fleet => (

                <div
                  className="fleet-card"
                  key={fleet.id}
                >

                  <div className="fleet-card-header">

                    <div>

                      <h3>
                        {fleet.name}
                      </h3>

                      <span
                        className={
                          fleet.is_active
                            ? "fleet-status active"
                            : "fleet-status inactive"
                        }
                      >
                        {fleet.is_active
                          ? "Active"
                          : "Inactive"}
                      </span>

                    </div>

                  </div>


                  <div className="fleet-card-body">

                    <div className="fleet-info">

                      <span>
                        Company
                      </span>

                      <strong>
                        {fleet.company_name}
                      </strong>

                    </div>


                    <div className="fleet-info">

                      <span>
                        Location
                      </span>

                      <strong>
                        {fleet.city},{" "}
                        {fleet.country}
                      </strong>

                    </div>


                    <div className="fleet-info">

                      <span>
                        Timezone
                      </span>

                      <strong>
                        {fleet.timezone}
                      </strong>

                    </div>


                    {fleet.contact_email && (

                      <div className="fleet-info">

                        <span>
                          Email
                        </span>

                        <strong>
                          {fleet.contact_email}
                        </strong>

                      </div>

                    )}


                    {fleet.description && (

                      <div className="fleet-description">

                        {fleet.description}

                      </div>

                    )}

                  </div>


                  <div className="fleet-card-actions">

                    <button
                      className="secondary-button"
                      onClick={() =>
                        openEditForm(fleet)
                      }
                    >
                      Edit
                    </button>

                    <button
                      className="danger-button"
                      onClick={() =>
                        handleDelete(fleet)
                      }
                    >
                      Delete
                    </button>

                  </div>

                </div>

              )
            )}

          </div>

        )}


      {/* ======================================================
          CREATE / EDIT MODAL
      ====================================================== */}

      {showForm && (

        <div
          className="fleet-modal-overlay"
          onClick={closeForm}
        >

          <div
            className="fleet-modal"
            onClick={event =>
              event.stopPropagation()
            }
          >

            <div className="fleet-modal-header">

              <div>

                <h2>
                  {editingFleet
                    ? "Edit Fleet"
                    : "Add Fleet"}
                </h2>

                <p>
                  {editingFleet
                    ? "Update fleet information."
                    : "Create a new fleet."}
                </p>

              </div>

              <button
                className="modal-close"
                onClick={closeForm}
                disabled={saving}
              >
                ×
              </button>

            </div>


            <form
              onSubmit={handleSubmit}
              className="fleet-form"
            >

              <div className="form-grid">

                {/* NAME */}

                <div className="form-group">

                  <label>
                    Fleet Name *
                  </label>

                  <input
                    name="name"
                    value={form.name}
                    onChange={handleChange}
                    placeholder="FleetVision Demo"
                    required
                    minLength={2}
                    maxLength={120}
                  />

                </div>


                {/* COMPANY */}

                <div className="form-group">

                  <label>
                    Company Name *
                  </label>

                  <input
                    name="company_name"
                    value={
                      form.company_name
                    }
                    onChange={handleChange}
                    placeholder="FleetVision"
                    required
                    minLength={2}
                    maxLength={150}
                  />

                </div>


                {/* EMAIL */}

                <div className="form-group">

                  <label>
                    Contact Email
                  </label>

                  <input
                    type="email"
                    name="contact_email"
                    value={
                      form.contact_email || ""
                    }
                    onChange={handleChange}
                    placeholder="admin@example.com"
                  />

                </div>


                {/* PHONE */}

                <div className="form-group">

                  <label>
                    Contact Phone
                  </label>

                  <input
                    name="contact_phone"
                    value={
                      form.contact_phone || ""
                    }
                    onChange={handleChange}
                    placeholder="+92..."
                  />

                </div>


                {/* COUNTRY */}

                <div className="form-group">

                  <label>
                    Country *
                  </label>

                  <input
                    name="country"
                    value={form.country}
                    onChange={handleChange}
                    placeholder="Pakistan"
                    required
                  />

                </div>


                {/* CITY */}

                <div className="form-group">

                  <label>
                    City *
                  </label>

                  <input
                    name="city"
                    value={form.city}
                    onChange={handleChange}
                    placeholder="Islamabad"
                    required
                  />

                </div>


                {/* TIMEZONE */}

                <div className="form-group">

                  <label>
                    Timezone *
                  </label>

                  <input
                    name="timezone"
                    value={form.timezone}
                    onChange={handleChange}
                    placeholder="Asia/Karachi"
                    required
                  />

                </div>


                {/* ADDRESS */}

                <div className="form-group">

                  <label>
                    Address
                  </label>

                  <input
                    name="address"
                    value={
                      form.address || ""
                    }
                    onChange={handleChange}
                    placeholder="Islamabad"
                  />

                </div>


                {/* DESCRIPTION */}

                <div className="form-group full-width">

                  <label>
                    Description
                  </label>

                  <textarea
                    name="description"
                    value={
                      form.description || ""
                    }
                    onChange={handleChange}
                    placeholder="Main fleet"
                    rows={4}
                    maxLength={500}
                  />

                </div>

              </div>


              {/* FORM ACTIONS */}

              <div className="fleet-form-actions">

                <button
                  type="button"
                  className="secondary-button"
                  onClick={closeForm}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="primary-button"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingFleet
                      ? "Update Fleet"
                      : "Create Fleet"}
                </button>

              </div>

            </form>

          </div>

        </div>

      )}

    </div>
  );
}

export default Fleets;