import {
  useMemo,
  useState,
} from "react";

import {
  Activity,
  Brain,
  Car,
  CircleAlert,
  Gauge,
  ShieldAlert,
  Wrench,
  Zap,
} from "lucide-react";

import PageHeader from "../components/common/PageHeader";

import {
  aiRiskVehicles,
  driverRisks,
  maintenancePredictions,
  vehicleAnomalies,
  aiRecommendations,
} from "../data/ai";

import type {
  RiskLevel,
} from "../types/ai";

import "../components/ai/ai.css";


function getRiskClass(
  level: RiskLevel
) {

  switch (level) {

    case "Critical":
      return "ai-badge ai-badge-critical";

    case "High":
      return "ai-badge ai-badge-high";

    case "Medium":
      return "ai-badge ai-badge-medium";

    default:
      return "ai-badge ai-badge-low";

  }

}


function getProgressClass(
  level: RiskLevel
) {

  switch (level) {

    case "Critical":
      return "ai-progress-critical";

    case "High":
      return "ai-progress-high";

    case "Medium":
      return "ai-progress-medium";

    default:
      return "ai-progress-low";

  }

}


function AI() {

  const [
    riskFilter,
    setRiskFilter,
  ] =
    useState<
      "All" | RiskLevel
    >("All");


  // ============================================================
  // AI METRICS
  // ============================================================

  const averageRisk =
    Math.round(
      aiRiskVehicles.reduce(
        (
          total,
          vehicle
        ) =>
          total +
          vehicle.riskScore,
        0
      ) /
        aiRiskVehicles.length
    );


  const vehiclesAtRisk =
    aiRiskVehicles.filter(
      vehicle =>
        vehicle.riskScore >= 60
    ).length;


  const predictedFailures =
    maintenancePredictions.filter(
      prediction =>
        prediction.failureProbability >= 60
    ).length;


  const criticalAlerts =
    vehicleAnomalies.filter(
      anomaly =>
        anomaly.severity ===
        "Critical"
    ).length;


  // ============================================================
  // FILTERED VEHICLES
  // ============================================================

  const filteredVehicles =
    useMemo(() => {

      if (
        riskFilter === "All"
      ) {

        return aiRiskVehicles;

      }

      return aiRiskVehicles.filter(
        vehicle =>
          vehicle.riskLevel ===
          riskFilter
      );

    }, [riskFilter]);


  // ============================================================
  // RISK DISTRIBUTION
  // ============================================================

  const riskDistribution = {

    Critical:
      aiRiskVehicles.filter(
        vehicle =>
          vehicle.riskLevel ===
          "Critical"
      ).length,

    High:
      aiRiskVehicles.filter(
        vehicle =>
          vehicle.riskLevel ===
          "High"
      ).length,

    Medium:
      aiRiskVehicles.filter(
        vehicle =>
          vehicle.riskLevel ===
          "Medium"
      ).length,

    Low:
      aiRiskVehicles.filter(
        vehicle =>
          vehicle.riskLevel ===
          "Low"
      ).length,

  };


  return (

    <div className="ai-page">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <PageHeader
        title="AI Intelligence"
        description="AI-powered fleet risk analysis, predictive maintenance and driver safety intelligence."
      />


      <div className="ai-header-row">

        <div>

          <p
            style={{
              margin: 0,
              fontSize: "13px",
              color: "#64748b",
            }}
          >
            Fleet intelligence overview
          </p>

        </div>


        <div className="ai-status">

          <span
            className="ai-status-dot"
          />

          AI Engine Online

        </div>

      </div>


      {/* ======================================================
          KPI CARDS
      ====================================================== */}

      <section className="ai-kpi-grid">


        {/* RISK */}

        <div className="ai-kpi-card">

          <div className="ai-kpi-top">

            <div>

              <div className="ai-kpi-label">
                Fleet Risk Score
              </div>

              <div className="ai-kpi-value">
                {averageRisk}
              </div>

              <div className="ai-kpi-description">
                Average AI risk score
              </div>

            </div>

            <div className="ai-icon">

              <ShieldAlert
                size={20}
              />

            </div>

          </div>

        </div>


        {/* VEHICLES AT RISK */}

        <div className="ai-kpi-card">

          <div className="ai-kpi-top">

            <div>

              <div className="ai-kpi-label">
                Vehicles At Risk
              </div>

              <div className="ai-kpi-value">
                {vehiclesAtRisk}
              </div>

              <div className="ai-kpi-description">
                Vehicles requiring attention
              </div>

            </div>

            <div className="ai-icon">

              <Car
                size={20}
              />

            </div>

          </div>

        </div>


        {/* PREDICTIONS */}

        <div className="ai-kpi-card">

          <div className="ai-kpi-top">

            <div>

              <div className="ai-kpi-label">
                Predicted Failures
              </div>

              <div className="ai-kpi-value">
                {predictedFailures}
              </div>

              <div className="ai-kpi-description">
                High probability predictions
              </div>

            </div>

            <div className="ai-icon">

              <Wrench
                size={20}
              />

            </div>

          </div>

        </div>


        {/* ANOMALIES */}

        <div className="ai-kpi-card">

          <div className="ai-kpi-top">

            <div>

              <div className="ai-kpi-label">
                Critical Anomalies
              </div>

              <div className="ai-kpi-value">
                {criticalAlerts}
              </div>

              <div className="ai-kpi-description">
                Detected by AI monitoring
              </div>

            </div>

            <div className="ai-icon">

              <CircleAlert
                size={20}
              />

            </div>

          </div>

        </div>

      </section>


      {/* ======================================================
          RISK + RECOMMENDATIONS
      ====================================================== */}

      <section className="ai-grid-2">


        {/* FLEET RISK */}

        <div className="ai-card">

          <div className="ai-card-header">

            <div>

              <h2 className="ai-card-title">
                Fleet Risk Overview
              </h2>

              <p className="ai-card-description">
                AI assessment of overall fleet health.
              </p>

            </div>

            <Gauge size={20} />

          </div>


          <div className="ai-risk-score">

            <div className="ai-risk-circle">

              <div className="ai-risk-circle-inner">

                <div className="ai-risk-number">
                  {averageRisk}
                </div>

                <div className="ai-risk-label">
                  Risk Score
                </div>

              </div>

            </div>


            <div className="ai-risk-info">

              <strong>
                Moderate Fleet Risk
              </strong>

              <span>
                {vehiclesAtRisk} vehicles
                currently require
                attention.
              </span>

              <span>
                AI is monitoring
                vehicle health,
                driver behavior and
                maintenance indicators.
              </span>

            </div>

          </div>

        </div>


        {/* RECOMMENDATIONS */}

        <div className="ai-card">

          <div className="ai-card-header">

            <div>

              <h2 className="ai-card-title">
                AI Recommendations
              </h2>

              <p className="ai-card-description">
                Recommended actions based on current fleet signals.
              </p>

            </div>

            <Brain size={20} />

          </div>


          <div className="ai-recommendations">

            {aiRecommendations
              .slice(0, 3)
              .map(
                recommendation => (

                  <div
                    className="ai-recommendation"
                    key={
                      recommendation.id
                    }
                  >

                    <div className="ai-recommendation-top">

                      <span className="ai-recommendation-title">

                        {
                          recommendation.title
                        }

                      </span>

                      <span
                        className={
                          getRiskClass(
                            recommendation.priority
                          )
                        }
                      >

                        {
                          recommendation.priority
                        }

                      </span>

                    </div>


                    <div className="ai-recommendation-description">

                      {
                        recommendation.description
                      }

                    </div>


                    <div className="ai-recommendation-action">

                      {
                        recommendation.recommendation
                      }

                    </div>

                  </div>

                )
              )}

          </div>

        </div>

      </section>


      {/* ======================================================
          RISK DISTRIBUTION
      ====================================================== */}

      <section className="ai-card ai-section">

        <div className="ai-card-header">

          <div>

            <h2 className="ai-card-title">
              Risk Distribution
            </h2>

            <p className="ai-card-description">
              Current distribution of vehicles by AI risk classification.
            </p>

          </div>

          <Activity size={20} />

        </div>


        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(4, 1fr)",
            gap: "16px",
          }}
        >

          {(
            [
              "Critical",
              "High",
              "Medium",
              "Low",
            ] as RiskLevel[]
          ).map(level => (

            <button
              key={level}
              onClick={() =>
                setRiskFilter(level)
              }
              style={{
                border:
                  riskFilter === level
                    ? "2px solid #334155"
                    : "1px solid #e5e7eb",

                background: "#ffffff",

                borderRadius: "12px",

                padding: "16px",

                textAlign: "left",

                cursor: "pointer",
              }}
            >

              <div
                style={{
                  display: "flex",
                  justifyContent:
                    "space-between",
                  alignItems: "center",
                }}
              >

                <span
                  className={
                    getRiskClass(level)
                  }
                >
                  {level}
                </span>

                <strong
                  style={{
                    fontSize:
                      "22px",
                  }}
                >
                  {
                    riskDistribution[
                      level
                    ]
                  }
                </strong>

              </div>

            </button>

          ))}

        </div>

      </section>


      {/* ======================================================
          VEHICLE RISK TABLE
      ====================================================== */}

      <section className="ai-card ai-section">

        <div className="ai-card-header">

          <div>

            <h2 className="ai-card-title">
              Vehicle Risk Analysis
            </h2>

            <p className="ai-card-description">
              AI-generated risk assessment for each monitored vehicle.
            </p>

          </div>


          <select
            value={riskFilter}
            onChange={event =>
              setRiskFilter(
                event.target.value as
                  | "All"
                  | RiskLevel
              )
            }
            style={{
              padding:
                "8px 12px",

              border:
                "1px solid #e2e8f0",

              borderRadius: "8px",

              background:
                "#ffffff",
            }}
          >

            <option value="All">
              All Risk Levels
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

        </div>


        <div className="ai-table-wrapper">

          <table className="ai-table">

            <thead>

              <tr>

                <th>
                  Vehicle
                </th>

                <th>
                  Risk
                </th>

                <th>
                  Health
                </th>

                <th>
                  Fatigue
                </th>

                <th>
                  Maintenance
                </th>

                <th>
                  Anomalies
                </th>

              </tr>

            </thead>


            <tbody>

              {filteredVehicles.map(
                vehicle => (

                  <tr
                    key={
                      vehicle.id
                    }
                  >

                    <td>

                      <div className="ai-vehicle-name">

                        <strong>
                          {
                            vehicle.registration
                          }
                        </strong>

                        <span>
                          {
                            vehicle.make
                          }{" "}
                          {
                            vehicle.model
                          }
                        </span>

                      </div>

                    </td>


                    <td>

                      <div
                        style={{
                          minWidth:
                            "110px",
                        }}
                      >

                        <div
                          style={{
                            display:
                              "flex",

                            justifyContent:
                              "space-between",

                            marginBottom:
                              "5px",
                          }}
                        >

                            <span
                              style={{
                                fontSize: "12px",
                                fontWeight: 650,
                              }}
                            >
                              {vehicle.riskScore}%
                            </span>

                          <span
                            className={
                              getRiskClass(
                                vehicle.riskLevel
                              )
                            }
                          >
                            {
                              vehicle.riskLevel
                            }
                          </span>

                        </div>


                        <div className="ai-progress">

                          <div
                            className={
                              `ai-progress-bar ${
                                getProgressClass(
                                  vehicle.riskLevel
                                )
                              }`
                            }
                            style={{
                              width:
                                `${vehicle.riskScore}%`,
                            }}
                          />

                        </div>

                      </div>

                    </td>


                    <td>

                      <strong>
                        {
                          vehicle.healthScore
                        }%
                      </strong>

                    </td>


                    <td>

                      {
                        vehicle.fatigueProbability
                      }%

                    </td>


                    <td>

                      {
                        vehicle.maintenanceProbability
                      }%

                    </td>


                    <td>

                      <span
                        className={
                          vehicle.anomalyCount >
                          2
                            ? "ai-badge ai-badge-high"
                            : "ai-badge ai-badge-low"
                        }
                      >

                        {
                          vehicle.anomalyCount
                        }

                      </span>

                    </td>

                  </tr>

                )
              )}

            </tbody>

          </table>

        </div>

      </section>


      {/* ======================================================
          DRIVER + MAINTENANCE
      ====================================================== */}

      <section className="ai-grid-2">


        {/* DRIVER FATIGUE */}

        <div className="ai-card">

          <div className="ai-card-header">

            <div>

              <h2 className="ai-card-title">
                Driver Fatigue Detection
              </h2>

              <p className="ai-card-description">
                AI-estimated driver fatigue probability.
              </p>

            </div>

            <Zap size={20} />

          </div>


          <div className="ai-table-wrapper">

            <table className="ai-table">

              <thead>

                <tr>

                  <th>
                    Driver
                  </th>

                  <th>
                    Vehicle
                  </th>

                  <th>
                    Fatigue
                  </th>

                  <th>
                    Status
                  </th>

                </tr>

              </thead>


              <tbody>

                {driverRisks.map(
                  driver => (

                    <tr
                      key={
                        driver.id
                      }
                    >

                      <td>

                        <strong>
                          {
                            driver.driverName
                          }
                        </strong>

                      </td>

                      <td>
                        {
                          driver.vehicleRegistration
                        }
                      </td>

                      <td>

                        <strong>
                          {
                            driver.fatigueProbability
                          }%
                        </strong>

                      </td>

                      <td>

                        <span
                          className={
                            driver.status ===
                            "Critical"
                              ? "ai-badge ai-badge-critical"
                              : driver.status ===
                                "Warning"
                              ? "ai-badge ai-badge-warning"
                              : "ai-badge ai-badge-normal"
                          }
                        >

                          {
                            driver.status
                          }

                        </span>

                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        </div>


        {/* PREDICTIVE MAINTENANCE */}

        <div className="ai-card">

          <div className="ai-card-header">

            <div>

              <h2 className="ai-card-title">
                Predictive Maintenance
              </h2>

              <p className="ai-card-description">
                Components with elevated failure probability.
              </p>

            </div>

            <Wrench size={20} />

          </div>


          <div className="ai-maintenance-list">

            {maintenancePredictions
              .slice(0, 4)
              .map(
                prediction => (

                  <div
                    className="ai-maintenance-item"
                    key={
                      prediction.id
                    }
                  >

                    <div className="ai-maintenance-main">

                      <strong>
                        {
                          prediction.vehicleRegistration
                        }{" "}
                        —{" "}
                        {
                          prediction.component
                        }
                      </strong>

                      <span>
                        Inspection recommended within{" "}
                        {
                          prediction.estimatedDays
                        }{" "}
                        days
                      </span>

                      <div className="ai-progress">

                        <div
                          className={
                            `ai-progress-bar ${
                              getProgressClass(
                                prediction.severity
                              )
                            }`
                          }
                          style={{
                            width:
                              `${prediction.failureProbability}%`,
                          }}
                        />

                      </div>

                    </div>


                    <div className="ai-maintenance-probability">

                      {
                        prediction.failureProbability
                      }%

                    </div>

                  </div>

                )
              )}

          </div>

        </div>

      </section>


      {/* ======================================================
          ANOMALIES
      ====================================================== */}

      <section className="ai-card ai-section">

        <div className="ai-card-header">

          <div>

            <h2 className="ai-card-title">
              Vehicle Anomaly Detection
            </h2>

            <p className="ai-card-description">
              AI-detected deviations from learned vehicle behavior.
            </p>

          </div>

          <CircleAlert size={20} />

        </div>


        <div className="ai-anomaly-list">

          {vehicleAnomalies.map(
            anomaly => (

              <div
                className="ai-anomaly"
                key={
                  anomaly.id
                }
              >

                <div className="ai-anomaly-top">

                  <div className="ai-anomaly-title">

                    <strong>

                      {
                        anomaly.vehicleRegistration
                      }{" "}
                      —{" "}
                      {
                        anomaly.anomalyType
                      }

                    </strong>

                    <span>

                      {
                        anomaly.component
                      }{" "}
                      •{" "}
                      {
                        anomaly.detectedAt
                      }

                    </span>

                  </div>


                  <span
                    className={
                      getRiskClass(
                        anomaly.severity
                      )
                    }
                  >

                    {
                      anomaly.severity
                    }

                  </span>

                </div>


                <div className="ai-anomaly-description">

                  {
                    anomaly.description
                  }

                </div>

              </div>

            )
          )}

        </div>

      </section>


      {/* ======================================================
          FINAL AI INSIGHT
      ====================================================== */}

      <section
        className="ai-card"
        style={{
          background:
            "#f8fafc",
        }}
      >

        <div
          style={{
            display: "flex",
            gap: "14px",
            alignItems:
              "flex-start",
          }}
        >

          <div className="ai-icon">

            <Brain size={21} />

          </div>


          <div>

            <h2
              className="ai-card-title"
            >
              AI Fleet Summary
            </h2>

            <p
              style={{
                marginTop:
                  "8px",

                fontSize:
                  "13px",

                lineHeight:
                  "1.6",

                color:
                  "#64748b",
              }}
            >

              FleetVision AI has identified{" "}
              <strong>
                {vehiclesAtRisk}
              </strong>{" "}
              vehicles requiring
              attention. The highest
              current risk is associated
              with{" "}
              <strong>
                FV-001
              </strong>
              , primarily due to elevated
              engine temperature,
              maintenance probability
              and driver fatigue indicators.

              {" "}

              Preventive intervention is
              recommended before these
              signals develop into costly
              failures or safety incidents.

            </p>

          </div>

        </div>

      </section>

    </div>

  );

}


export default AI;
