import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import MainLayout from "../components/layout/MainLayout";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Vehicles from "../pages/Vehicles";
import VehicleDetails from "../pages/VehicleDetails";
import Alerts from "../pages/Alerts";
import Analytics from "../pages/Analytics";
import AI from "../pages/AI";
import Fleets from "../pages/Fleets";
import EditVehicle from "../pages/EditVehicle";

function AppRouter() {
  return (
    <Routes>

      {/* =====================================================
          AUTHENTICATION
      ===================================================== */}

      <Route
        path="/login"
        element={<Login />}
      />


      {/* =====================================================
          MAIN APPLICATION
      ===================================================== */}

      <Route
        path="/"
        element={<MainLayout />}
      >

        <Route
          index
          element={
            <Navigate
              to="/dashboard"
              replace
            />
          }
        />


        {/* Dashboard */}

        <Route
          path="dashboard"
          element={<Dashboard />}
        />


        {/* Vehicles */}

        <Route
          path="vehicles"
          element={<Vehicles />}
        />

        <Route
          path="vehicles/:vehicleId"
          element={<VehicleDetails />}
        />

        <Route
          path="vehicles/:id/edit"
          element={<EditVehicle />}
        />

        {/* Fleets */}

        <Route
          path="fleets"
          element={<Fleets />}
        />


        {/* Alerts */}

        <Route
          path="alerts"
          element={<Alerts />}
        />


        {/* Analytics */}

        <Route
          path="analytics"
          element={<Analytics />}
        />


        {/* AI */}

        <Route
          path="ai"
          element={<AI />}
        />

      </Route>


      {/* =====================================================
          UNKNOWN ROUTES
      ===================================================== */}

      <Route
        path="*"
        element={
          <Navigate
            to="/dashboard"
            replace
          />
        }
      />

    </Routes>
  );
}

export default AppRouter;