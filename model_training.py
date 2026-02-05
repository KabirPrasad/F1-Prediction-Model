"""
model_training.py

This file is responsible for training and evaluating the ML model


- Loads the prepared dataset from data_pipeline.py
- Defines the prediction target (race outcome for a single race)
- Splits the data using time-aware validation
- Trains a baseline model
- Trains an improved model
- Evaluates model performance using appropriate metrics
- Saves the trained model for future predictions

The goal of this file is to produce a trained model
that can generalize to unseen races.
"""
