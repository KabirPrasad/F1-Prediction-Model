"""
utils.py

Shared helper functions.

Responsibilities:
- Race name normalization
- Driver name normalization
- Year validation
- Output formatting
- Safe LLM output parsing

This keeps logic clean across files.
"""
import ast


def safe_parse_llm_output(text):
    try:
        return ast.literal_eval(text)
    except Exception:
        return None


def format_response(data, request_type):

    if data is None:
        return "No prediction found."

    if request_type == "winner":
    return (
        f"Based on the model's 2026 predictions, "
        f"{data['driver_forename']} {data['driver_surname']} "
        f"is projected to win the {data['name']}."
    )

    if request_type == "podium":
        response = "🏆 Predicted Podium:\n"
        for i, (_, row) in enumerate(data.iterrows(), start=1):
            response += (
                f"{i}. {row['driver_forename']} "
                f"{row['driver_surname']} "
                f"({row['constructor_name']})\n"
            )
        return response

    if request_type == "top_10":
        response = "🔟 Predicted Top 10:\n"
        for i, (_, row) in enumerate(data.iterrows(), start=1):
            response += (
                f"{i}. {row['driver_forename']} "
                f"{row['driver_surname']}\n"
            )
        return response

    if request_type == "driver_position":
        return (
            f"📍 Predicted Finish:\n"
            f"{data['driver_forename']} {data['driver_surname']} "
            f"→ P{int(round(data['predicted_finish']))}"
        )
    
    return "Unknown request."
