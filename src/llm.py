from dotenv import load_dotenv
from langchain_community.chat_models import ChatMaritalk
import os

load_dotenv()

llm = ChatMaritalk(
    model="sabia-3",
    api_key= os.getenv("CHAVE_API"),
    temperature=0.7,
    max_tokens=100
)
