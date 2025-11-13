from dotenv import load_dotenv
import os
from google import genai
from datetime import datetime

# Load .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("환경변수 GEMINI_API_KEY 설정되어 있지 않습니다. .env에 추가하세요.")

# Create client with API key
client = genai.Client(api_key=api_key)

# Get today's date
today = datetime.now().strftime("%B %d, %Y")

# List to store conversation history
conversation_history = []

print("Chat started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chat ended.")
        break

    # Build conversation memory for the prompt
    # Each turn is clearly marked as User/AI
    prompt_lines = []
    
    # Add today's date at the start (model knows the date)
    if not prompt_lines:
        prompt_lines.append(f"Today's date is {today}.")
        prompt_lines.append("")
    
    for q, a in conversation_history:
        prompt_lines.append(f"User: {q}")
        prompt_lines.append(f"AI: {a}")
    prompt_lines.append(f"User: {user_input}")
    prompt_lines.append("AI:")

    prompt = "\n".join(prompt_lines)

    # Send prompt with memory to the model
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    print("AI:", response.text.strip())

    # Save this turn to memory
    conversation_history.append((user_input, response.text.strip()))칟