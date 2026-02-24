
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


def load_model():
    """
    Load trained model from disk.
    Return model object.
    """
    pass


def load_prediction_data():
    """
    Load dataset used for prediction.

    Could:
    - Read CSV
    - Prepare feature matrix
    - Filter by year/race
    """
    pass
