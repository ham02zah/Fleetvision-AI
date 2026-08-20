import {
  Car,
  Gauge,
  Fuel,
  Wrench,
  Activity,
} from "lucide-react";

import PageHeader from "../components/common/PageHeader";

import {
  UtilizationChart,
  FuelConsumptionChart,
  VehicleStatusChart,
  MaintenanceTrendChart,
} from "../components/analytics/AnalyticsCharts";

import {
  fleetPerformanceData,
} from "../components/analytics/analyticsData";

import "../components/analytics/analytics.css";


function Analytics() {

  return (

    <div className="analytics-page">

      {/* ======================================================
          PAGE HEADER
      ====================================================== */}

      <PageHeader
        title="Analytics"
        description="Monitor fleet performance, utilization and operational trends."
      />


      {/* ======================================================
          PERIOD FILTER
      ====================================================== */}

      <div className="analytics-controls">

        <select
          className="analytics-period-select"
          defaultValue="30"
        >

          <option value="7">
            Last 7 days
          </option>

          <option value="30">
            Last 30 days
          </option>

          <option value="90">
            Last 90 days
          </option>

          <option value="365">
            Last year
          </option>

        </select>

      </div>


      {/* ======================================================
          KPI CARDS
      ====================================================== */}

      <div className="analytics-kpi-grid">


        {/* TOTAL VEHICLES */}

        <div className="analytics-kpi-card">

          <div className="analytics-kpi-top">

            <p className="analytics-kpi-label">
              Total Vehicles
            </p>

            <div className="analytics-kpi-icon">
              <Car size={18} />
            </div>

          </div>

          <p className="analytics-kpi-value">
            48
          </p>

          <div className="analytics-kpi-change">
            +4.2% from last month
          </div>

        </div>


        {/* ACTIVE VEHICLES */}

        <div className="analytics-kpi-card">

          <div className="analytics-kpi-top">

            <p className="analytics-kpi-label">
              Active Vehicles
            </p>

            <div className="analytics-kpi-icon">
              <Activity size={18} />
            </div>

          </div>

          <p className="analytics-kpi-value">
            42
          </p>

          <div className="analytics-kpi-change">
            87.5% of total fleet
          </div>

        </div>


        {/* UTILIZATION */}

        <div className="analytics-kpi-card">

          <div className="analytics-kpi-top">

            <p className="analytics-kpi-label">
              Avg. Utilization
            </p>

            <div className="analytics-kpi-icon">
              <Gauge size={18} />
            </div>

          </div>

          <p className="analytics-kpi-value">
            78%
          </p>

          <div className="analytics-kpi-change">
            +6.8% this period
          </div>

        </div>


        {/* FUEL */}

        <div className="analytics-kpi-card">

          <div className="analytics-kpi-top">

            <p className="analytics-kpi-label">
              Fuel Efficiency
            </p>

            <div className="analytics-kpi-icon">
              <Fuel size={18} />
            </div>

          </div>

          <p className="analytics-kpi-value">
            8.4
          </p>

          <div className="analytics-kpi-change">
            L / 100 km
          </div>

        </div>


        {/* MAINTENANCE */}

        <div className="analytics-kpi-card">

          <div className="analytics-kpi-top">

            <p className="analytics-kpi-label">
              Maintenance Cost
            </p>

            <div className="analytics-kpi-icon">
              <Wrench size={18} />
            </div>

          </div>

          <p className="analytics-kpi-value">
            $12.4K
          </p>

          <div className="analytics-kpi-change">
            -8.2% from last month
          </div>

        </div>

      </div>


      {/* ======================================================
          CHARTS
      ====================================================== */}

      <div className="analytics-chart-grid">

        <UtilizationChart />

        <FuelConsumptionChart />

        <VehicleStatusChart />

        <MaintenanceTrendChart />

      </div>


      {/* ======================================================
          FLEET PERFORMANCE
      ====================================================== */}

      <div className="analytics-table-card">

        <div className="analytics-table-header">

          <h3>
            Fleet Performance
          </h3>

          <p>
            Operational performance across fleet groups.
          </p>

        </div>


        <div className="analytics-table-wrapper">

          <table className="analytics-table">

            <thead>

              <tr>

                <th>
                  Fleet
                </th>

                <th>
                  Vehicles
                </th>

                <th>
                  Utilization
                </th>

                <th>
                  Fuel Efficiency
                </th>

                <th>
                  Maintenance Cost
                </th>

              </tr>

            </thead>


            <tbody>

              {fleetPerformanceData.map(
                (fleet) => (

                  <tr
                    key={fleet.fleet}
                  >

                    <td className="analytics-table-fleet">
                      {fleet.fleet}
                    </td>

                    <td>
                      {fleet.vehicles}
                    </td>

                    <td>

                      <span className="analytics-utilization">

                        {fleet.utilization}%

                      </span>

                    </td>

                    <td>
                      {fleet.fuelEfficiency}
                      {" "}
                      L / 100 km
                    </td>

                    <td>
                      $
                      {fleet.maintenanceCost.toLocaleString()}
                    </td>

                  </tr>

                )
              )}

            </tbody>

          </table>

        </div>

      </div>

    </div>

  );
}


export default Analytics;