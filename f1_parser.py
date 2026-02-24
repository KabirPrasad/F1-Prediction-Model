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
    """
    Use Gemini to convert user input into structured dictionary.

    Steps:
    1. Define system prompt explaining expected schema
    2. Call llm.invoke()
    3. Safely parse response
    4. Validate keys and return dictionary
    """

    # 1. Create system prompt
    # 2. Invoke LLM
    # 3. Parse response safely
    # 4. Return structured dict
    pass
