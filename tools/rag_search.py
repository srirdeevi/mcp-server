from auth import authenticate
import requests


def search_documents(
        question: str,
        api_key: str
):

    authenticate(api_key)

    response = requests.get(
        "http://127.0.0.1:8000/search",
        params={
            "question": question
        }
    )

    response.raise_for_status()

    return response.json()["answer"]
