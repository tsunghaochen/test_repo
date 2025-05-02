import os
import requests

def my_validation(output: str, validation: str) -> float:
    # test external API installed in infrastructure/zenml/poetry.toml
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(f"External API response: {response.json()}")
    score = len(output) / 100
    print(f"Validation of [{output}] using [{validation}] is [{score}]")
    return score


if __name__ == "__main__":
    my_validation("AXA_contract.pdf", "LLM_AAJ")