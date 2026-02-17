"""
merge_tables.py

Purpose:
Load data from the folder F1 Data - take the columns which are relevant and make a final dataset. 
Merge raw F1 CSV tables into a single race-driver dataset.
Each row represents one driver in one race. Of current drivers only
"""


def merge_tables(dataframes):
    """
    Merges results, races, drivers, constructors, qualifying, and status tables.

    Args:
        dataframes (dict): Dictionary of pandas DataFrames loaded from CSVs

    Returns:
        pandas.DataFrame: Final merged race-driver dataset
    """

    results = dataframes["results"]
    races = dataframes["races"]
    drivers = dataframes["drivers"]
    constructors = dataframes["constructors"]
    qualifying = dataframes["qualifying"]
    status = dataframes["status"]

    # Selecting relevant columns only
    results = results[
        [
            "raceId",
            "driverId",
            "constructorId",
            "grid",
            "positionOrder",
            "points",
            "laps",
            "milliseconds",
            "fastestLapSpeed",
            "statusId",
        ]
    ]

    races = races[
        [
            "raceId",
            "year",
            "round",
            "circuitId",
        ]
    ]

    drivers = drivers[
        [
            "driverId",
            "forename",
            "surname",
            "dob",
            "nationality",
        ]
    ]

    constructors = constructors[
        [
            "constructorId",
            "name",
            "nationality",
        ]
    ]

    qualifying = qualifying[
        [
            "raceId",
            "driverId",
            "position",
        ]
    ].rename(columns={"position": "quali_position"})

    status = status[
        [
            "statusId",
            "status",
        ]
    ]

  
    # Merging tables


    df = results.merge(races, on="raceId", how="left")

    df = df.merge(drivers, on="driverId", how="left")

    df = df.merge(constructors, on="constructorId", how="left")

    df = df.merge(
        qualifying,
        on=["raceId", "driverId"],
        how="left"
    )

    df = df.merge(status, on="statusId", how="left")

 # Preparing target variable 

    df = df.rename(columns={"positionOrder": "finish_position"})

    df["finish_position"] = pd.to_numeric(df["finish_position"], errors="coerce")

    # Keep only finished races if desired
    df = df[df["finish_position"].notna()]

    # Sort nicely
    df = df.sort_values(["year", "round", "finish_position"])

    df = df.reset_index(drop=True)

    return df

