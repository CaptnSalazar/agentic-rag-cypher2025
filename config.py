import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_INDEX_PATH = os.getenv("VECTOR_INDEX_PATH", "./vector_index")
WEB_SEARCH_API_KEY = os.getenv("WEB_SEARCH_API_KEY")  # optional

# LLM client config: replace with any client wrapper
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

# Hyperparams
TOP_K = int(os.getenv("TOP_K", 5))
TRUST_SOURCE_THRESHOLD = float(os.getenv("TRUST_SOURCE_THRESHOLD", 0.4))