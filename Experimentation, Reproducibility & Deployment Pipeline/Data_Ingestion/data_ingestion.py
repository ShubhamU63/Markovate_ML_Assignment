import pandas as pd
import os
import yaml
from typing import Dict, Any
from datetime import datetime
import logging

MONITOR_DIR = "Monitoring"
os.makedirs(MONITOR_DIR, exist_ok=True)

baseline_path= "Experimentation, Reproducibility & Deployment Pipeline\Baseline\train.csv"
def read_params(path='config/params.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_logger(name: str, logfile: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(os.path.join(MONITOR_DIR, logfile))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

validation_logger = get_logger("validation_logger", "validation.log")
error_logger = get_logger("error_logger", "error.log")

def validate_data(df: pd.DataFrame, baseline_path: str) -> Dict[str, Any]:
    """Validate CSV structure against baseline"""
    try:
        if not baseline_path:
            raise FileNotFoundError(f"Baseline not found at {baseline_path}")
        
        base = pd.read_csv(baseline_path, nrows=1000)
        validation_logger.info(f"Baseline loaded with {len(base.columns)} columns")

        missing_cols = list(set(base.columns) - set(df.columns))
        extra_cols = list(set(df.columns) - set(base.columns))

        dtype_mismatch = []
        for col in base.columns.intersection(df.columns):
            if str(base[col].dtype) != str(df[col].dtype):
                dtype_mismatch.append({
                    "column": col,
                    "baseline_dtype": str(base[col].dtype),
                    "file_dtype": str(df[col].dtype)
                })

        validation_logger.info("Validation completed successfully")
        return {
            "missing_columns": missing_cols,
            "extra_columns": extra_cols,
            "dtype_mismatch": dtype_mismatch,
            "rows": len(df),
            "cols": len(df.columns),
            "status": "valid"
        }

    except Exception as e:
        error_logger.exception("Validation error")
        return {"status": "error", "message": str(e)}