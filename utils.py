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


def normalize_race_name(race):
    """
    Convert informal race names into standardized format.
    Example:
    'aussie gp' -> 'Australia'
    """
    pass


def validate_year(year):
    """
    Ensure year is integer and within supported range.
    """
    pass


def format_response(data, request_type):
    """
    Convert structured prediction output into
    clean natural language response.
    """
    pass


def safe_parse_llm_output(text):
    """
    Safely convert LLM string output into dictionary.

    Avoid using raw eval().
    Use ast.literal_eval or JSON parsing.
    """
    pass
