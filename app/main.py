from fastapi import FastAPI

app = FastAPI(
    title="FleetVision AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "FleetVision AI API Running"
    }