"""
f1_engine.py

This file contains ALL prediction logic.

Responsibilities:
- Load trained ML model (via model_loader.py)
- Generate race predictions
- Sort predicted finishing positions
- Compute derived results (podium, winner, etc.)
- Return structured prediction results

This file should NOT:
- Call LLM
- Handle Flask routes
- Format HTML
"""

from model_loader import load_model, load_prediction_data

from model_loader import load_prediction_data


def _filter_race(df, year, race):
    return df[(df["year"] == year) & (df["round"] == race)]


def get_winner(year, race_name):
    df = load_prediction_data()
    race_df = _filter_race_by_name(df, year, race_name)

    race_df = race_df.sort_values("predicted_finish")

    if race_df.empty:
        return None

    return race_df.iloc[0]


def get_podium(year, race):
    df = load_prediction_data()
    race_df = _filter_race(df, year, race)
    race_df = race_df.sort_values("predicted_finish")
    return race_df.head(3)


def get_top_10(year, race):
    df = load_prediction_data()
    race_df = _filter_race(df, year, race)
    race_df = race_df.sort_values("predicted_finish")
    return race_df.head(10)


def get_driver_position(year, race, driver):
    df = load_prediction_data()
    race_df = _filter_race(df, year, race)

    driver_row = race_df[
        race_df["driver_surname"].str.lower() == driver.lower()
    ]

    if driver_row.empty:
        return None

    return driver_row.iloc[0]
    Return top 10 predicted finishers.
    """
    pass


def get_driver_position(year, race, driver):
    """
    Return predicted finishing position for a specific driver.
    """
    pass

def _filter_race_by_name(df, year, race_name):
    return df[
        (df["year"] == year) &
        (df["name"].str.lower() == race_name.lower())
    ]
def simulate_season(year):
    """
    Simulate full season standings based on model predictions.
    """
    pass
