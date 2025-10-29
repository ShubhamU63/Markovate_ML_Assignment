 ```
Experimentation, Reproducibility & Deployment Pipeline/
│
├── app/
│   ├── main.py                     # FastAPI app entry point
│
│
├── Data_Ingestion/
│   ├── data_ingestion.py           # Data validation, logging, YAML loading
│   ├── __init__.py
│ 
├── Model_Training/
│   ├── train.py                    # Model training pipeline
│
├── Model_Artifacts_Registry/
│   ├── models/                     # Saved model pipelines
│   └── reports/                    # Generated classification reports
│
├── Baseline/train.csv              # Baseline dataset schema reference
├── config/params.yaml              # Model parameters & training configs
├── Monitoring/                     # Logs (validation, errors, training)
│   ├── error.log                     # Saved model pipelines
│   └── training.log
│   └── validation.log
├── sapp.py                      # Streamlit frontend app
│
│
├── requirement.txt
└── README.md
 ```
![alt text](<Mlops Architecture.png>)

## Clone Repository

git clone [<your-repo-url>](https://github.com/ShubhamU63/Markovate_ML_Assignment.git)
cd project_root

## Create Virtual Environment
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate   

## Install Dependencies
pip install -r requirements.txt

## Backend – FastAPI---Run FastAPI
uvicorn app.main:app --reload

Server runs at 👉 http://127.0.0.1:8000

## Frontend – Streamlit --Run Streamlit
streamlit run frontend/app.py


Frontend runs at 👉 http://localhost:8501



## Example Response

```
{
  "message": "Model trained successfully",
  "accuracy": 0.83,
  "model_path": "Model_Artifacts_Registry/models/pipeline_model_20251029_202100.joblib",
  "report_path": "Model_Artifacts_Registry/reports/report_20251029_202100.txt"
}
```

## Streamlit Frontend Features
File uploader for dataset CSV

Sends data to /train-model endpoint

Displays training metrics in a styled box

Shows report text file output directly in the interface


## Configuration (config/params.yaml)


seed: 42
test_size: 0.2



## Logging
All logs are stored in the Monitoring/ directory:

validation.log → Data validation steps

error.log → Any validation or ingestion errors

training.log → Model training details


## Outputs
After running /train-model, the following artifacts are created:

Trained Model: Model_Artifacts_Registry/models/pipeline_model_<timestamp>.joblib

Report File: Model_Artifacts_Registry/reports/report_<timestamp>.txt

Accuracy: Displayed in frontend