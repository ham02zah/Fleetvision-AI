import {
  useMemo,
  useState,
} from "react";

import PageHeader from "../components/common/PageHeader";

import "../components/alerts/alerts.css";


type AlertSeverity =
  | "critical"
  | "warning"
  | "info";

type AlertStatus =
  | "active"
  | "acknowledged"
  | "resolved";


interface FleetAlert {
  id: string;

  title: string;

  description: string;

  vehicle: string;

  severity: AlertSeverity;

  status: AlertStatus;

  timestamp: string;
}


const initialAlerts: FleetAlert[] = [
  {
    id: "ALT-001",
    title: "Engine Temperature High",
    description:
      "Engine temperature exceeded the recommended operating threshold.",
    vehicle: "Toyota Hilux — FL-001",
    severity: "critical",
    status: "active",
    timestamp: "Today, 10:42 AM",
  },

  {
    id: "ALT-002",
    title: "Driver Fatigue Detected",
    description:
      "Repeated fatigue indicators detected during vehicle operation.",
    vehicle: "Ford Transit — FL-002",
    severity: "critical",
    status: "active",
    timestamp: "Today, 09:18 AM",
  },

  {
    id: "ALT-003",
    title: "Maintenance Due",
    description:
      "Vehicle has reached the scheduled maintenance interval.",
    vehicle: "Mercedes Sprinter — FL-003",
    severity: "warning",
    status: "acknowledged",
    timestamp: "Today, 08:35 AM",
  },

  {
    id: "ALT-004",
    title: "Unusual Fuel Consumption",
    description:
      "Fuel consumption is above the vehicle's expected operating range.",
    vehicle: "Isuzu D-Max — FL-004",
    severity: "warning",
    status: "active",
    timestamp: "Yesterday, 06:41 PM",
  },

  {
    id: "ALT-005",
    title: "Speed Threshold Exceeded",
    description:
      "Vehicle exceeded the configured maximum speed threshold.",
    vehicle: "Toyota Corolla — FL-005",
    severity: "warning",
    status: "resolved",
    timestamp: "Yesterday, 04:20 PM",
  },

  {
    id: "ALT-006",
    title: "Vehicle Back Online",
    description:
      "Vehicle successfully reconnected to the fleet monitoring system.",
    vehicle: "Ford Ranger — FL-006",
    severity: "info",
    status: "resolved",
    timestamp: "Yesterday, 02:15 PM",
  },
];


function Alerts() {

  const [alerts, setAlerts] =
    useState<FleetAlert[]>(
      initialAlerts
    );

  const [filter, setFilter] =
    useState<
      "all" |
      AlertSeverity
    >("all");

  const [search, setSearch] =
    useState("");


  const filteredAlerts =
    useMemo(() => {

      return alerts.filter(
        (alert) => {

          const matchesFilter =
            filter === "all" ||
            alert.severity === filter;

          const searchText =
            search.toLowerCase();

          const matchesSearch =
            alert.title
              .toLowerCase()
              .includes(searchText) ||

            alert.vehicle
              .toLowerCase()
              .includes(searchText) ||

            alert.description
              .toLowerCase()
              .includes(searchText);

          return (
            matchesFilter &&
            matchesSearch
          );
        }
      );

    }, [
      alerts,
      filter,
      search,
    ]);


  const activeCount =
    alerts.filter(
      (alert) =>
        alert.status === "active"
    ).length;


  const criticalCount =
    alerts.filter(
      (alert) =>
        alert.severity === "critical" &&
        alert.status !== "resolved"
    ).length;


  const warningCount =
    alerts.filter(
      (alert) =>
        alert.severity === "warning" &&
        alert.status !== "resolved"
    ).length;


  const resolvedCount =
    alerts.filter(
      (alert) =>
        alert.status === "resolved"
    ).length;


  const updateStatus =
    (
      id: string,
      status: AlertStatus
    ) => {

      setAlerts(
        (current) =>
          current.map(
            (alert) =>
              alert.id === id
                ? {
                    ...alert,
                    status,
                  }
                : alert
          )
      );
    };


  return (

    <div className="alerts-page">

      <PageHeader
        title="Alerts"
        description="Monitor active and historical fleet alerts."
      />


      {/* =====================================================
          SUMMARY CARDS
      ===================================================== */}

      <div className="alert-summary-grid">

        <div className="alert-summary-card critical">

          <h3>
            Critical Alerts
          </h3>

          <div className="alert-summary-value">
            {criticalCount}
          </div>

        </div>


        <div className="alert-summary-card warning">

          <h3>
            Warnings
          </h3>

          <div className="alert-summary-value">
            {warningCount}
          </div>

        </div>


        <div className="alert-summary-card info">

          <h3>
            Active Alerts
          </h3>

          <div className="alert-summary-value">
            {activeCount}
          </div>

        </div>


        <div className="alert-summary-card resolved">

          <h3>
            Resolved
          </h3>

          <div className="alert-summary-value">
            {resolvedCount}
          </div>

        </div>

      </div>


      {/* =====================================================
          TOOLBAR
      ===================================================== */}

      <div className="alert-toolbar">

        <div className="alert-search">

          <input
            type="text"
            placeholder="Search alerts, vehicles..."
            value={search}
            onChange={(event) =>
              setSearch(
                event.target.value
              )
            }
          />

        </div>


        <div className="alert-filters">

          <button
            className={`alert-filter-button ${
              filter === "all"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setFilter("all")
            }
          >
            All
          </button>


          <button
            className={`alert-filter-button ${
              filter === "critical"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setFilter("critical")
            }
          >
            Critical
          </button>


          <button
            className={`alert-filter-button ${
              filter === "warning"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setFilter("warning")
            }
          >
            Warning
          </button>


          <button
            className={`alert-filter-button ${
              filter === "info"
                ? "active"
                : ""
            }`}
            onClick={() =>
              setFilter("info")
            }
          >
            Info
          </button>

        </div>

      </div>


      {/* =====================================================
          ALERT TABLE
      ===================================================== */}

      <div className="alert-table-container">

        {filteredAlerts.length === 0 ? (

          <div className="alert-empty">

            <h3>
              No alerts found
            </h3>

            <p>
              Try changing your search
              or filter.
            </p>

          </div>

        ) : (

          <table className="alert-table">

            <thead>

              <tr>

                <th>
                  Alert
                </th>

                <th>
                  Vehicle
                </th>

                <th>
                  Severity
                </th>

                <th>
                  Status
                </th>

                <th>
                  Time
                </th>

                <th>
                  Actions
                </th>

              </tr>

            </thead>


            <tbody>

              {filteredAlerts.map(
                (alert) => (

                  <tr key={alert.id}>

                    <td>

                      <div className="alert-title">

                        <strong>
                          {alert.title}
                        </strong>

                        <span>
                          {alert.description}
                        </span>

                      </div>

                    </td>


                    <td>
                      {alert.vehicle}
                    </td>


                    <td>

                      <span
                        className={`alert-severity ${alert.severity}`}
                      >
                        {alert.severity}
                      </span>

                    </td>


                    <td>

                      <span
                        className={`alert-status ${alert.status}`}
                      >
                        {alert.status}
                      </span>

                    </td>


                    <td>
                      {alert.timestamp}
                    </td>


                    <td>

                      <div className="alert-actions">

                        {alert.status ===
                          "active" && (

                          <button
                            className="alert-action-button acknowledge"
                            onClick={() =>
                              updateStatus(
                                alert.id,
                                "acknowledged"
                              )
                            }
                          >
                            Acknowledge
                          </button>

                        )}


                        {alert.status !==
                          "resolved" && (

                          <button
                            className="alert-action-button resolve"
                            onClick={() =>
                              updateStatus(
                                alert.id,
                                "resolved"
                              )
                            }
                          >
                            Resolve
                          </button>

                        )}

                      </div>

                    </td>

                  </tr>

                )
              )}

            </tbody>

          </table>

        )}

      </div>

    </div>

  );
}


export default Alerts;