import {
  Bell,
  Search,
} from "lucide-react";

function Topbar() {
  return (
    <header className="topbar">

      <div className="topbar-search">

        <Search size={18} />

        <input
          type="text"
          placeholder="Search fleet..."
        />

      </div>

      <div className="topbar-actions">

        <button
          className="notification-button"
          type="button"
        >
          <Bell size={20} />

          <span className="notification-dot" />
        </button>

        <div className="user-profile">

          <div className="user-avatar">
            H
          </div>

          <div className="user-info">
            <strong>
              Fleet Admin
            </strong>

            <span>
              Administrator
            </span>
          </div>

        </div>

      </div>

    </header>
  );
}

export default Topbar;