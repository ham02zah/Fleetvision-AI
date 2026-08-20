function Login() {
  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#f5f7fa",
      }}
    >

      <div
        style={{
          width: "400px",
          background: "white",
          padding: "35px",
          borderRadius: "12px",
          boxShadow:
            "0 10px 30px rgba(0,0,0,0.08)",
        }}
      >

        <h1>
          FleetVision AI
        </h1>

        <p
          style={{
            color: "#6b7280",
            marginBottom: "25px",
          }}
        >
          Sign in to your fleet dashboard.
        </p>

        <div style={{ marginBottom: "15px" }}>

          <label>
            Email
          </label>

          <input
            type="email"
            placeholder="admin@example.com"
            style={{
              width: "100%",
              padding: "11px",
              marginTop: "6px",
              border:
                "1px solid #d1d5db",
              borderRadius: "7px",
            }}
          />

        </div>

        <div style={{ marginBottom: "20px" }}>

          <label>
            Password
          </label>

          <input
            type="password"
            placeholder="••••••••"
            style={{
              width: "100%",
              padding: "11px",
              marginTop: "6px",
              border:
                "1px solid #d1d5db",
              borderRadius: "7px",
            }}
          />

        </div>

        <button
          type="button"
          style={{
            width: "100%",
            padding: "12px",
            border: "none",
            borderRadius: "7px",
            background: "#2563eb",
            color: "white",
            fontWeight: 600,
            cursor: "pointer",
          }}
        >
          Sign In
        </button>

      </div>

    </div>
  );
}

export default Login;