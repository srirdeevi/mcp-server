import os
from dotenv import load_dotenv


load_dotenv()


EXPECTED_API_KEY = os.getenv(
    "MCP_API_KEY"
)


def authenticate(api_key: str):

    if api_key != EXPECTED_API_KEY:
        raise Exception(
            "Unauthorized: Invalid API Key"
        )

    return True
