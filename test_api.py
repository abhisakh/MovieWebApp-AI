#import google.generativeai as genai
from google import genai
import os
from dotenv import load_dotenv

# -----------------------------
# 1. API Key Handling (Crucial Change)
# -----------------------------
# It's highly recommended to load the key from an environment variable (.env file)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Replace the placeholder key with your actual, loaded key
if not GEMINI_API_KEY:
    # Use a placeholder (THIS WILL FAIL) or raise an error if needed
    print("❌ WARNING: GEMINI_API_KEY not found in .env. Replace the placeholder below.")
    # NOTE: You MUST replace "YOUR_ACTUAL_API_KEY" with a valid key for the code to work.
    API_KEY = "YOUR_ACTUAL_API_KEY"
else:
    API_KEY = GEMINI_API_KEY

# -----------------------------
# 2. Modern Client Initialization (Crucial Change)
# -----------------------------
# Initialize the client. This replaces the old genai.configure()
client = genai.Client(api_key=API_KEY)

# -----------------------------
# 3. Chat Session using Modern Client
# -----------------------------
# Define the model name
model_name = "gemini-2.5-flash"  # Use the standard, current model name

try:
    # Use client.chats.create for a new session
    # The 'client' handles the API key and configuration
    session = client.chats.create(model=model_name)

    # Send a message using the modern session.send_message
    response = session.send_message("Suggest 5 movies about space exploration")

    # Print the model's reply (access response.text instead of response.output_text)
    print("\n--- Model Response ---")
    print(response.text)
    print("----------------------")

except Exception as e:
    print(f"\n❌ An error occurred: {e}")
    print("Ensure you have a valid and correctly configured API key.")