import {
  ResponsiveContainer,
  LineChart,
  Line,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

import {
  utilizationData,
  fuelData,
  vehicleStatusData,
  maintenanceData,
} from "./analyticsData";

import "./analytics.css";


// ============================================================
// UTILIZATION CHART
// ============================================================

export function UtilizationChart() {
  return (
    <div className="analytics-chart-card">

      <div className="analytics-chart-header">
        <div>
          <h3>Vehicle Utilization</h3>

          <p>
            Average fleet utilization over the selected period.
          </p>
        </div>
      </div>

      <div className="analytics-chart-container">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >
          <LineChart
            data={utilizationData}
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 5,
            }}
          >

            <CartesianGrid
              strokeDasharray="3 3"
              vertical={false}
            />

            <XAxis
              dataKey="day"
              tickLine={false}
              axisLine={false}
            />

            <YAxis
              domain={[0, 100]}
              tickFormatter={(value) =>
                `${value}%`
              }
              tickLine={false}
              axisLine={false}
            />

            <Tooltip
              formatter={(value) =>
                `${value}%`
              }
            />

            <Line
              type="monotone"
              dataKey="utilization"
              stroke="#2563eb"
              strokeWidth={3}
              dot={{
                r: 4,
              }}
              activeDot={{
                r: 6,
              }}
            />

          </LineChart>
        </ResponsiveContainer>

      </div>

    </div>
  );
}


// ============================================================
// FUEL CHART
// ============================================================

export function FuelConsumptionChart() {
  return (
    <div className="analytics-chart-card">

      <div className="analytics-chart-header">
        <div>
          <h3>Fuel Consumption</h3>

          <p>
            Total fuel consumption by month.
          </p>
        </div>
      </div>

      <div className="analytics-chart-container">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >
          <BarChart
            data={fuelData}
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 5,
            }}
          >

            <CartesianGrid
              strokeDasharray="3 3"
              vertical={false}
            />

            <XAxis
              dataKey="month"
              tickLine={false}
              axisLine={false}
            />

            <YAxis
              tickFormatter={(value) =>
                `${value / 1000}k`
              }
              tickLine={false}
              axisLine={false}
            />

            <Tooltip />

            <Bar
              dataKey="consumption"
              fill="#2563eb"
              radius={[
                6,
                6,
                0,
                0,
              ]}
            />

          </BarChart>
        </ResponsiveContainer>

      </div>

    </div>
  );
}


// ============================================================
// VEHICLE STATUS CHART
// ============================================================

export function VehicleStatusChart() {

  const COLORS = [
    "#22c55e",
    "#f59e0b",
    "#94a3b8",
  ];

  return (
    <div className="analytics-chart-card">

      <div className="analytics-chart-header">

        <div>

          <h3>
            Vehicle Status
          </h3>

          <p>
            Current fleet vehicle status.
          </p>

        </div>

      </div>

      <div className="analytics-pie-container">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <PieChart>

            <Pie
              data={vehicleStatusData}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              innerRadius={65}
              outerRadius={95}
              paddingAngle={3}
            >

              {vehicleStatusData.map(
                (_, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={
                      COLORS[index]
                    }
                  />
                )
              )}

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}


// ============================================================
// MAINTENANCE CHART
// ============================================================

export function MaintenanceTrendChart() {
  return (
    <div className="analytics-chart-card">

      <div className="analytics-chart-header">

        <div>

          <h3>
            Maintenance Trend
          </h3>

          <p>
            Maintenance events recorded
            each month.
          </p>

        </div>

      </div>

      <div className="analytics-chart-container">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <LineChart
            data={maintenanceData}
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 5,
            }}
          >

            <CartesianGrid
              strokeDasharray="3 3"
              vertical={false}
            />

            <XAxis
              dataKey="month"
              tickLine={false}
              axisLine={false}
            />

            <YAxis
              allowDecimals={false}
              tickLine={false}
              axisLine={false}
            />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="events"
              stroke="#f59e0b"
              strokeWidth={3}
              dot={{
                r: 4,
              }}
              activeDot={{
                r: 6,
              }}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}