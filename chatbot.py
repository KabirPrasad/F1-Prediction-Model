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


def process_query(user_input, llm):
    """
    Main entry point for chatbot logic.

    Steps:
    1. Parse user input using LLM
    2. Validate parsed structure
    3. Determine request type
    4. Call appropriate engine function
    5. Format and return final response
    """

    # 1. Parse query
    # 2. Check for parsing errors
    # 3. Route based on request type
    # 4. Return formatted result
    pass
