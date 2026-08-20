import {
  NavLink,
} from "react-router-dom";

import {
  LayoutDashboard,
  Car,
  Bell,
  BarChart3,
  Brain,
  LogOut,
  Truck,
} from "lucide-react";

function Sidebar() {

  const navigation = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "Vehicles",
      path: "/vehicles",
      icon: Car,
    },
    {
      name: "Alerts",
      path: "/alerts",
      icon: Bell,
    },
    {
      name: "Analytics",
      path: "/analytics",
      icon: BarChart3,
    },
    {
      name: "AI Intelligence",
      path: "/ai",
      icon: Brain,
    },
    {
      name: "Fleets",
      path: "/fleets",
      icon: Truck,
    },
  ];

  return (
    <aside className="sidebar">

      <div className="sidebar-logo">

        <div className="logo-mark">
          F
        </div>

        <div>
          <h1>FleetVision</h1>
          <span>AI Platform</span>
        </div>

      </div>

      <nav className="sidebar-nav">

        {navigation.map(
          ({
            name,
            path,
            icon: Icon,
          }) => (

            <NavLink
              key={path}
              to={path}
              className={({ isActive }) =>
                `sidebar-link ${
                  isActive
                    ? "active"
                    : ""
                }`
              }
            >

              <Icon size={19} />

              <span>
                {name}
              </span>

            </NavLink>

          )
        )}

      </nav>

      <div className="sidebar-footer">

        <NavLink
          to="/login"
          className="sidebar-link"
        >
          <LogOut size={19} />
          <span>Logout</span>
        </NavLink>

      </div>

    </aside>
  );
}

export default Sidebar;