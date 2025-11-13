from dotenv import load_dotenv
import os
from google import genai

# .env 파일을 로드합니다
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("환경변수 GEMINI_API_KEY 설정되어 있지 않습니다. .env에 추가하세요.")

# API 키로 클라이언트 생성
client = genai.Client(api_key=api_key)
print("Client initialized:", type(client))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="How many days until christmas? Today is November 13."
    )
print(response.text)

print("---------------")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="How is the weather usually like around that time?"
    )
print(response.text)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # Make a loop that asks for the user's input and sends it to the model until the user types 'exit'    
while True:
    user_input = input("Enter your question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    print("Response:", response.text)