from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
from fastapi.responses import JSONResponse
from Data_Ingestion.data_ingestion import validate_data, read_params
from Model_Training.train import train_model
app = FastAPI()

BASELINE_PATH = "Baseline/train.csv"
PARAMS_PATH = "config/params.yaml"

@app.get("/")
async def root():
    return {"message": "Welcome to the MLOps Classification API"}

@app.post("/train-model")
async def train_endpoint(file: UploadFile = File(...)):
    """Train a model from uploaded CSV"""
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Validate before training
        validation_result = validate_data(df, BASELINE_PATH)
        if validation_result.get("status") == "error":
            raise HTTPException(status_code=400, detail=validation_result["message"])

        # Train model (set your target column name here)
        result = train_model(df, target="Survived", params_path=PARAMS_PATH)
        return JSONResponse(content={
            "message": "Model trained successfully",
            "accuracy": result["accuracy"],
            "model_path": result["model_path"],
            "report_path": result["report_path"]
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))