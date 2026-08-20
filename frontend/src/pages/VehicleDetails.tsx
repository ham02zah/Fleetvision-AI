import {
  useEffect,
  useState,
} from "react";

import {
  useParams,
  useNavigate,
} from "react-router-dom";

import {
  ArrowLeft,
  Pencil,
  Car,
  Fuel,
  Calendar,
  Hash,
  Palette,
  Building2,
  CircleCheck,
  CircleX,
} from "lucide-react";

import type {
  Vehicle,
} from "../types/vehicle";

import {
  vehicleService,
} from "../services/vehicleService";

import {
  fleetService,
} from "../services/fleetService";

import type {
  Fleet,
} from "../types/fleet";

import "../components/fleet/fleet.css";


export default function VehicleDetails() {

  const {
    vehicleId,
  } = useParams();

  const navigate =
    useNavigate();


  const [vehicle, setVehicle] =
    useState<Vehicle | null>(null);

  const [fleet, setFleet] =
    useState<Fleet | null>(null);

  const [loading, setLoading] =
    useState(true);


  useEffect(() => {

    if (!vehicleId) {
      return;
    }

    loadVehicle();

  }, [vehicleId]);


  const loadVehicle =
    async () => {

      try {

        setLoading(true);

        const data =
          await vehicleService.getVehicle(
            vehicleId!
          );

        setVehicle(data);


        try {

          const fleetData =
            await fleetService.getFleet(
              data.fleet_id
            );

          setFleet(
            fleetData
          );

        } catch (fleetError) {

          console.error(
            "Unable to load fleet:",
            fleetError
          );

        }

      } catch (error) {

        console.error(
          "Unable to load vehicle:",
          error
        );

        setVehicle(null);

      } finally {

        setLoading(false);

      }

    };


  if (loading) {

    return (

      <div className="vehicle-state">

        <Car size={32} />

        <h3>
          Loading vehicle...
        </h3>

      </div>

    );

  }


  if (!vehicle) {

    return (

      <div className="vehicle-state">

        <Car size={40} />

        <h3>
          Vehicle not found
        </h3>

        <p>
          The requested vehicle could not be loaded.
        </p>

        <button
          onClick={() =>
            navigate("/vehicles")
          }
        >
          Back to Vehicles
        </button>

      </div>

    );

  }


  return (

    <div className="vehicle-details-page">

      {/* ======================================================
          TOP BAR
      ====================================================== */}

      <div className="vehicle-details-topbar">

        <button
          className="back-button"
          onClick={() =>
            navigate("/vehicles")
          }
        >

          <ArrowLeft size={17} />

          Back to Vehicles

        </button>


        <button
          className="vehicle-edit-button"
          onClick={() =>
            navigate(
              `/vehicles/${vehicle.id}/edit`
            )
          }
        >

          <Pencil size={17} />

          Edit Vehicle

        </button>

      </div>


      {/* ======================================================
          VEHICLE HERO
      ====================================================== */}

      <div className="vehicle-details-hero">

        <div className="vehicle-details-icon">

          <Car size={38} />

        </div>


        <div className="vehicle-details-title">

          <div className="vehicle-details-title-row">

            <h1>
              {vehicle.make} {vehicle.model}
            </h1>

            <span
              className={
                vehicle.is_active
                  ? "status-badge active"
                  : "status-badge inactive"
              }
            >

              <span className="status-dot" />

              {vehicle.is_active
                ? "Active"
                : "Inactive"}

            </span>

          </div>

          <p>
            {vehicle.registration_number}
          </p>

        </div>

      </div>


      {/* ======================================================
          INFORMATION
      ====================================================== */}

      <div className="vehicle-details-grid">


        {/* BASIC INFORMATION */}

        <div className="vehicle-detail-card">

          <div className="vehicle-detail-card-header">

            <h2>
              Vehicle Information
            </h2>

          </div>


          <div className="vehicle-info-list">


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Car size={18} />
              </div>

              <div>

                <span>
                  Make
                </span>

                <strong>
                  {vehicle.make}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Car size={18} />
              </div>

              <div>

                <span>
                  Model
                </span>

                <strong>
                  {vehicle.model}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Calendar size={18} />
              </div>

              <div>

                <span>
                  Year
                </span>

                <strong>
                  {vehicle.year}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Fuel size={18} />
              </div>

              <div>

                <span>
                  Fuel Type
                </span>

                <strong>
                  {vehicle.fuel_type}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Palette size={18} />
              </div>

              <div>

                <span>
                  Color
                </span>

                <strong>
                  {vehicle.color || "Not specified"}
                </strong>

              </div>

            </div>


          </div>

        </div>


        {/* IDENTIFICATION */}

        <div className="vehicle-detail-card">

          <div className="vehicle-detail-card-header">

            <h2>
              Identification
            </h2>

          </div>


          <div className="vehicle-info-list">


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Hash size={18} />
              </div>

              <div>

                <span>
                  Registration Number
                </span>

                <strong>
                  {vehicle.registration_number}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Hash size={18} />
              </div>

              <div>

                <span>
                  VIN
                </span>

                <strong className="monospace">
                  {vehicle.vin}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">
                <Building2 size={18} />
              </div>

              <div>

                <span>
                  Fleet
                </span>

                <strong>
                  {fleet?.name || "Unknown Fleet"}
                </strong>

              </div>

            </div>


            <div className="vehicle-info-item">

              <div className="vehicle-info-icon">

                {vehicle.is_active
                  ? <CircleCheck size={18} />
                  : <CircleX size={18} />
                }

              </div>

              <div>

                <span>
                  Status
                </span>

                <strong>
                  {vehicle.is_active
                    ? "Active"
                    : "Inactive"}
                </strong>

              </div>

            </div>


          </div>

        </div>


      </div>


      {/* ======================================================
          SYSTEM INFORMATION
      ====================================================== */}

      <div className="vehicle-detail-card vehicle-system-card">

        <div className="vehicle-detail-card-header">

          <h2>
            System Information
          </h2>

        </div>


        <div className="vehicle-system-grid">

          <div>

            <span>
              Vehicle ID
            </span>

            <strong className="monospace">
              {vehicle.id}
            </strong>

          </div>


          {vehicle.created_at && (

            <div>

              <span>
                Created
              </span>

              <strong>
                {new Date(
                  vehicle.created_at
                ).toLocaleString()}
              </strong>

            </div>

          )}


          {vehicle.updated_at && (

            <div>

              <span>
                Last Updated
              </span>

              <strong>
                {new Date(
                  vehicle.updated_at
                ).toLocaleString()}
              </strong>

            </div>

          )}

        </div>

      </div>

    </div>

  );

}