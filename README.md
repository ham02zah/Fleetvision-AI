# FleetVision AI

> AI-powered fleet intelligence platform for vehicle monitoring, predictive maintenance, driver behavior analysis, anomaly detection, alerts, telemetry analytics, and operational decision support.

FleetVision AI is an end-to-end fleet management and vehicle intelligence platform designed to transform vehicle and fleet telemetry into actionable operational intelligence.

The system combines fleet operations, vehicle management, driver management, trip management, telemetry, maintenance, alerts, analytics, machine-learning-based prediction, risk analysis, vehicle health scoring, anomaly detection, recommendations, explainability, and operational decision support.

The platform is built around a FastAPI backend, PostgreSQL database, Redis, SQLAlchemy, Alembic migrations, a modular AI/ML subsystem, Docker/Docker Compose infrastructure, and a React/TypeScript frontend dashboard.

The architecture is intentionally modular. Instead of treating AI as one isolated prediction script, FleetVision AI processes telemetry through validation and feature engineering, sends the resulting information through multiple intelligence modules, and combines their outputs into risk scores, health indicators, maintenance predictions, anomaly information, recommendations, explanations, and operational decisions.

---

## Project Overview

FleetVision AI is designed for fleet operators who need more than simple vehicle CRUD management.

A traditional fleet-management system may tell an operator:

- Which vehicles exist
- Which drivers are assigned
- Where vehicles are located
- What maintenance records exist
- What alerts have been generated

FleetVision AI adds an intelligence layer on top of those operational capabilities.

The platform can analyze telemetry and operational information to determine:

- Vehicle risk
- Vehicle health
- Driving risk
- Driver fatigue-related indicators
- Predicted maintenance problems
- Vehicle anomalies
- Speed predictions
- Performance deviations
- Recommended actions
- Explainable reasons behind recommendations
- Operational AI decisions

The high-level concept is:

```text
                         FLEETVISION AI
                               |
             +-----------------+-----------------+
             |                                   |
             v                                   v
      Fleet Operations                    AI Intelligence
             |                                   |
      +------+------+                    +-------+--------+
      |      |      |                    |       |        |
   Fleets Vehicles Drivers            Risk   Prediction Anomaly
      |      |      |                    |       |        |
      +------+------+                    +-------+--------+
             |                                   |
          Trips                              Maintenance
             |                                   |
        Telemetry                            Health Score
             |                                   |
          Alerts                           Driver Analysis
             |                                   |
             +-----------------+-----------------+
                               |
                               v
                       Decision Engine
                               |
                               v
                     Recommendations
                               |
                               v
                      Operational Action
```

The goal is to turn raw fleet data into information that a fleet operator can actually act upon.

---

# Key Features

FleetVision AI provides a broad fleet-intelligence foundation.

## Fleet Management

Fleet records can be created, listed, retrieved, updated, and deleted.

Fleet information provides the organizational layer used to associate vehicles and operational data.

---

## Vehicle Management

Vehicles are associated with fleets and contain operational information including:

- Make
- Model
- Year
- Registration number
- VIN
- Fuel type
- Color
- Active/inactive status

The frontend provides a dedicated vehicle-management interface for:

- Viewing vehicles
- Creating vehicles
- Viewing vehicle details
- Editing vehicle records through the dedicated edit workflow
- Deleting vehicles

The vehicle details page is intended for viewing vehicle information rather than directly editing it.

---

## Driver Management

The platform supports driver records and driver-related operational intelligence.

Driver intelligence can incorporate information such as:

- Driving hours
- Harsh braking
- Fatigue probability
- Driver risk
- Driver status
- Vehicle association

The AI layer can use these signals to identify drivers requiring additional attention.

---

## Trip Management

Trips provide an operational representation of vehicle journeys.

Trip-related information can be used together with telemetry and vehicle data for downstream analytics and intelligence.

---

## Vehicle Telemetry

FleetVision AI supports vehicle telemetry information such as:

- GPS latitude
- GPS longitude
- Speed
- Heading
- Ignition state
- Engine state
- Fuel level
- Engine temperature
- Odometer
- Timestamp-related information

Telemetry is one of the primary inputs to the AI intelligence pipeline.

---

## Vehicle Status

Vehicle status information can be used to determine the current operational state of vehicles.

This information can be combined with telemetry, maintenance, alerts, and AI outputs to provide fleet-level visibility.

---

## Maintenance

Maintenance functionality supports vehicle maintenance analysis and predictive maintenance intelligence.

The system can identify components with elevated failure probability and provide recommendations such as:

```text
Schedule engine inspection and diagnostic testing.

Inspect brake pads, discs and hydraulic pressure.

Schedule transmission inspection.

Monitor battery voltage and charging performance.
```

The current maintenance intelligence is feature/rule based rather than a separately persisted maintenance machine-learning model.

---

## Fleet Alerts

The system supports fleet alerts across categories such as:

- Safety
- Maintenance
- Driver
- Vehicle
- Performance

Alerts can have severity levels:

```text
Critical
High
Medium
Low
```

and statuses:

```text
Active
Investigating
Resolved
```

Alerts are designed to provide an operational bridge between AI detection and fleet-management action.

---

## Dashboard KPIs

The dashboard provides high-level fleet metrics and operational visibility.

Examples include:

- Fleet size
- Vehicle count
- Active vehicles
- Fleet status
- Risk indicators
- Maintenance indicators
- Alert indicators
- Analytics summaries

---

# AI Intelligence

The AI subsystem is the central intelligence layer of FleetVision AI.

The architecture combines multiple forms of intelligence rather than depending entirely on one machine-learning model.

The current architecture combines:

- Machine learning
- Deterministic thresholds
- Feature engineering
- Rule-based anomaly detection
- Domain heuristics
- Explainability templates
- Decision logic

This hybrid approach is deliberate because not every fleet-management decision requires a machine-learning model.

For example:

```text
Telemetry
    |
    v
Validation
    |
    v
Feature Engineering
    |
    +--------------------+--------------------+--------------------+
    |                    |                    |                    |
    v                    v                    v                    v
Speed Prediction      Risk Engine       Maintenance       Health Scoring
    |                    |                    |                    |
    +--------------------+--------------------+--------------------+
                             |
                             v
                      Driver Analysis
                             |
                             v
                    Anomaly Detection
                             |
                             v
                     Recommendations
                             |
                             v
                      Explainability
                             |
                             v
                       Decision Engine
                             |
                             v
                       Final AI Output
```

The complete AI analysis can combine information such as:

```text
prediction
risk_level
risk_score
speed_prediction
risk_analysis
maintenance_analysis
vehicle_health
driver_score
anomaly_analysis
advanced_anomaly_analysis
recommendations
ai_decision
explanations
engineered_features
```

---

# AI Speed Prediction

FleetVision AI includes a speed-prediction component.

The persisted model is located at:

```text
models/speed_prediction_model.pkl
```

The model is based on an engineered feature set.

A simplified example request is:

```bash
curl -X POST "http://localhost:8000/api/v1/ai/predict-speed" \
  -H "Content-Type: application/json" \
  -d '{
    "speed": 75,
    "previous_speed": 65
  }'
```

The endpoint provides predicted speed and related risk information.

The feature-generation pipeline and inference feature construction must remain compatible when the model is retrained.

---

# AI Risk Detection

The AI risk engine evaluates vehicle operating conditions and produces risk-related information.

Example:

```bash
curl -X POST "http://localhost:8000/api/v1/ai/detect-risk" \
  -H "Content-Type: application/json" \
  -d '{
    "speed": 105,
    "previous_speed": 90
  }'
```

The resulting analysis can contribute to:

- Risk level
- Risk score
- Safety indicators
- Driver/vehicle warnings
- Recommendations

---

# Complete AI Analysis

FleetVision AI provides a central AI analysis workflow.

Example:

```bash
curl -X POST "http://localhost:8000/api/v1/ai/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "vehicle_id": "vehicle-001",
    "latitude": 25.0,
    "longitude": 67.0,
    "speed": 85,
    "heading": 180,
    "ignition": true,
    "engine_running": true,
    "fuel": 55,
    "engine_temp": 92,
    "odometer": 85000,
    "previous_speed": 75
  }'
```

The complete orchestration layer combines multiple intelligence modules.

Conceptually:

```text
Input Telemetry
      |
      v
Feature Engineering
      |
      +----------+
      |          |
      v          v
 Speed Model   Risk Engine
      |          |
      +-----+----+
            |
            v
     Maintenance Analysis
            |
            v
      Vehicle Health
            |
            v
      Driver Analysis
            |
            v
    Anomaly Detection
            |
            v
     Recommendations
            |
            v
      Explainability
            |
            v
      Decision Engine
            |
            v
       AI Response
```

---

# Predictive Maintenance

Predictive maintenance attempts to identify components that may require attention before an actual failure occurs.

The current implementation uses engineered features, rules, and domain logic.

Example maintenance output:

```text
Vehicle: FV-001
Component: Engine
Failure Probability: 81%
Estimated Time: 12 days
Severity: Critical
Recommendation:
Schedule engine inspection and diagnostic testing.
```

Another example:

```text
Vehicle: FV-004
Component: Brake System
Failure Probability: 76%
Estimated Time: 18 days
Severity: High
Recommendation:
Inspect brake pads, discs and hydraulic pressure.
```

The purpose is to move fleet operations from purely reactive maintenance toward preventive decision-making.

---

# Vehicle Health Scoring

Vehicle health scoring combines operational indicators to estimate the current health condition of a vehicle.

Relevant inputs can include:

- Engine temperature
- Fuel
- Speed
- Maintenance probability
- Detected anomalies
- Operational behavior
- Telemetry indicators

The health score can then be surfaced through the dashboard and AI intelligence interface.

---

# Driver Behavior Intelligence

Driver intelligence analyzes operational behavior indicators.

Examples include:

- Fatigue probability
- Driving hours
- Harsh braking events
- Driver risk score
- Driver status

Example conceptual output:

```text
Driver
    |
    +-- Driving Hours
    |
    +-- Harsh Braking
    |
    +-- Fatigue Probability
    |
    +-- Risk Score
    |
    v
Driver Safety Assessment
```

This allows fleet operators to identify potentially unsafe driving behavior and intervene before it develops into a serious incident.

---

# Anomaly Detection

The current anomaly system is deterministic and rule-driven.

It identifies deviations from expected vehicle behavior.

Examples include:

```text
Temperature Spike
Pressure Drop
Vibration Pattern
Consumption Spike
Voltage Variation
```

An anomaly contains information such as:

- Vehicle
- Component
- Anomaly type
- Severity
- Detection time
- Description
- Status

Example:

```text
Vehicle: FV-001
Component: Engine
Anomaly: Temperature Spike
Severity: Critical

Description:
Engine temperature exceeded the expected operating range.
```

The architecture allows the anomaly subsystem to be replaced or augmented with statistical or machine-learning-based anomaly detection in the future.

---

# AI Recommendations

The recommendation layer converts intelligence into operational actions.

Recommendations can belong to categories such as:

- Safety
- Maintenance
- Performance
- Driver

Example:

```text
Immediate engine inspection

Engine temperature and maintenance indicators
show elevated failure risk.

Recommendation:
Schedule an inspection within the next 24 hours.
```

Another example:

```text
Brake system inspection

AI detected abnormal brake pressure behavior.

Recommendation:
Inspect the braking system before the next
long-distance trip.
```

The purpose of the recommendation system is to make AI output operationally useful rather than simply displaying model scores.

---

# Explainability

FleetVision AI includes explainability-style reasoning.

Instead of exposing only:

```text
Risk Score: 82
```

the platform can communicate why a vehicle has elevated risk.

For example:

```text
Elevated engine temperature
+
High maintenance probability
+
Driver fatigue indicators
+
Recent anomaly detection
=
High operational risk
```

Explainability helps fleet operators understand why an AI recommendation exists.

---

# AI Decision Engine

The decision engine combines AI outputs into an operational decision.

Conceptually:

```text
Predictions
     |
Risk Analysis
     |
Maintenance Analysis
     |
Health Score
     |
Driver Analysis
     |
Anomaly Detection
     |
Recommendations
     |
Explainability
     |
     v
Decision Engine
     |
     v
Operational Decision
```

This provides the final intelligence layer between raw analysis and fleet action.

---

# Analytics

FleetVision AI provides analytics capabilities for fleet operations.

Analytics can include:

- Fleet KPIs
- Vehicle statistics
- Telemetry trends
- Risk distribution
- Maintenance indicators
- Alert statistics
- Driver behavior indicators
- Vehicle health
- AI intelligence metrics

The frontend is implemented as a React/TypeScript dashboard and uses charting functionality for visual analytics.

---

# Frontend

The frontend is implemented separately from the backend archive.

The frontend uses:

- React
- TypeScript
- Vite
- React Router
- Axios
- Lucide React
- Recharts

The frontend provides the operator-facing dashboard and management interface.

The project includes pages for areas such as:

```text
Dashboard
Vehicles
Vehicle Details
Vehicle Editing
Fleets
Alerts
Analytics
AI Intelligence
```

The frontend communicates with the FastAPI backend through an API service layer.

The frontend contains reusable service modules for backend communication rather than placing API requests directly throughout every page.

Example:

```text
src/
├── components/
├── pages/
├── services/
├── types/
├── data/
├── router/
└── main.tsx
```

---

# Frontend AI Intelligence Interface

The AI Intelligence page presents the intelligence layer in a dashboard-oriented interface.

It provides sections for:

- Fleet risk
- Risk distribution
- Driver risk
- Predictive maintenance
- Vehicle anomalies
- AI recommendations
- Fleet-level AI summary

The interface can display:

```text
Average Risk
Vehicles At Risk
Predicted Failures
Critical Alerts
```

Vehicle risk information can include:

```text
Risk Score
Risk Level
Vehicle Health
Fatigue Probability
Anomaly Count
Maintenance Probability
```

---

# Frontend Vehicle Management

The vehicle interface supports:

```text
Create Vehicle
View Vehicle
Edit Vehicle
Delete Vehicle
```

Vehicle details include:

```text
Fleet
Make
Model
Year
Registration Number
VIN
Fuel Type
Color
Active Status
```

The vehicle list provides operational actions.

The view action is intended to display vehicle details.

The edit action uses a dedicated editing route.

---

# Technology Stack

## Backend

```text
Python
FastAPI
Pydantic
SQLAlchemy
Alembic
Uvicorn
PostgreSQL
Redis
```

## AI / Machine Learning

```text
pandas
NumPy
scikit-learn
joblib
SciPy
Matplotlib
```

## Frontend

```text
React
TypeScript
Vite
React Router
Axios
Lucide React
Recharts
```

## Security

```text
JWT
PyJWT
python-jose
pwdlib
bcrypt
cryptography
```

## Testing

```text
pytest
pytest-asyncio
pytest-cov
```

## Development Tools

```text
Black
Flake8
isort
```

## Infrastructure

```text
Docker
Docker Compose
PostgreSQL
Redis
```

---

# Repository Structure

The backend follows a modular architecture:

```text
Fleetvision-AI/
│
├── app/
│   ├── ai/
│   │   ├── alerts/
│   │   ├── anomaly/
│   │   ├── dataset/
│   │   ├── decision/
│   │   ├── evaluation/
│   │   ├── explainability/
│   │   ├── feature_engineering/
│   │   ├── inference/
│   │   ├── intelligence/
│   │   ├── preprocessing/
│   │   ├── recommendations/
│   │   ├── services/
│   │   ├── training/
│   │   ├── utils/
│   │   └── versioning/
│   │
│   ├── api/
│   │   ├── dependencies/
│   │   ├── routes/
│   │   └── v1/
│   │
│   ├── core/
│   ├── dashboard/
│   ├── database/
│   ├── exceptions/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── simulator/
│   ├── workers/
│   ├── dependencies.py
│   ├── lifespan.py
│   └── main.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── datasets/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── v1/
│   ├── v2/
│   ├── speed_prediction_model.pkl
│   ├── feature_importance.csv
│   ├── predictions.csv
│   ├── actual_vs_predicted.png
│   ├── residual_plot.png
│   └── latest.txt
│
├── scripts/
│   ├── generate_dataset.py
│   ├── build_features.py
│   ├── train_model.py
│   └── testing/
│
├── tests/
│   ├── ai/
│   └── api/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── .env.example
├── .gitignore
└── README.md
```

The supplied backend archive contains the backend and AI/ML implementation. The separate React frontend is maintained independently and should be considered part of the complete application when the frontend repository/version is included. 

---

# Backend Architecture

The backend uses a layered architecture.

```text
Client / Frontend
       |
       v
FastAPI Routes
       |
       v
Schemas / Validation
       |
       v
Services
       |
       +-----------------------+
       |                       |
       v                       v
Repositories              AI Modules
       |                       |
       v                       |
PostgreSQL <------------------+
       |
       +---- Redis
```

---

# API Layer

API routes are responsible for HTTP communication.

Versioned routes are exposed below:

```text
/api/v1
```

The API layer is separated from business logic so that the system remains modular.

---

# Schema Layer

Pydantic schemas define request and response contracts.

They are responsible for:

- Validation
- Serialization
- API data structures
- Input contracts
- Output contracts

---

# Service Layer

Services contain application and business logic.

The general flow is:

```text
API Route
    |
    v
Schema Validation
    |
    v
Service
    |
    +------> Repository
    |
    +------> AI Module
```

This separation makes the backend easier to maintain and test.

---

# Repository Layer

Repositories provide database-access abstractions.

Examples include repositories for:

```text
Vehicle
Fleet
Driver
User
Telemetry
Analytics
Dashboard
AI Prediction
```

This prevents database-access code from becoming tightly coupled to HTTP routes.

---

# Database

FleetVision AI uses PostgreSQL as its primary persistent database.

The database layer uses SQLAlchemy.

The system contains models for entities including:

```text
Users
Fleets
Vehicles
Drivers
Trips
Telemetry
Vehicle Status
Maintenance
Alerts
AI Predictions
```

Database configuration is assembled using environment variables:

```text
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
```

The resulting connection follows the general form:

```text
postgresql+psycopg2://USER:PASSWORD@HOST:PORT/DATABASE
```

---

# Redis

Redis is included as an infrastructure component.

It can support caching and future background-processing functionality.

Redis configuration uses:

```text
REDIS_HOST
REDIS_PORT
```

Redis should remain private in production.

---

# REST API

Versioned API endpoints are mounted below:

```text
/api/v1
```

## System

```text
GET /api/v1/health
GET /api/v1/database
```

## Authentication

```text
GET  /api/v1/auth/health
POST /api/v1/auth/register
POST /api/v1/auth/login
```

## Users

```text
GET    /api/v1/users/me
GET    /api/v1/users
POST   /api/v1/users
GET    /api/v1/users/{user_id}
PATCH  /api/v1/users/{user_id}
DELETE /api/v1/users/{user_id}
```

Additional versioned routes cover fleet, vehicle, driver, trip, telemetry, maintenance, alerts, analytics, dashboard, and AI functionality.

---

# API Health Check

Run:

```bash
curl http://localhost:8000/health
```

Expected response shape:

```json
{
  "status": "healthy",
  "application": "FleetVision AI"
}
```

---

# API Documentation

FastAPI automatically exposes interactive API documentation.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

These interfaces provide an interactive way to inspect and test available API endpoints.

---

# Authentication and Security

FleetVision AI includes authentication functionality.

Passwords are handled through password hashing utilities.

JWT-based authentication is used for protected API functionality.

Sensitive values must never be committed to Git.

Never commit:

```text
.env
SECRET_KEY
POSTGRES_PASSWORD
JWT secrets
TWILIO_AUTH_TOKEN
SMTP_PASSWORD
```

The repository should contain:

```text
.env.example
```

instead of the real environment file.

---

# Environment Configuration

Create a local environment file from the example:

```bash
cp .env.example .env
```

Then configure the required values.

Typical configuration includes:

```env
PROJECT_NAME=FleetVision AI
SECRET_KEY=change-this-value

POSTGRES_USER=postgres
POSTGRES_PASSWORD=change-this-value
POSTGRES_DB=fleetvision
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_HOST=localhost
REDIS_PORT=6379
```

Optional integrations may include:

```env
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=

SMTP_HOST=
SMTP_PORT=
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM_EMAIL=
```

Do not use placeholder secrets in a production environment.

---

# Database Migrations

Alembic manages database schema migrations.

Configuration:

```text
alembic.ini
```

Environment:

```text
alembic/env.py
```

Migration files:

```text
alembic/versions/
```

Run the current migrations:

```bash
alembic upgrade head
```

Generate a new migration:

```bash
alembic revision --autogenerate -m "describe change"
```

Generated migrations should always be reviewed before applying them.

---

# Docker

The backend contains a Dockerfile based on:

```text
python:3.12-slim
```

The Docker image:

1. Creates the application directory.
2. Installs Python dependencies.
3. Copies the application.
4. Exposes port `8000`.
5. Starts Uvicorn.

The container starts the API using:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# Docker Compose

Docker Compose provides the main backend infrastructure.

The primary services are:

```text
fleetvision-api
fleetvision-postgres
fleetvision-redis
```

PostgreSQL uses:

```text
postgres:16
```

Redis uses:

```text
redis:7
```

Persistent Docker volumes are used for:

```text
postgres_data
redis_data
```

This prevents database and Redis data from being lost when containers are recreated.

---

# Running with Docker Compose

Build the services:

```bash
docker compose build
```

Start the complete stack:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs -f api
```

Stop the services:

```bash
docker compose down
```

---

# Local Backend Development

Clone the repository:

```bash
git clone https://github.com/ham02zah/Fleetvision-AI.git
cd Fleetvision-AI
```

Create a Python 3.12 virtual environment:

```bash
python3.12 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Upgrade pip:

```bash
pip install --upgrade pip
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Start PostgreSQL and Redis.

If Docker Compose is configured with the corresponding service names:

```bash
docker compose up -d
```

Run migrations:

```bash
alembic upgrade head
```

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API is normally available at:

```text
http://localhost:8000
```

---

# Running the Frontend

The React frontend is maintained as the client-side application.

From the frontend directory:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend normally runs at:

```text
http://localhost:5173
```

Build the frontend:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

The frontend communicates with the FastAPI backend through its configured API service layer.

---

# Frontend Build Verification

Before committing frontend changes, run:

```bash
npm run build
```

A successful build should complete both TypeScript compilation and Vite production bundling.

Typical output ends with a successful Vite build.

If TypeScript reports an error, resolve the error before deployment.

---

# Dataset Generation

FleetVision AI includes dataset-generation utilities for development, testing, and demonstration.

Generate the dataset:

```bash
python scripts/generate_dataset.py
```

Build features:

```bash
python scripts/build_features.py
```

The generated datasets should be treated as synthetic/demo data unless replaced with real-world telematics data.

---

# Model Training

The training pipeline can be executed with:

```bash
python scripts/train_model.py
```

The training process can produce artifacts such as:

```text
models/
├── speed_prediction_model.pkl
├── feature_importance.csv
├── predictions.csv
├── actual_vs_predicted.png
├── residual_plot.png
└── latest.txt
```

Model artifacts should remain compatible with the feature-engineering pipeline used during inference.

---

# Model Evaluation

The project includes evaluation functionality for assessing model performance.

Evaluation artifacts can include:

```text
Feature importance
Predictions
Actual vs predicted plots
Residual plots
```

Example model-analysis files:

```text
models/feature_importance.csv
models/predictions.csv
models/actual_vs_predicted.png
models/residual_plot.png
```

These artifacts help determine whether the trained model is behaving as expected.

---

# Model Versioning

The project supports model versioning.

Model directories include:

```text
models/v1/
models/v2/
```

A versioned approach allows new model iterations to be introduced without immediately destroying previous artifacts.

The current active model can be tracked using:

```text
models/latest.txt
```

---

# Testing

The project includes tests for AI and API functionality.

Examples include:

```text
test_alert_engine.py
test_batch_prediction.py
test_feature_engineering.py
test_preprocessing.py
test_realtime_ai.py
test_ai_intelligence.py
```

Run the full test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app
```

Testing should be performed before production deployment.

---

# Useful Commands

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

## Build Docker Image

```bash
docker build -t fleetvision-api .
```

## Start Docker Compose

```bash
docker compose up -d
```

## Stop Docker Compose

```bash
docker compose down
```

## View Containers

```bash
docker compose ps
```

## View API Logs

```bash
docker compose logs -f api
```

## Run Migrations

```bash
alembic upgrade head
```

## Create Migration

```bash
alembic revision --autogenerate -m "migration description"
```

## Run Tests

```bash
pytest
```

## Generate Dataset

```bash
python scripts/generate_dataset.py
```

## Build Features

```bash
python scripts/build_features.py
```

## Train Model

```bash
python scripts/train_model.py
```

---

# Complete Development Workflow

A typical development workflow is:

```text
Clone Repository
       |
       v
Create Virtual Environment
       |
       v
Install Dependencies
       |
       v
Configure .env
       |
       v
Start PostgreSQL + Redis
       |
       v
Run Alembic Migrations
       |
       v
Start FastAPI
       |
       v
Start React Frontend
       |
       v
Test Application
       |
       v
Run AI/Data Pipeline
       |
       v
Run Tests
       |
       v
Build Frontend
       |
       v
Build Docker Images
       |
       v
Deploy
```

---

# Production Architecture

A production deployment can follow:

```text
                         INTERNET
                            |
                            v
                     Reverse Proxy
                       HTTPS / SSL
                            |
              +-------------+-------------+
              |                           |
              v                           v
         React Frontend              FastAPI API
                                          |
                           +--------------+--------------+
                           |                             |
                           v                             v
                      PostgreSQL                       Redis
                           |
                           v
                     Persistent Data
```

A more detailed architecture is:

```text
                         Internet
                            |
                            v
                     Nginx / HTTPS
                            |
              +-------------+-------------+
              |                           |
              v                           v
         Frontend                     FastAPI
                                          |
                              +-----------+-----------+
                              |                       |
                              v                       v
                         PostgreSQL                 Redis
                              |
                              v
                         Fleet Data
                              |
                              v
                       AI Intelligence
                              |
               +--------------+--------------+
               |              |              |
               v              v              v
             Risk       Maintenance      Anomaly
               |              |              |
               +--------------+--------------+
                              |
                              v
                       Recommendations
                              |
                              v
                       Fleet Operator
```

---

# Production Deployment Recommendations

For production deployment:

- Use a VPS or cloud server.
- Install Docker.
- Configure firewall rules.
- Keep PostgreSQL private where possible.
- Keep Redis private.
- Put the API behind HTTPS.
- Use strong production secrets.
- Set production configuration.
- Configure persistent database storage.
- Configure backups.
- Use a reverse proxy.
- Configure automatic container restart.
- Keep `.env` outside Git.
- Rotate credentials when necessary.

Never expose PostgreSQL or Redis publicly unless there is a specific operational requirement.

---

# Production Security

The following values must never be committed:

```text
.env
SECRET_KEY
POSTGRES_PASSWORD
JWT secrets
TWILIO_AUTH_TOKEN
SMTP_PASSWORD
```

Production should use:

```env
DEBUG=False
```

Database credentials should be strong and unique.

Redis should not be publicly accessible.

PostgreSQL should not be publicly accessible unless explicitly required.

The `.env.example` file should contain configuration placeholders but never real secrets.

---

# Git and GitHub

The project repository is:

```text
https://github.com/ham02zah/Fleetvision-AI
```

To check the current Git status:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Update FleetVision AI"
```

Push:

```bash
git push origin main
```

If the repository uses another branch, push to that branch instead.

Before pushing, verify that sensitive files are excluded:

```bash
git status
```

Make sure `.env` is not staged.

---

# Recommended .gitignore Entries

The repository should exclude local secrets, Python environments, generated files, and frontend dependencies.

Example:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
.pytest_cache/
.coverage
htmlcov/

# Virtual environment
venv/
.venv/
env/

# Environment variables
.env
.env.*
!.env.example

# IDE
.vscode/
.idea/

# macOS
.DS_Store

# Node
node_modules/
dist/

# Logs
*.log

# Temporary files
*.tmp
*.temp
```

---

# API and Frontend Relationship

The complete application can be viewed as two major layers.

```text
React / TypeScript Frontend
             |
             | HTTP / JSON
             v
        FastAPI Backend
             |
       +-----+------+
       |            |
       v            v
 PostgreSQL       Redis
       |
       v
 AI / Analytics / Operations
```

The frontend is responsible for:

- User interface
- Navigation
- Dashboard visualization
- Vehicle management
- Fleet management
- Alerts
- Analytics
- AI intelligence presentation
- User interaction

The backend is responsible for:

- API endpoints
- Authentication
- Validation
- Business logic
- Database access
- AI processing
- Telemetry
- Analytics
- Alerts
- Persistence

---

# AI Data Flow

A typical AI processing request follows:

```text
Vehicle Telemetry
       |
       v
API Request
       |
       v
Schema Validation
       |
       v
Preprocessing
       |
       v
Feature Engineering
       |
       +-------------------+
       |                   |
       v                   v
Speed Prediction      Risk Detection
       |                   |
       +---------+---------+
                 |
                 v
       Maintenance Analysis
                 |
                 v
         Vehicle Health
                 |
                 v
       Driver Risk Analysis
                 |
                 v
        Anomaly Detection
                 |
                 v
        Recommendation
                 |
                 v
         Explainability
                 |
                 v
         Decision Engine
                 |
                 v
          Final AI Output
```

---

# Example AI Scenario

Consider a vehicle reporting:

```json
{
  "vehicle_id": "vehicle-001",
  "latitude": 25.0,
  "longitude": 67.0,
  "speed": 85,
  "heading": 180,
  "ignition": true,
  "engine_running": true,
  "fuel": 55,
  "engine_temp": 92,
  "odometer": 85000,
  "previous_speed": 75
}
```

The system can process the information through multiple intelligence layers.

For example:

```text
Speed:
85 km/h

Previous Speed:
75 km/h

Engine Temperature:
92

Fuel:
55%

Odometer:
85,000

        |
        v

Feature Engineering
        |
        v

AI Analysis
        |
        +--> Speed Prediction
        |
        +--> Risk Detection
        |
        +--> Maintenance Analysis
        |
        +--> Vehicle Health
        |
        +--> Driver Score
        |
        +--> Anomaly Detection
        |
        +--> Recommendations
        |
        v

Decision Engine
```

This allows the platform to provide more meaningful information than a raw telemetry record.

---

# Current AI Implementation Notes

## Synthetic Data

The current dataset-generation utilities are intended for:

- Development
- Testing
- Demonstration

They should not automatically be interpreted as real-world telematics data.

Real-world deployment would require appropriately sourced and validated telemetry.

---

## Hybrid AI Architecture

FleetVision AI intentionally combines:

```text
Machine Learning
+
Deterministic Thresholds
+
Feature Engineering
+
Rule-Based Anomaly Detection
+
Domain Heuristics
+
Explainability
+
Decision Logic
```

This provides flexibility while avoiding unnecessary use of machine learning where deterministic logic is more appropriate.

---

## Speed Model

The speed prediction component uses:

```text
models/speed_prediction_model.pkl
```

The model expects a specific engineered feature set.

When retraining the model, the feature-generation pipeline and inference feature construction must remain compatible.

---

## Maintenance Prediction

The current maintenance predictor is feature/rule based rather than a separately persisted maintenance machine-learning model.

---

## Anomaly Detection

The current anomaly system is deterministic and rule-driven.

It can later be replaced or augmented with statistical or machine-learning anomaly detection.

---

# Current Project Status

FleetVision AI currently provides the foundation of a complete fleet-intelligence platform.

## Backend

```text
FastAPI REST API
PostgreSQL persistence
Redis integration
SQLAlchemy models
Alembic migrations
Authentication
Fleet management
Vehicle management
Driver management
Trip management
Maintenance
Telemetry
Vehicle status
Alerts
Dashboard APIs
Analytics APIs
```

## AI

```text
Speed prediction
Risk detection
Maintenance analysis
Vehicle health scoring
Driver behavior analysis
Anomaly detection
Feature engineering
Recommendations
Explainability
Decision engine
Batch inference
Prediction logging
Model evaluation
Model versioning
```

## Frontend

```text
React
TypeScript
Vite
React Router
Axios
Lucide React
Recharts

Dashboard
Fleet management
Vehicle management
Vehicle details
Vehicle editing
Alerts
Analytics
AI Intelligence
```

## Infrastructure

```text
Docker
Docker Compose
Persistent PostgreSQL volume
Persistent Redis volume
Environment configuration
Production-oriented container restart configuration
```

---

# Project Strengths

FleetVision AI is designed as a portfolio-level AI engineering project rather than a single machine-learning notebook.

It demonstrates experience across:

```text
Software Engineering
        |
        +-- REST APIs
        +-- Authentication
        +-- Database Design
        +-- Repository Pattern
        +-- Service Architecture
        +-- Validation
        +-- Migrations

Machine Learning
        |
        +-- Dataset Generation
        +-- Feature Engineering
        +-- Model Training
        +-- Prediction
        +-- Evaluation
        +-- Model Versioning

AI Engineering
        |
        +-- Risk Analysis
        +-- Maintenance Intelligence
        +-- Anomaly Detection
        +-- Recommendations
        +-- Explainability
        +-- Decision Engine

Frontend Engineering
        |
        +-- React
        +-- TypeScript
        +-- Routing
        +-- API Integration
        +-- Dashboards
        +-- Charts
        +-- Fleet UI

DevOps
        |
        +-- Docker
        +-- Docker Compose
        +-- PostgreSQL
        +-- Redis
        +-- Environment Management
```

---

# Future Expansion

The architecture supports future additions such as:

- Real GPS/telematics ingestion
- MQTT ingestion
- Kafka streaming
- Real-time WebSocket dashboards
- LSTM time-series models
- Transformer time-series models
- Dedicated maintenance ML models
- Advanced anomaly detection
- Driver fatigue computer vision
- Geofencing
- Route optimization
- Fuel consumption prediction
- Fleet cost optimization
- Automated notification delivery
- Cloud object storage
- Model registry
- CI/CD
- Kubernetes deployment
- Prometheus monitoring
- Grafana monitoring

These are extension points and are not requirements for the current implementation.

---

# Limitations

FleetVision AI should currently be understood as a fleet-intelligence foundation and demonstration platform.

The system should not be represented as a fully autonomous safety-critical fleet-control system.

In particular:

- Synthetic data should not be treated as real-world telemetry.
- Rule-based anomaly detection is not equivalent to production-grade ML anomaly detection.
- Predictive maintenance results require validation against real maintenance outcomes.
- AI risk scores should be validated against real operational incidents before being used for safety-critical decisions.
- The speed model depends on compatible feature engineering.
- Production deployment requires proper security configuration.
- Real-world fleet deployments require monitoring, logging, validation, backups, and operational controls.

---

# Deployment Checklist

Before production deployment:

```text
[ ] Backend builds successfully
[ ] Frontend builds successfully
[ ] Tests pass
[ ] Docker image builds successfully
[ ] Docker Compose starts successfully
[ ] PostgreSQL is persistent
[ ] Redis is persistent where required
[ ] Alembic migrations are applied
[ ] Production .env is configured
[ ] .env is excluded from Git
[ ] Strong SECRET_KEY configured
[ ] Strong PostgreSQL password configured
[ ] JWT secrets configured
[ ] HTTPS configured
[ ] Reverse proxy configured
[ ] Firewall configured
[ ] PostgreSQL not publicly exposed
[ ] Redis not publicly exposed
[ ] API health check verified
[ ] Frontend API URL configured
[ ] AI model files available
[ ] Database backup strategy configured
[ ] Logs reviewed
```

---

# Quick Start

For a quick local setup:

```bash
git clone https://github.com/ham02zah/Fleetvision-AI.git

cd Fleetvision-AI

python3.12 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

cp .env.example .env

docker compose up -d

alembic upgrade head

uvicorn app.main:app --reload
```

Then open:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

For the React frontend:

```bash
cd frontend

npm install

npm run dev
```

The frontend normally runs at:

```text
http://localhost:5173
```

---

# Docker Quick Start

Build:

```bash
docker compose build
```

Start:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs -f api
```

Verify the API:

```bash
curl http://localhost:8000/health
```

Stop:

```bash
docker compose down
```

---

# Project Architecture Summary

The complete FleetVision AI architecture can be summarized as:

```text
                           FLEETVISION AI
                                |
          +---------------------+---------------------+
          |                                           |
          v                                           v
    Fleet Operations                           AI Intelligence
          |                                           |
   +------+------+------+                    +--------+--------+
   |      |      |      |                    |        |        |
 Fleets Vehicles Drivers Trips              Risk  Prediction Anomaly
   |      |      |      |                    |        |        |
   +------+------+------+                    +--------+--------+
          |                                           |
          v                                           v
      Telemetry                                Maintenance
          |                                           |
          v                                           v
       Alerts                                   Health Score
          |                                           |
          +---------------------+---------------------+
                                |
                                v
                         Decision Engine
                                |
                                v
                       AI Recommendations
                                |
                                v
                         Fleet Operator
```

The application is ultimately designed around one principle:

```text
RAW FLEET DATA
      ↓
DATA PROCESSING
      ↓
AI / ANALYTICS
      ↓
RISK + HEALTH + PREDICTIONS
      ↓
EXPLANATIONS
      ↓
RECOMMENDATIONS
      ↓
OPERATIONAL DECISIONS
```

FleetVision AI therefore acts as an intelligent layer between fleet data and fleet operations.

---

# Author

**Hamzah Jawad**

Artificial Intelligence Engineer / Developer

FleetVision AI