import {
  useMemo,
  useState,
} from "react";

import {
  AlertTriangle,
  Bell,
  CheckCircle2,
  CircleAlert,
  Search,
  ShieldAlert,
  Wrench,
  X,
} from "lucide-react";

import PageHeader from "../components/common/PageHeader";

import {
  fleetAlerts,
} from "../data/alerts";

import type {
  AlertSeverity,
  AlertStatus,
  FleetAlert,
} from "../types/alert";

import "../components/alerts/alerts.css";


// ============================================================
// HELPERS
// ============================================================

function getSeverityClass(
  severity: AlertSeverity
) {

  switch (severity) {

    case "Critical":
      return "alert-badge alert-badge-critical";

    case "High":
      return "alert-badge alert-badge-high";

    case "Medium":
      return "alert-badge alert-badge-medium";

    default:
      return "alert-badge alert-badge-low";

  }

}


function getSeverityIcon(
  severity: AlertSeverity
) {

  switch (severity) {

    case "Critical":
      return (
        <ShieldAlert
          size={18}
        />
      );

    case "High":
      return (
        <CircleAlert
          size={18}
        />
      );

    case "Medium":
      return (
        <AlertTriangle
          size={18}
        />
      );

    default:
      return (
        <Bell
          size={18}
        />
      );

  }

}


// ============================================================
// PAGE
// ============================================================

function Alerts() {

  const [
    severityFilter,
    setSeverityFilter,
  ] =
    useState<
      "All" | AlertSeverity
    >("All");


  const [
    statusFilter,
    setStatusFilter,
  ] =
    useState<
      "All" | AlertStatus
    >("All");


  const [
    categoryFilter,
    setCategoryFilter,
  ] =
    useState<
      "All" |
      FleetAlert["category"]
    >("All");


  const [
    search,
    setSearch,
  ] =
    useState("");


  const [
    selectedAlert,
    setSelectedAlert,
  ] =
    useState<FleetAlert | null>(
      null
    );


  // ============================================================
  // COUNTS
  // ============================================================

  const criticalCount =
    fleetAlerts.filter(
      alert =>
        alert.severity ===
        "Critical" &&
        alert.status !==
          "Resolved"
    ).length;


  const highCount =
    fleetAlerts.filter(
      alert =>
        alert.severity ===
        "High" &&
        alert.status !==
          "Resolved"
    ).length;


  const mediumCount =
    fleetAlerts.filter(
      alert =>
        alert.severity ===
        "Medium" &&
        alert.status !==
          "Resolved"
    ).length;


  const lowCount =
    fleetAlerts.filter(
      alert =>
        alert.severity ===
        "Low" &&
        alert.status !==
          "Resolved"
    ).length;


  const activeCount =
    fleetAlerts.filter(
      alert =>
        alert.status !==
        "Resolved"
    ).length;


  // ============================================================
  // FILTER
  // ============================================================

  const filteredAlerts =
    useMemo(() => {

      return fleetAlerts.filter(
        alert => {

          const matchesSeverity =
            severityFilter ===
              "All" ||
            alert.severity ===
              severityFilter;


          const matchesStatus =
            statusFilter ===
              "All" ||
            alert.status ===
              statusFilter;


          const matchesCategory =
            categoryFilter ===
              "All" ||
            alert.category ===
              categoryFilter;


          const searchValue =
            search
              .toLowerCase()
              .trim();


          const matchesSearch =
            !searchValue ||
            alert.title
              .toLowerCase()
              .includes(
                searchValue
              ) ||
            alert.vehicleRegistration
              .toLowerCase()
              .includes(
                searchValue
              ) ||
            alert.description
              .toLowerCase()
              .includes(
                searchValue
              );


          return (
            matchesSeverity &&
            matchesStatus &&
            matchesCategory &&
            matchesSearch
          );

        }
      );

    }, [
      severityFilter,
      statusFilter,
      categoryFilter,
      search,
    ]);


  return (

    <div className="alerts-page">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <PageHeader
        title="Alerts"
        description="Monitor active and historical fleet alerts."
      />


      {/* ======================================================
          SUMMARY
      ====================================================== */}

      <section className="alert-summary-grid">

        <div className="alert-summary-card">

          <div className="alert-summary-icon alert-icon-critical">

            <ShieldAlert
              size={20}
            />

          </div>

          <div>

            <span>
              Critical
            </span>

            <strong>
              {criticalCount}
            </strong>

          </div>

        </div>


        <div className="alert-summary-card">

          <div className="alert-summary-icon alert-icon-high">

            <CircleAlert
              size={20}
            />

          </div>

          <div>

            <span>
              High
            </span>

            <strong>
              {highCount}
            </strong>

          </div>

        </div>


        <div className="alert-summary-card">

          <div className="alert-summary-icon alert-icon-medium">

            <AlertTriangle
              size={20}
            />

          </div>

          <div>

            <span>
              Medium
            </span>

            <strong>
              {mediumCount}
            </strong>

          </div>

        </div>


        <div className="alert-summary-card">

          <div className="alert-summary-icon alert-icon-low">

            <Bell
              size={20}
            />

          </div>

          <div>

            <span>
              Low
            </span>

            <strong>
              {lowCount}
            </strong>

          </div>

        </div>

      </section>


      {/* ======================================================
          ALERT CENTER
      ====================================================== */}

      <section className="alerts-card">

        <div className="alerts-card-header">

          <div>

            <h2>
              Alert Center
            </h2>

            <p>
              {activeCount} active alerts require monitoring.
            </p>

          </div>


          <div className="alerts-header-status">

            <span className="alert-live-dot" />

            Monitoring

          </div>

        </div>


        {/* ====================================================
            FILTERS
        ==================================================== */}

        <div className="alert-filters">

          <div className="alert-search">

            <Search
              size={17}
            />

            <input
              placeholder="Search alerts or vehicles..."
              value={search}
              onChange={
                event =>
                  setSearch(
                    event.target.value
                  )
              }
            />

          </div>


          <select
            value={
              severityFilter
            }
            onChange={
              event =>
                setSeverityFilter(
                  event.target.value as
                    | "All"
                    | AlertSeverity
                )
            }
          >

            <option value="All">
              All Severity
            </option>

            <option value="Critical">
              Critical
            </option>

            <option value="High">
              High
            </option>

            <option value="Medium">
              Medium
            </option>

            <option value="Low">
              Low
            </option>

          </select>


          <select
            value={
              statusFilter
            }
            onChange={
              event =>
                setStatusFilter(
                  event.target.value as
                    | "All"
                    | AlertStatus
                )
            }
          >

            <option value="All">
              All Status
            </option>

            <option value="Active">
              Active
            </option>

            <option value="Investigating">
              Investigating
            </option>

            <option value="Resolved">
              Resolved
            </option>

          </select>


          <select
            value={
              categoryFilter
            }
            onChange={
              event =>
                setCategoryFilter(
                  event.target.value as
                    | "All"
                    | FleetAlert["category"]
                )
            }
          >

            <option value="All">
              All Categories
            </option>

            <option value="Safety">
              Safety
            </option>

            <option value="Maintenance">
              Maintenance
            </option>

            <option value="Driver">
              Driver
            </option>

            <option value="Vehicle">
              Vehicle
            </option>

            <option value="Performance">
              Performance
            </option>

          </select>

        </div>


        {/* ====================================================
            ALERT LIST
        ==================================================== */}

        <div className="alerts-list">

          {filteredAlerts.length === 0 ? (

            <div className="alerts-empty">

              <CheckCircle2
                size={34}
              />

              <h3>
                No alerts found
              </h3>

              <p>
                Try changing your filters or search query.
              </p>

            </div>

          ) : (

            filteredAlerts.map(
              alert => (

                <div
                  className={
                    `alert-row ${
                      alert.status ===
                      "Resolved"
                        ? "alert-row-resolved"
                        : ""
                    }`
                  }
                  key={
                    alert.id
                  }
                >

                  <div
                    className={
                      `alert-severity-icon ${
                        alert.severity
                          .toLowerCase()
                      }`
                    }
                  >

                    {
                      getSeverityIcon(
                        alert.severity
                      )
                    }

                  </div>


                  <div className="alert-main">

                    <div className="alert-title-row">

                      <div>

                        <strong>
                          {
                            alert.title
                          }
                        </strong>

                        <span>
                          {
                            alert.vehicleRegistration
                          }{" "}
                          •{" "}
                          {
                            alert.component
                          }
                        </span>

                      </div>


                      <span
                        className={
                          getSeverityClass(
                            alert.severity
                          )
                        }
                      >

                        {
                          alert.severity
                        }

                      </span>

                    </div>


                    <p>
                      {
                        alert.description
                      }
                    </p>


                    <div className="alert-meta">

                      <span>
                        {
                          alert.timestamp
                        }
                      </span>

                      <span>
                        {
                          alert.category
                        }
                      </span>

                      <span
                        className={
                          `alert-status alert-status-${alert.status
                            .toLowerCase()}`
                        }
                      >
                        {
                          alert.status
                        }
                      </span>

                    </div>

                  </div>


                  <button
                    className="alert-view-button"
                    onClick={() =>
                      setSelectedAlert(
                        alert
                      )
                    }
                  >
                    View
                  </button>

                </div>

              )
            )

          )}

        </div>

      </section>


      {/* ======================================================
          MODAL
      ====================================================== */}

      {selectedAlert && (

        <div
          className="alert-modal-overlay"
          onClick={() =>
            setSelectedAlert(
              null
            )
          }
        >

          <div
            className="alert-modal"
            onClick={
              event =>
                event.stopPropagation()
            }
          >

            <div className="alert-modal-header">

              <div>

                <span
                  className={
                    getSeverityClass(
                      selectedAlert.severity
                    )
                  }
                >
                  {
                    selectedAlert.severity
                  }
                </span>

                <h2>
                  {
                    selectedAlert.title
                  }
                </h2>

              </div>


              <button
                className="alert-close-button"
                onClick={() =>
                  setSelectedAlert(
                    null
                  )
                }
              >

                <X
                  size={19}
                />

              </button>

            </div>


            <div className="alert-modal-body">

              <div className="alert-detail-grid">

                <div>

                  <span>
                    Vehicle
                  </span>

                  <strong>
                    {
                      selectedAlert.vehicleRegistration
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Component
                  </span>

                  <strong>
                    {
                      selectedAlert.component
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Category
                  </span>

                  <strong>
                    {
                      selectedAlert.category
                    }
                  </strong>

                </div>


                <div>

                  <span>
                    Status
                  </span>

                  <strong>
                    {
                      selectedAlert.status
                    }
                  </strong>

                </div>

              </div>


              <div className="alert-detail-section">

                <h3>
                  Description
                </h3>

                <p>
                  {
                    selectedAlert.description
                  }
                </p>

              </div>


              <div className="alert-recommendation">

                <Wrench
                  size={20}
                />

                <div>

                  <strong>
                    Recommended action
                  </strong>

                  <p>
                    {
                      selectedAlert.recommendation
                    }
                  </p>

                </div>

              </div>

            </div>


            <div className="alert-modal-footer">

              <button
                onClick={() =>
                  setSelectedAlert(
                    null
                  )
                }
              >
                Close
              </button>

            </div>

          </div>

        </div>

      )}

    </div>

  );

}

export default Alerts;