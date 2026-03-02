"""
f1_chatbot.py

This file acts as the orchestration layer.

Responsibilities:
- Receive raw user input
- Call the LLM parser (f1_parser.py)
- Interpret structured intent
- Route request to correct engine function (f1_engine.py)
- Format final natural language response
- Handle errors gracefully

This file should NOT:
- Load models
- Define LLM prompts
- Contain Flask code
"""

from f1_parser import parse_query
from f1_engine import (
    get_podium,
    get_winner,
    get_top_10,
    get_driver_position,
    simulate_season
)
from utils import format_response
from f1_parser import parse_query
from f1_engine import (
    get_podium,
    get_winner,
    get_top_10,
    get_driver_position
)
from utils import format_response


def process_query(user_input, llm):

    parsed = parse_query(user_input, llm)

    if not parsed:
        return "Sorry, I couldn't understand the question."

    request_type = parsed.get("request")
    year = parsed.get("year")
    race = parsed.get("race")

    if request_type == "winner":
        result = get_winner(year, race)

    elif request_type == "podium":
        result = get_podium(year, race)

    elif request_type == "top_10":
        result = get_top_10(year, race)

    elif request_type == "driver_position":
        driver = parsed.get("driver")
        result = get_driver_position(year, race, driver)

    else:
        return "Unsupported request type."

    return format_response(result, request_type)
