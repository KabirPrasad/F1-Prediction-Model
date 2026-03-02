
"""
model_loader.py

This file centralizes model and data loading.

Responsibilities:
- Load trained .pkl model
- Load prediction dataset
- Handle feature preprocessing setup
- Optionally cache model in memory

This file should NOT:
- Perform business logic
- Format outputs
- Call LLM
"""
import joblib
import pandas as pd

MODEL_PATH = "f1_trained_model.pkl"
PREDICTIONS_PATH = "predictions.csv"

_model_cache = None
_predictions_cache = None


def load_model():
    global _model_cache
    if _model_cache is None:
        _model_cache = joblib.load(MODEL_PATH)
    return _model_cache


def load_prediction_data():
    global _predictions_cache
    if _predictions_cache is None:
        _predictions_cache = pd.read_csv(PREDICTIONS_PATH)
    return _predictions_cache
