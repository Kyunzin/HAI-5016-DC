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
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
print(response.text)