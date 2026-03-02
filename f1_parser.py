"""
f1_parser.py

This file handles LLM-based intent extraction.

Responsibilities:
- Define system prompt for Gemini
- Convert natural language question into structured dictionary
- Validate and safely parse LLM output
- Return standardized dictionary format

Expected schema example:
{
    "year": 2026,
    "race": "Australia",
    "request": "podium"
}

Supported request types:
- podium
- winner
- top_10
- driver_position
- team_points
- season_simulation

This file should NOT:
- Call ML model
- Load data
- Format final user responses
"""
import json
from utils import safe_parse_llm_output


def parse_query(user_input, llm):

    system_prompt = """
    You are an F1 query parser.

    Convert the user question into a Python dictionary with this schema:

    {
        "year": int,
        "race": int,
        "request": "winner" | "podium" | "top_10" | "driver_position",
        "driver": optional string
    }

    - race should be the race round number (integer).
    - If driver is not needed, omit it.
    - Return ONLY a valid Python dictionary.
    """

    response = llm.invoke(system_prompt + "\nUser: " + user_input)

    return safe_parse_llm_output(response.content)
    pass
