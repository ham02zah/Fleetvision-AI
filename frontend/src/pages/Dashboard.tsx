import {
  useEffect,
  useState,
} from "react";

import PageHeader from "../components/common/PageHeader";

import KPICard from "../components/dashboard/KPICard";

import "../components/dashboard/dashboard.css";

import {
  dashboardService,
} from "../services/dashboardService";

import type {
  DashboardOverview,
} from "../types/dashboard";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function Dashboard() {
  const [data, setData] =
    useState<DashboardOverview | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState<string | null>(null);

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        setLoading(true);
        setError(null);

        const result =
          await dashboardService.getOverview();

        setData(result);
      } catch (err) {
        console.error(
          "Dashboard request failed:",
          err
        );

        setError(
          "Unable to load dashboard data."
        );
      } finally {
        setLoading(false);
      }
    };

    loadDashboard();
  }, []);

  if (loading) {
    return (
      <div>
        <PageHeader
          title="Fleet Dashboard"
          description="Real-time fleet monitoring and AI insights."
        />

        <div className="dashboard-loading">
          <div className="loading-spinner" />
          <p>Loading fleet data...</p>
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div>
        <PageHeader
          title="Fleet Dashboard"
          description="Real-time fleet monitoring and AI insights."
        />

        <div className="dashboard-error">
          <h2>Unable to load dashboard</h2>

          <p>
            {error ||
              "No dashboard data was returned by the backend."}
          </p>
        </div>
      </div>
    );
  }

  const summary = data.summary;

  const speedChartData =
    [...(data.speed_trend || [])]
      .reverse()
      .map((point) => ({
        ...point,
        time: new Date(
          point.timestamp
        ).toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      }));

  return (
    <div className="dashboard-page">

      <PageHeader
        title="Fleet Dashboard"
        description="Real-time fleet monitoring and AI insights."
      />

      {/* KPI CARDS */}

      <div className="dashboard-kpi-grid">

        <KPICard
          title="Total Vehicles"
          value={
            summary.total_vehicles ?? 0
          }
          subtitle="Vehicles in fleet"
        />

        <KPICard
          title="Active Vehicles"
          value={
            summary.active_vehicles ?? 0
          }
          subtitle="Currently active"
        />

        <KPICard
          title="AI Predictions"
          value={
            summary.total_predictions ?? 0
          }
          subtitle="Predictions generated"
        />

        <KPICard
          title="Active Alerts"
          value={
            summary.total_alerts ?? 0
          }
          subtitle="Fleet alerts"
        />

        <KPICard
          title="Fleet Health"
          value={
            summary.average_health_score !==
            undefined
              ? `${summary.average_health_score.toFixed(1)}%`
              : "N/A"
          }
          subtitle="Average health score"
        />

        <KPICard
          title="Driver Score"
          value={
            summary.average_driver_score !==
            undefined
              ? `${summary.average_driver_score.toFixed(1)}%`
              : "N/A"
          }
          subtitle="Average driver score"
        />

        <KPICard
          title="Average Speed"
          value={
            summary.average_speed !==
            undefined
              ? `${summary.average_speed.toFixed(1)}`
              : "N/A"
          }
          subtitle="Average fleet speed"
        />

        <KPICard
          title="Fleet Status"
          value={
            summary.active_vehicles ===
            summary.total_vehicles
              ? "Healthy"
              : "Monitoring"
          }
          subtitle="Current fleet state"
        />

      </div>

      {/* SPEED TREND */}

      <div className="dashboard-section">

        <div className="dashboard-section-header">

          <div>
            <h2>Speed Trend</h2>

            <p>
              Recent vehicle speed measurements
            </p>
          </div>

        </div>

        <div className="dashboard-chart-card">

          {speedChartData.length > 0 ? (
            <ResponsiveContainer
              width="100%"
              height={320}
            >
              <LineChart
                data={speedChartData}
                margin={{
                  top: 10,
                  right: 20,
                  left: 0,
                  bottom: 10,
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="time"
                />

                <YAxis />

                <Tooltip />

                <Line
                  type="monotone"
                  dataKey="speed"
                  name="Speed"
                  stroke="#2563eb"
                  strokeWidth={3}
                  dot={false}
                  activeDot={{
                    r: 5,
                  }}
                />

              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="empty-chart">
              No speed trend data available.
            </div>
          )}

        </div>

      </div>

      {/* FLEET HEALTH */}

      <div className="dashboard-two-column">

        <div className="dashboard-info-card">

          <h2>Fleet Health</h2>

          <p className="dashboard-card-description">
            Current overall fleet health status.
          </p>

          <div className="health-score">

            <div className="health-score-value">
              {summary.average_health_score !==
              undefined
                ? summary.average_health_score.toFixed(
                    1
                  )
                : "N/A"}
            </div>

            <div className="health-score-label">
              Average Health Score
            </div>

          </div>

          <div className="health-progress">

            <div
              className="health-progress-bar"
              style={{
                width: `${Math.min(
                  summary.average_health_score ??
                    0,
                  100
                )}%`,
              }}
            />

          </div>

        </div>

        <div className="dashboard-info-card">

          <h2>Driver Performance</h2>

          <p className="dashboard-card-description">
            Average driver performance across
            the fleet.
          </p>

          <div className="health-score">

            <div className="health-score-value">
              {summary.average_driver_score !==
              undefined
                ? summary.average_driver_score.toFixed(
                    1
                  )
                : "N/A"}
            </div>

            <div className="health-score-label">
              Average Driver Score
            </div>

          </div>

          <div className="health-progress">

            <div
              className="health-progress-bar"
              style={{
                width: `${Math.min(
                  summary.average_driver_score ??
                    0,
                  100
                )}%`,
              }}
            />

          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;