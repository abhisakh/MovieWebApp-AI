# ai_movie_navigator.py

import os
import re
import json
from dotenv import load_dotenv
import google.genai as genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel, Field
import logging

# Load environment variables
load_dotenv()

# -----------------------------
# GEMINI SETUP (Diagnostic Check)
# -----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    client = None
    print("❌ ERROR: GEMINI_API_KEY IS MISSING or FAILED TO LOAD.") # <--- CHECK YOUR CONSOLE FOR THIS!
else:
    # Print the last few characters to confirm it loaded (but not the whole key)
    print(f"✅ GEMINI_API_KEY loaded. Ends with: ...{GEMINI_API_KEY[-4:]}")
    client = genai.Client(api_key=GEMINI_API_KEY)
# -----------------------------


# 1. Define the desired output structure using Pydantic
class MovieSuggestion(BaseModel):
    """Schema for a single movie suggestion."""
    title: str = Field(description="The primary English title of the movie.")
    year: int = Field(description="The movie's release year. Use 0 if the year is unknown.")
    director: str = Field(description="The director's full name. Use 'Unknown' if the director is unknown.")

class MovieSuggestionList(BaseModel):
    """The required container for exactly 5 movie suggestions."""
    suggestions: list[MovieSuggestion] = Field(description="A list of 5 movies that match the user's request.")


def get_ai_movie_suggestions(query, max_suggestions=5):
    """
    Generates structured movie suggestions using the Gemini API,
    reliable for complex queries.

    Returns: (list of dicts, model_name_str)
    """
    model_name = "gemini-2.5-flash"

    if not client:
        logging.error("GEMINI_API_KEY is missing or invalid.")
        return ([], "API Key Missing")
    if not query:
        return ([], model_name)

    try:
        # ... (System Instruction and Config setup remain the same) ...
        system_instruction = (
            "You are an expert cinematic recommendation engine. Your task is to analyze the user's "
            "request (e.g., genre, topic, theme, or simple title) and provide a list of exactly "
            f"{max_suggestions} relevant movie suggestions. The output MUST be a JSON object that adheres "
            "strictly to the provided MovieSuggestionList JSON schema. Do not include any preamble, commentary, "
            "or text outside the required JSON."
        )

        prompt = f"Suggest {max_suggestions} movies related to '{query}'."

        config = GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=MovieSuggestionList,
            temperature=0.4
            #max_output_tokens=512,
        )

        # 🚀 THE GEMINI API CALL (MODERN SDK)
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=config
        )

        # 1. CRITICAL FIX: Check if the response text is None (e.g., due to safety block)
        if response.text is None:
            logging.error(f"Gemini returned an empty response (NoneType text) for query: '{query}'")
            return ([], "Error")

        # 2. Proceed only if response.text is a string, and strip it once.
        raw_text = response.text.strip()

        # 🧪 Debugging Step: Log the raw response
        logging.info(f"Raw Gemini response start: {raw_text[:100]}...")

        # 3. Parse the structured JSON response
        json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)

        if json_match:
            json_string = json_match.group(0)
        else:
            logging.error(f"Could not find JSON block in response for query: '{query}'. Full text: {raw_text}")
            return ([], "Error")

        try:
            data = json.loads(json_string)
            suggestions = data.get('suggestions', [])
        except json.JSONDecodeError as json_e:
            logging.error(f"JSON Decoding failed. Query: '{query}'. Error: {json_e}")
            return ([], "Error")

        # Return the clean list of movie dictionaries
        return (suggestions, model_name)

    except Exception as e:
        # Check 3: General API/Connection Error
        logging.error(f"General API error fetching AI suggestions for '{query}': {e}")
        # === ⚠️ TEMPORARY DIAGNOSTIC LINE ===
        print(f"⚠️ DIAGNOSTIC ERROR for query '{query[:50]}...': {e}")
        # ===================================

        return ([], "Error")

# -----------------------------
# Test Block (Optional) - Now tests a complex query
# -----------------------------
if __name__ == "__main__":
    # Test the complex query that previously failed
    test_query = "best movies in last five years"
    suggestions, model = get_ai_movie_suggestions(test_query)
    print(f"\n--- AI Suggestions for: '{test_query}' ({model}) ---")
    if suggestions:
        for s in suggestions:
            # The output is now clean Python dictionaries
            print(s)
    else:
        print("No suggestions returned.")